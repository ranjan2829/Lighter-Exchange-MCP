"""
Account-related tools for Lighter Exchange.

Provides 11 tools for account management and queries.
"""

import json
from typing import Optional, Literal
from lighter_agno.client import get_client


def get_account(
    by: Literal["index", "l1_address"],
    value: str,
    authorization: Optional[str] = None
) -> str:
    """Get account details by account index or L1 address.

    Returns comprehensive account information including:
    - Account status (1 = active, 0 = inactive)
    - Collateral and available balance
    - Position details for each market
    - Asset balances (USDC, ETH, etc.)

    Position fields explained:
    - OOC: Open order count in that market
    - Sign: 1 for Long, -1 for Short
    - Position: Amount of position held
    - Avg Entry Price: Average entry price
    - Unrealized/Realized PnL: Profit and loss

    Args:
        by: Query type - 'index' for account index, 'l1_address' for Ethereum address
        value: The account index number or L1 Ethereum address

    Returns:
        JSON string with account details
    """
    client = get_client(authorization)
    result = client.get("/account", {"by": by, "value": value})
    return json.dumps(result, indent=2)


def get_accounts_by_l1_address(
    l1_address: str,
    authorization: Optional[str] = None
) -> str:
    """Get all accounts (main and sub-accounts) associated with an L1 Ethereum address.

    Args:
        l1_address: The L1 Ethereum address (0x...)

    Returns:
        JSON string with list of accounts
    """
    client = get_client(authorization)
    result = client.get("/accountsByL1Address", {"l1_address": l1_address})
    return json.dumps(result, indent=2)


def get_account_limits(
    by: Literal["index", "l1_address"],
    value: str,
    authorization: Optional[str] = None
) -> str:
    """Get trading limits and restrictions for an account.

    Returns position limits, leverage limits, and order size constraints.

    Args:
        by: Query type - 'index' for account index, 'l1_address' for Ethereum address
        value: Account index or L1 address

    Returns:
        JSON string with account limits
    """
    client = get_client(authorization)
    result = client.get("/accountLimits", {"by": by, "value": value})
    return json.dumps(result, indent=2)


def get_account_metadata(
    by: Literal["index", "l1_address"],
    value: str,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get account metadata including name, description, and configuration settings.

    Args:
        by: Query type - 'index' for account index, 'l1_address' for Ethereum address
        value: Account index or L1 address
        auth: Authentication token (required for private data)

    Returns:
        JSON string with account metadata
    """
    client = get_client(authorization)
    result = client.get("/accountMetadata", {"by": by, "value": value, "auth": auth})
    return json.dumps(result, indent=2)


def get_pnl(
    by: Literal["index"],
    value: str,
    resolution: Literal["1m", "5m", "15m", "1h", "4h", "1d"],
    start_timestamp: int,
    end_timestamp: int,
    count_back: int,
    ignore_transfers: Optional[bool] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get account PnL (Profit and Loss) chart data over time.

    Supports multiple time resolutions for different analysis needs:
    - 1m, 5m, 15m: Short-term trading analysis
    - 1h, 4h: Medium-term trends
    - 1d: Long-term performance

    Args:
        by: Query type (currently only 'index' supported)
        value: Account index
        resolution: Time resolution for PnL data points (1m, 5m, 15m, 1h, 4h, 1d)
        start_timestamp: Start timestamp in milliseconds
        end_timestamp: End timestamp in milliseconds
        count_back: Number of data points to return
        ignore_transfers: Exclude deposit/withdrawal effects from PnL calculation
        auth: Authentication token

    Returns:
        JSON string with PnL data points
    """
    client = get_client(authorization)
    result = client.get("/pnl", {
        "by": by,
        "value": value,
        "resolution": resolution,
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "count_back": count_back,
        "ignore_transfers": ignore_transfers,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_l1_metadata(
    by: Literal["index", "l1_address"],
    value: str,
    authorization: Optional[str] = None
) -> str:
    """Get L1 blockchain metadata for an account including on-chain registration details.

    Args:
        by: Query type - 'index' for account index, 'l1_address' for Ethereum address
        value: Account index or L1 address

    Returns:
        JSON string with L1 metadata
    """
    client = get_client(authorization)
    result = client.get("/l1Metadata", {"by": by, "value": value})
    return json.dumps(result, indent=2)


def change_account_tier(
    account_index: int,
    tier: str,
    auth: str,
    authorization: Optional[str] = None
) -> str:
    """Change account tier between Standard and Premium.

    - Standard: Fee-free trading
    - Premium: 0.2 bps maker / 2 bps taker fees

    Requires authentication.

    Args:
        account_index: Account index to modify
        tier: New tier to set
        auth: Authentication token (required)

    Returns:
        JSON string with result
    """
    client = get_client(authorization)
    result = client.post("/changeAccountTier", {
        "account_index": account_index,
        "tier": tier,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_liquidations(
    account_index: int,
    limit: int,
    cursor: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get liquidation events history for an account.

    Args:
        account_index: Account index
        limit: Number of results (1-100)
        cursor: Pagination cursor for next page

    Returns:
        JSON string with liquidation history
    """
    client = get_client(authorization)
    result = client.get("/liquidations", {
        "account_index": account_index,
        "cursor": cursor,
        "limit": limit,
    })
    return json.dumps(result, indent=2)


def get_position_funding(
    account_index: int,
    limit: int,
    market_id: Optional[int] = None,
    cursor: Optional[str] = None,
    side: Optional[Literal["long", "short", "all"]] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get funding payment history for positions.

    Auth is required for accounts linked to main/sub-accounts,
    but can be omitted for public pools.

    Args:
        account_index: Account index
        limit: Number of results (1-100)
        market_id: Filter by market ID (255 for all markets)
        cursor: Pagination cursor
        side: Filter by position side (long, short, all)
        auth: Authentication token

    Returns:
        JSON string with funding payment history
    """
    client = get_client(authorization)
    result = client.get("/positionFunding", {
        "account_index": account_index,
        "market_id": market_id,
        "cursor": cursor,
        "limit": limit,
        "side": side,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_public_pools_metadata(
    authorization: Optional[str] = None
) -> str:
    """Get metadata for all public liquidity pools.

    Returns:
        JSON string with public pools information
    """
    client = get_client(authorization)
    result = client.get("/publicPoolsMetadata", {})
    return json.dumps(result, indent=2)


def get_positions(
    param: str,
    authorization: Optional[str] = None
) -> str:
    """Get all open positions for an account using the Explorer API.

    Args:
        param: L1 address or account index

    Returns:
        JSON string with open positions
    """
    client = get_client(authorization)
    result = client.get_explorer(f"/accounts/{param}/positions")
    return json.dumps(result, indent=2)
