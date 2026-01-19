"""
Market-related tools for Lighter Exchange.

Provides 6 tools for market data and queries.
"""

import json
from typing import Optional, Literal
from lighter_agno.client import get_client


def get_markets(
    authorization: Optional[str] = None
) -> str:
    """Get information about all available trading markets on Lighter Exchange.

    Returns:
        JSON string with all markets and their details
    """
    client = get_client(authorization)
    # Use orderBookDetails as /markets is blocked by CloudFront
    result = client.get("/orderBookDetails", {})
    return json.dumps(result, indent=2)


def get_market(
    market_id: int,
    authorization: Optional[str] = None
) -> str:
    """Get detailed information about a specific market.

    Args:
        market_id: Market ID

    Returns:
        JSON string with market details
    """
    client = get_client(authorization)
    # Use orderBookDetails with market_id filter as /market is blocked
    result = client.get("/orderBookDetails", {"market_id": market_id})
    return json.dumps(result, indent=2)


def get_orderbook(
    market_id: int,
    limit: Optional[int] = None,
    authorization: Optional[str] = None
) -> str:
    """Get the order book (bids and asks) for a specific market.

    Args:
        market_id: Market ID
        limit: Number of price levels to return

    Returns:
        JSON string with orderbook bids and asks
    """
    client = get_client(authorization)
    result = client.get("/orderbook", {
        "market_id": market_id,
        "limit": limit,
    })
    return json.dumps(result, indent=2)


def get_orderbook_details(
    market_id: Optional[int] = None,
    filter: Optional[Literal["all", "spot", "perp"]] = None,
    authorization: Optional[str] = None
) -> str:
    """Get detailed metadata for order books.

    Includes:
    - Trading pair information
    - Fee structure (maker/taker/liquidation fees)
    - Margin requirements
    - Price decimals and size constraints
    - 24h volume and price statistics
    - Open interest

    Args:
        market_id: Market ID (255 for all markets)
        filter: Filter by market type (all, spot, perp)

    Returns:
        JSON string with orderbook details
    """
    client = get_client(authorization)
    result = client.get("/orderBookDetails", {
        "market_id": market_id,
        "filter": filter,
    })
    return json.dumps(result, indent=2)


def get_ticker(
    market_id: int,
    authorization: Optional[str] = None
) -> str:
    """Get current ticker data for a market.

    Returns last price, 24h volume, and price change.

    Args:
        market_id: Market ID

    Returns:
        JSON string with ticker data
    """
    client = get_client(authorization)
    # Use orderBookDetails as /ticker is blocked by CloudFront
    result = client.get("/orderBookDetails", {"market_id": market_id})
    return json.dumps(result, indent=2)


def get_asset_details(
    asset_index: Optional[int] = None,
    authorization: Optional[str] = None
) -> str:
    """Get details about supported assets.

    Includes:
    - Asset symbol and ID
    - Decimal precision
    - Minimum transfer/withdrawal amounts
    - Margin mode status
    - Current index price
    - L1 contract address

    Args:
        asset_index: Asset index (omit for all assets)

    Returns:
        JSON string with asset details
    """
    client = get_client(authorization)
    result = client.get("/assetDetails", {"asset_index": asset_index})
    return json.dumps(result, indent=2)
