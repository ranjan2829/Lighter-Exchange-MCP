"""
Trading-related tools for Lighter Exchange.

Provides 4 tools for trade history and market data.
"""

import json
from typing import Optional, Literal
from lighter_agno.client import get_client


def get_trades(
    limit: int,
    account_index: Optional[int] = None,
    market_id: Optional[int] = None,
    cursor: Optional[str] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get trade history for an account or market.

    Args:
        limit: Number of results (1-100)
        account_index: Filter by account index
        market_id: Filter by market ID
        cursor: Pagination cursor
        auth: Authentication token

    Returns:
        JSON string with trade history
    """
    client = get_client(authorization)
    result = client.get("/trades", {
        "account_index": account_index,
        "market_id": market_id,
        "cursor": cursor,
        "limit": limit,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_recent_trades(
    market_id: int,
    limit: Optional[int] = None,
    authorization: Optional[str] = None
) -> str:
    """Get the most recent trades for a market.

    Args:
        market_id: Market ID
        limit: Number of trades to return

    Returns:
        JSON string with recent trades
    """
    client = get_client(authorization)
    result = client.get("/recentTrades", {
        "market_id": market_id,
        "limit": limit,
    })
    return json.dumps(result, indent=2)


def get_candlesticks(
    market_id: int,
    resolution: Literal["1m", "5m", "15m", "1h", "4h", "1d"],
    start_timestamp: Optional[int] = None,
    end_timestamp: Optional[int] = None,
    count_back: Optional[int] = None,
    authorization: Optional[str] = None
) -> str:
    """Get OHLCV (Open, High, Low, Close, Volume) candlestick data for charting.

    Supported resolutions:
    - 1m, 5m, 15m: Intraday analysis
    - 1h, 4h: Swing trading
    - 1d: Daily charts

    Args:
        market_id: Market ID
        resolution: Candlestick time resolution (1m, 5m, 15m, 1h, 4h, 1d)
        start_timestamp: Start timestamp in milliseconds
        end_timestamp: End timestamp in milliseconds
        count_back: Number of candles to return

    Returns:
        JSON string with candlestick data
    """
    client = get_client(authorization)
    result = client.get("/candlestick", {
        "market_id": market_id,
        "resolution": resolution,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "count_back": count_back,
    })
    return json.dumps(result, indent=2)


def get_funding_rates(
    market_id: int,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
    authorization: Optional[str] = None
) -> str:
    """Get funding rate history for perpetual markets.

    Funding rates are periodic payments between long and short positions.

    Args:
        market_id: Market ID
        cursor: Pagination cursor
        limit: Number of results

    Returns:
        JSON string with funding rate history
    """
    client = get_client(authorization)
    result = client.get("/funding", {
        "market_id": market_id,
        "cursor": cursor,
        "limit": limit,
    })
    return json.dumps(result, indent=2)
