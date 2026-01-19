"""
Bridge (deposits/withdrawals) tools for Lighter Exchange.

Provides 3 tools for managing deposits and withdrawals.
"""

import json
from typing import Optional
from lighter_agno.client import get_client


def get_bridge_info(
    account_index: Optional[int] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get bridge information including supported assets, minimum amounts, and deposit/withdrawal instructions.

    Args:
        account_index: Account index (optional)
        auth: Authentication token

    Returns:
        JSON string with bridge information
    """
    client = get_client(authorization)
    result = client.get("/bridge", {
        "account_index": account_index,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_deposits(
    account_index: int,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get deposit history for an account including pending and completed deposits.

    Args:
        account_index: Account index
        cursor: Pagination cursor
        limit: Number of results
        auth: Authentication token

    Returns:
        JSON string with deposit history
    """
    client = get_client(authorization)
    result = client.get("/deposits", {
        "account_index": account_index,
        "cursor": cursor,
        "limit": limit,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_withdrawals(
    account_index: int,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get withdrawal history for an account including pending and completed withdrawals.

    Args:
        account_index: Account index
        cursor: Pagination cursor
        limit: Number of results
        auth: Authentication token

    Returns:
        JSON string with withdrawal history
    """
    client = get_client(authorization)
    result = client.get("/withdrawals", {
        "account_index": account_index,
        "cursor": cursor,
        "limit": limit,
        "auth": auth,
    })
    return json.dumps(result, indent=2)
