"""
Order-related tools for Lighter Exchange.

Provides 5 tools for order management and queries.
"""

import json
from typing import Optional, Literal
from lighter_agno.client import get_client


def get_orders(
    account_index: int,
    limit: int,
    market_id: Optional[int] = None,
    status: Optional[Literal["open", "filled", "cancelled", "all"]] = None,
    cursor: Optional[str] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get orders for an account with optional filtering by market and status.

    Args:
        account_index: Account index
        limit: Number of results (1-100)
        market_id: Filter by market ID
        status: Filter by order status (open, filled, cancelled, all)
        cursor: Pagination cursor
        auth: Authentication token

    Returns:
        JSON string with orders list
    """
    client = get_client(authorization)
    result = client.get("/orders", {
        "account_index": account_index,
        "market_id": market_id,
        "status": status,
        "cursor": cursor,
        "limit": limit,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_account_active_orders(
    account_index: int,
    limit: int,
    market_id: Optional[int] = None,
    cursor: Optional[str] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get all active (open) orders for an account.

    Args:
        account_index: Account index
        limit: Number of results (1-100)
        market_id: Filter by market ID
        cursor: Pagination cursor
        auth: Authentication token

    Returns:
        JSON string with active orders
    """
    client = get_client(authorization)
    result = client.get("/accountActiveOrders", {
        "account_index": account_index,
        "market_id": market_id,
        "cursor": cursor,
        "limit": limit,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_account_inactive_orders(
    account_index: int,
    limit: int,
    market_id: Optional[int] = None,
    cursor: Optional[str] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get inactive (filled/cancelled) orders history for an account.

    Args:
        account_index: Account index
        limit: Number of results (1-100)
        market_id: Filter by market ID
        cursor: Pagination cursor
        auth: Authentication token

    Returns:
        JSON string with inactive orders
    """
    client = get_client(authorization)
    result = client.get("/accountInactiveOrders", {
        "account_index": account_index,
        "market_id": market_id,
        "cursor": cursor,
        "limit": limit,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_orderbook_orders(
    market_id: int,
    side: Optional[Literal["buy", "sell", "all"]] = None,
    limit: Optional[int] = None,
    authorization: Optional[str] = None
) -> str:
    """Get orders directly from the order book for a specific market.

    Args:
        market_id: Market ID
        side: Filter by order side (buy, sell, all)
        limit: Number of orders to return

    Returns:
        JSON string with orderbook orders
    """
    client = get_client(authorization)
    result = client.get("/orderBookOrders", {
        "market_id": market_id,
        "side": side,
        "limit": limit,
    })
    return json.dumps(result, indent=2)


def export_orders(
    account_index: int,
    market_id: Optional[int] = None,
    start_timestamp: Optional[int] = None,
    end_timestamp: Optional[int] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Export order data for an account within a time range.

    Useful for record keeping and analysis.

    Args:
        account_index: Account index
        market_id: Filter by market ID
        start_timestamp: Start timestamp in milliseconds
        end_timestamp: End timestamp in milliseconds
        auth: Authentication token

    Returns:
        JSON string with exported order data
    """
    client = get_client(authorization)
    result = client.get("/export", {
        "account_index": account_index,
        "market_id": market_id,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "auth": auth,
    })
    return json.dumps(result, indent=2)
