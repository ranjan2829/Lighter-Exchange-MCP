"""
Position management tools for Lighter Exchange.

Tools for fetching positions and closing them.
"""

import os
import json
import asyncio
from typing import Optional, Literal
import lighter


def get_config():
    """Get Lighter configuration."""
    config_file = os.path.join(os.path.dirname(__file__), "..", "api_key_config.json")
    if os.path.exists(config_file):
        with open(config_file) as f:
            cfg = json.load(f)
        return {
            "base_url": cfg["baseUrl"],
            "account_index": cfg["accountIndex"],
            "private_keys": {int(k): v for k, v in cfg["privateKeys"].items()}
        }
    return None


def _run_async(coro):
    """Run async coroutine synchronously."""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, coro)
                return future.result()
        return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)


def get_positions() -> str:
    """Get all open positions with PnL for the account.

    Returns:
        JSON string with all positions including:
        - Market symbol and ID
        - Position size and side (long/short)
        - Entry price
        - Current value
        - Unrealized PnL
        - Liquidation price
    """
    config = get_config()
    if not config:
        return json.dumps({"error": "Config not found"})

    import httpx
    url = f"{config['base_url']}/api/v1/account"
    params = {"by": "index", "value": str(config["account_index"])}

    with httpx.Client(timeout=30) as client:
        response = client.get(url, params=params)
        data = response.json()

    if data.get("code") != 200:
        return json.dumps({"error": "Failed to fetch account"})

    acc = data["accounts"][0]
    positions = []

    for p in acc["positions"]:
        size = float(p["position"])
        if size != 0:
            positions.append({
                "market": p["symbol"],
                "market_id": p["market_id"],
                "side": "LONG" if p["sign"] == 1 else "SHORT",
                "size": p["position"],
                "entry_price": p["avg_entry_price"],
                "position_value": p["position_value"],
                "unrealized_pnl": p["unrealized_pnl"],
                "realized_pnl": p["realized_pnl"],
                "liquidation_price": p["liquidation_price"],
            })

    return json.dumps({
        "account_index": config["account_index"],
        "balance": acc["available_balance"],
        "collateral": acc["collateral"],
        "positions": positions,
        "total_positions": len(positions)
    }, indent=2)


def close_position_market(
    market_index: int,
    max_slippage_percent: float = 0.5,
) -> str:
    """Close an entire position at market price.

    Fetches the current position and places an opposite market order to close it.

    Args:
        market_index: Market ID (0=ETH, 1=BTC, 2=SOL, etc.)
        max_slippage_percent: Maximum slippage allowed (default 0.5%)

    Returns:
        JSON string with close result including final PnL
    """
    config = get_config()
    if not config:
        return json.dumps({"error": "Config not found"})

    # First, get current position
    import httpx
    url = f"{config['base_url']}/api/v1/account"
    params = {"by": "index", "value": str(config["account_index"])}

    with httpx.Client(timeout=30) as client:
        response = client.get(url, params=params)
        data = response.json()

    acc = data["accounts"][0]
    position = None
    for p in acc["positions"]:
        if p["market_id"] == market_index and float(p["position"]) != 0:
            position = p
            break

    if not position:
        return json.dumps({
            "success": False,
            "error": f"No open position found for market {market_index}"
        })

    size = float(position["position"])
    is_long = position["sign"] == 1
    entry_price = float(position["avg_entry_price"])
    unrealized_pnl = position["unrealized_pnl"]

    # Get current market price for slippage calculation
    url = f"{config['base_url']}/api/v1/orderBookDetails"
    with httpx.Client(timeout=30) as client:
        response = client.get(url, params={"market_id": market_index})
        market_data = response.json()

    current_price = market_data["order_book_details"][0]["last_trade_price"]

    # Calculate max execution price with slippage
    if is_long:
        # Closing long = SELL, want price not too low
        max_price = current_price * (1 - max_slippage_percent / 100)
    else:
        # Closing short = BUY, want price not too high
        max_price = current_price * (1 + max_slippage_percent / 100)

    async def _close():
        client = lighter.SignerClient(
            url=config["base_url"],
            account_index=config["account_index"],
            api_private_keys=config["private_keys"],
        )

        err = client.check_client()
        if err:
            return {"success": False, "error": str(err)}

        try:
            # Convert to Lighter format
            base_amount = int(abs(size) * 10000)  # 4 decimals
            avg_price = int(max_price * 100)  # 2 decimals

            tx, tx_hash, err = await client.create_market_order(
                market_index=market_index,
                client_order_index=999,  # Use 999 for close orders
                base_amount=base_amount,
                avg_execution_price=avg_price,
                is_ask=is_long,  # If LONG, we SELL (is_ask=True). If SHORT, we BUY (is_ask=False)
                reduce_only=True,  # Important: only reduce, don't flip position
            )

            if err:
                return {"success": False, "error": str(err)}

            return {
                "success": True,
                "tx_hash": str(tx_hash),
                "closed_position": {
                    "market": position["symbol"],
                    "side": "LONG" if is_long else "SHORT",
                    "size": position["position"],
                    "entry_price": entry_price,
                    "exit_price": f"~{current_price} (market)",
                    "unrealized_pnl_before_close": unrealized_pnl,
                }
            }
        finally:
            await client.close()

    result = _run_async(_close())
    return json.dumps(result, indent=2)


