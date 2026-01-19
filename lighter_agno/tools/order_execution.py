"""
Order execution tools using official Lighter SDK.

These tools can actually place, modify, and cancel orders.
"""

import os
import json
import asyncio
from typing import Optional, Literal
import lighter

# Load config from environment or file
def get_config():
    """Get Lighter configuration from environment or config file."""
    config_file = os.path.join(os.path.dirname(__file__), "..", "api_key_config.json")

    if os.path.exists(config_file):
        with open(config_file) as f:
            cfg = json.load(f)
        return {
            "base_url": cfg["baseUrl"],
            "account_index": cfg["accountIndex"],
            "private_keys": {int(k): v for k, v in cfg["privateKeys"].items()}
        }

    # Fallback to environment variables
    return {
        "base_url": os.getenv("LIGHTER_BASE_URL", "https://mainnet.zklighter.elliot.ai"),
        "account_index": int(os.getenv("LIGHTER_ACCOUNT_INDEX", 0)),
        "private_keys": {
            int(os.getenv("LIGHTER_API_KEY_INDEX", 0)): os.getenv("LIGHTER_PRIVATE_KEY", "")
        }
    }


def _run_async(coro):
    """Run async coroutine synchronously."""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If we're already in an async context, create a new loop
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, coro)
                return future.result()
        return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)


async def _create_client():
    """Create and verify Lighter SignerClient."""
    config = get_config()
    client = lighter.SignerClient(
        url=config["base_url"],
        account_index=config["account_index"],
        api_private_keys=config["private_keys"],
    )
    err = client.check_client()
    if err:
        raise Exception(f"Client error: {err}")
    return client, config["account_index"]


def place_limit_order(
    market_index: int,
    side: Literal["buy", "sell"],
    size: float,
    price: float,
    client_order_id: int = 1,
    reduce_only: bool = False,
) -> str:
    """Place a limit order on Lighter Exchange.

    Args:
        market_index: Market ID (0=ETH-PERP, 1=BTC-PERP, 2=SOL-PERP, etc.)
        side: 'buy' or 'sell'
        size: Order size in base asset (e.g., 0.1 for 0.1 ETH)
        price: Limit price in USD
        client_order_id: Your custom order ID (default 1)
        reduce_only: If True, only reduces existing position

    Returns:
        JSON string with order result
    """
    async def _place():
        client, account_index = await _create_client()
        try:
            # Convert to Lighter format
            # Size decimals vary by market, typically 4 (so 0.1 = 1000)
            base_amount = int(size * 10000)
            price_amount = int(price * 100)  # 2 decimal places

            tx, tx_hash, err = await client.create_order(
                market_index=market_index,
                client_order_index=client_order_id,
                base_amount=base_amount,
                price=price_amount,
                is_ask=(side == "sell"),
                order_type=0,  # LIMIT
                time_in_force=1,  # GTC
                reduce_only=reduce_only,
            )

            if err:
                return {"success": False, "error": str(err)}
            return {
                "success": True,
                "tx_hash": tx_hash,
                "order": {
                    "market_index": market_index,
                    "side": side,
                    "size": size,
                    "price": price,
                    "client_order_id": client_order_id
                }
            }
        finally:
            await client.close()

    result = _run_async(_place())
    return json.dumps(result, indent=2)


def place_market_order(
    market_index: int,
    side: Literal["buy", "sell"],
    size: float,
    max_slippage_price: float,
    client_order_id: int = 1,
    reduce_only: bool = False,
) -> str:
    """Place a market order on Lighter Exchange.

    Args:
        market_index: Market ID (0=ETH-PERP, 1=BTC-PERP, etc.)
        side: 'buy' or 'sell'
        size: Order size in base asset
        max_slippage_price: Maximum acceptable execution price (for slippage protection)
        client_order_id: Your custom order ID
        reduce_only: If True, only reduces existing position

    Returns:
        JSON string with order result
    """
    async def _place():
        client, _ = await _create_client()
        try:
            base_amount = int(size * 10000)
            avg_price = int(max_slippage_price * 100)

            tx, tx_hash, err = await client.create_market_order(
                market_index=market_index,
                client_order_index=client_order_id,
                base_amount=base_amount,
                avg_execution_price=avg_price,
                is_ask=(side == "sell"),
                reduce_only=reduce_only,
            )

            if err:
                return {"success": False, "error": str(err)}
            return {
                "success": True,
                "tx_hash": tx_hash,
                "order": {
                    "market_index": market_index,
                    "side": side,
                    "size": size,
                    "type": "market"
                }
            }
        finally:
            await client.close()

    result = _run_async(_place())
    return json.dumps(result, indent=2)


def cancel_order(
    market_index: int,
    order_id: int,
) -> str:
    """Cancel an existing order.

    Args:
        market_index: Market ID
        order_id: The order ID to cancel

    Returns:
        JSON string with cancellation result
    """
    async def _cancel():
        client, _ = await _create_client()
        try:
            tx, tx_hash, err = await client.cancel_order(
                market_index=market_index,
                order_index=order_id,
            )

            if err:
                return {"success": False, "error": str(err)}
            return {
                "success": True,
                "tx_hash": tx_hash,
                "cancelled_order_id": order_id
            }
        finally:
            await client.close()

    result = _run_async(_cancel())
    return json.dumps(result, indent=2)


def cancel_all_orders(
    market_index: Optional[int] = None,
) -> str:
    """Cancel all open orders, optionally for a specific market.

    Args:
        market_index: Market ID (None for all markets)

    Returns:
        JSON string with cancellation result
    """
    async def _cancel_all():
        client, _ = await _create_client()
        try:
            tx, tx_hash, err = await client.cancel_all_orders(
                market_index=market_index if market_index is not None else 255,
            )

            if err:
                return {"success": False, "error": str(err)}
            return {
                "success": True,
                "tx_hash": tx_hash,
                "market_index": market_index
            }
        finally:
            await client.close()

    result = _run_async(_cancel_all())
    return json.dumps(result, indent=2)


def get_account_status() -> str:
    """Get current account status including balance and positions.

    Returns:
        JSON string with account information
    """
    config = get_config()
    api_client = lighter.ApiClient(
        configuration=lighter.Configuration(host=config["base_url"] + "/api/v1")
    )
    account_api = lighter.AccountApi(api_client)

    try:
        account = account_api.get_account(by="index", value=str(config["account_index"]))
        acc = account.accounts[0]

        return json.dumps({
            "account_index": acc.account_index,
            "balance": acc.available_balance,
            "collateral": acc.collateral,
            "positions": [
                {
                    "market": p.symbol,
                    "market_id": p.market_id,
                    "side": "long" if p.sign == 1 else "short",
                    "size": p.position,
                    "entry_price": p.avg_entry_price,
                    "unrealized_pnl": p.unrealized_pnl,
                }
                for p in acc.positions if float(p.position) != 0
            ]
        }, indent=2)
    finally:
        api_client.close()
