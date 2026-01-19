"""
General info tools for Lighter Exchange.

Provides 5 tools for exchange information and notifications.
"""

import json
from typing import Optional
from lighter_agno.client import get_client


def get_info(
    authorization: Optional[str] = None
) -> str:
    """Get general exchange information including status, version, and system health.

    Returns:
        JSON string with exchange info
    """
    client = get_client(authorization)
    result = client.get("/info", {})
    return json.dumps(result, indent=2)


def get_exchange_stats(
    authorization: Optional[str] = None
) -> str:
    """Get exchange-wide statistics including total volume, number of users, and market metrics.

    Returns:
        JSON string with exchange statistics
    """
    client = get_client(authorization)
    result = client.get("/exchangeStats", {})
    return json.dumps(result, indent=2)


def get_announcements(
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
    authorization: Optional[str] = None
) -> str:
    """Get exchange announcements including maintenance notices, new features, and market updates.

    Args:
        cursor: Pagination cursor
        limit: Number of results

    Returns:
        JSON string with announcements
    """
    client = get_client(authorization)
    result = client.get("/announcements", {
        "cursor": cursor,
        "limit": limit,
    })
    return json.dumps(result, indent=2)


def get_notifications(
    account_index: int,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get account notifications including order fills, liquidation warnings, and system alerts.

    Args:
        account_index: Account index
        cursor: Pagination cursor
        limit: Number of results
        auth: Authentication token

    Returns:
        JSON string with notifications
    """
    client = get_client(authorization)
    result = client.get("/notifications", {
        "account_index": account_index,
        "cursor": cursor,
        "limit": limit,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def get_referral_info(
    account_index: int,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get referral program information for an account.

    Includes referral code, earnings, and referred users.

    Args:
        account_index: Account index
        auth: Authentication token

    Returns:
        JSON string with referral information
    """
    client = get_client(authorization)
    result = client.get("/referral", {
        "account_index": account_index,
        "auth": auth,
    })
    return json.dumps(result, indent=2)