def close_position_limit(
    market_index: int,
    limit_price: float,
) -> str:
    """Close an entire position with a limit order at specified price.

    Args:
        market_index: Market ID (0=ETH, 1=BTC, 2=SOL, etc.)
        limit_price: The limit price to close at

    Returns:
        JSON string with order placement result
    """
    config = get_config()
    if not config:
        return json.dumps({"error": "Config not found"})

    # Get current position
    import httpx
    url = f"{config['base_url']}/api/v1/account"
    params = {"by": "index", "value": str(config["account_index"])}

    with httpx.Client(timeout=30) as client:
        response = client.get(url, params=params)
        data = response.json()

    acc = data["accounts"][0]
    position = None
    for p in acc["positions"]:
        if p["market_id"] == market_index and float(p["position"]) != 0:
            position = p
            break

    if not position:
        return json.dumps({
            "success": False,
            "error": f"No open position found for market {market_index}"
        })

    size = float(position["position"])
    is_long = position["sign"] == 1

    async def _close_limit():
        client = lighter.SignerClient(
            url=config["base_url"],
            account_index=config["account_index"],
            api_private_keys=config["private_keys"],
        )

        err = client.check_client()
        if err:
            return {"success": False, "error": str(err)}

        try:
            base_amount = int(abs(size) * 10000)
            price_amount = int(limit_price * 100)

            tx, tx_hash, err = await client.create_order(
                market_index=market_index,
                client_order_index=998,
                base_amount=base_amount,
                price=price_amount,
                is_ask=is_long,  # LONG -> SELL, SHORT -> BUY
                order_type=0,  # LIMIT
                time_in_force=1,  # GTC
                reduce_only=True,
            )

            if err:
                return {"success": False, "error": str(err)}

            return {
                "success": True,
                "tx_hash": str(tx_hash),
                "order": {
                    "market": position["symbol"],
                    "type": "LIMIT",
                    "side": "SELL" if is_long else "BUY",
                    "size": position["position"],
                    "limit_price": limit_price,
                    "reduce_only": True,
                }
            }
        finally:
            await client.close()

    result = _run_async(_close_limit())
    return json.dumps(result, indent=2)


def get_position_pnl(market_index: int) -> str:
    """Get detailed PnL information for a specific position.

    Args:
        market_index: Market ID

    Returns:
        JSON string with PnL details
    """
    config = get_config()
    if not config:
        return json.dumps({"error": "Config not found"})

    import httpx

    # Get position
    url = f"{config['base_url']}/api/v1/account"
    params = {"by": "index", "value": str(config["account_index"])}

    with httpx.Client(timeout=30) as client:
        response = client.get(url, params=params)
        data = response.json()

    acc = data["accounts"][0]
    position = None
    for p in acc["positions"]:
        if p["market_id"] == market_index:
            position = p
            break

    if not position or float(position["position"]) == 0:
        return json.dumps({
            "market_id": market_index,
            "has_position": False,
            "message": "No open position for this market"
        })

    # Get current market price
    url = f"{config['base_url']}/api/v1/orderBookDetails"
    with httpx.Client(timeout=30) as client:
        response = client.get(url, params={"market_id": market_index})
        market_data = response.json()

    current_price = market_data["order_book_details"][0]["last_trade_price"]
    entry_price = float(position["avg_entry_price"])
    size = float(position["position"])
    is_long = position["sign"] == 1

    # Calculate PnL percentage
    if is_long:
        pnl_percent = ((current_price - entry_price) / entry_price) * 100
    else:
        pnl_percent = ((entry_price - current_price) / entry_price) * 100

    return json.dumps({
        "market": position["symbol"],
        "market_id": market_index,
        "side": "LONG" if is_long else "SHORT",
        "size": position["position"],
        "entry_price": entry_price,
        "current_price": current_price,
        "position_value": position["position_value"],
        "unrealized_pnl": position["unrealized_pnl"],
        "unrealized_pnl_percent": f"{pnl_percent:.2f}%",
        "realized_pnl": position["realized_pnl"],
        "liquidation_price": position["liquidation_price"],
    }, indent=2)
