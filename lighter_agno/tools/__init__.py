"""
Lighter Exchange Tools for Agno

This module exports all 40 tools organized by category.
"""

from lighter_agno.tools.account import (
    get_account,
    get_accounts_by_l1_address,
    get_account_limits,
    get_account_metadata,
    get_pnl,
    get_l1_metadata,
    change_account_tier,
    get_liquidations,
    get_position_funding,
    get_public_pools_metadata,
    get_positions,
)

from lighter_agno.tools.orders import (
    get_orders,
    get_account_active_orders,
    get_account_inactive_orders,
    get_orderbook_orders,
    export_orders,
)

from lighter_agno.tools.markets import (
    get_markets,
    get_market,
    get_orderbook,
    get_orderbook_details,
    get_ticker,
    get_asset_details,
)

from lighter_agno.tools.trading import (
    get_trades,
    get_recent_trades,
    get_candlesticks,
    get_funding_rates,
)

from lighter_agno.tools.transactions import (
    get_next_nonce,
    send_transaction,
    send_transaction_batch,
)

from lighter_agno.tools.apikeys import (
    get_api_keys,
    create_api_key,
    delete_api_key,
)

from lighter_agno.tools.bridge import (
    get_bridge_info,
    get_deposits,
    get_withdrawals,
)

from lighter_agno.tools.info import (
    get_info,
    get_exchange_stats,
    get_announcements,
    get_notifications,
    get_referral_info,
)

# All tools organized by category
ACCOUNT_TOOLS = [
    get_account,
    get_accounts_by_l1_address,
    get_account_limits,
    get_account_metadata,
    get_pnl,
    get_l1_metadata,
    change_account_tier,
    get_liquidations,
    get_position_funding,
    get_public_pools_metadata,
    get_positions,
]

ORDER_TOOLS = [
    get_orders,
    get_account_active_orders,
    get_account_inactive_orders,
    get_orderbook_orders,
    export_orders,
]

MARKET_TOOLS = [
    get_markets,
    get_market,
    get_orderbook,
    get_orderbook_details,
    get_ticker,
    get_asset_details,
]

TRADING_TOOLS = [
    get_trades,
    get_recent_trades,
    get_candlesticks,
    get_funding_rates,
]

TRANSACTION_TOOLS = [
    get_next_nonce,
    send_transaction,
    send_transaction_batch,
]

API_KEY_TOOLS = [
    get_api_keys,
    create_api_key,
    delete_api_key,
]

BRIDGE_TOOLS = [
    get_bridge_info,
    get_deposits,
    get_withdrawals,
]

INFO_TOOLS = [
    get_info,
    get_exchange_stats,
    get_announcements,
    get_notifications,
    get_referral_info,
]

# All tools combined (40 total)
ALL_TOOLS = (
    ACCOUNT_TOOLS +
    ORDER_TOOLS +
    MARKET_TOOLS +
    TRADING_TOOLS +
    TRANSACTION_TOOLS +
    API_KEY_TOOLS +
    BRIDGE_TOOLS +
    INFO_TOOLS
)

__all__ = [
    # Account tools
    "get_account",
    "get_accounts_by_l1_address",
    "get_account_limits",
    "get_account_metadata",
    "get_pnl",
    "get_l1_metadata",
    "change_account_tier",
    "get_liquidations",
    "get_position_funding",
    "get_public_pools_metadata",
    "get_positions",
    # Order tools
    "get_orders",
    "get_account_active_orders",
    "get_account_inactive_orders",
    "get_orderbook_orders",
    "export_orders",
    # Market tools
    "get_markets",
    "get_market",
    "get_orderbook",
    "get_orderbook_details",
    "get_ticker",
    "get_asset_details",
    # Trading tools
    "get_trades",
    "get_recent_trades",
    "get_candlesticks",
    "get_funding_rates",
    # Transaction tools
    "get_next_nonce",
    "send_transaction",
    "send_transaction_batch",
    # API key tools
    "get_api_keys",
    "create_api_key",
    "delete_api_key",
    # Bridge tools
    "get_bridge_info",
    "get_deposits",
    "get_withdrawals",
    # Info tools
    "get_info",
    "get_exchange_stats",
    "get_announcements",
    "get_notifications",
    "get_referral_info",
    # Tool lists
    "ACCOUNT_TOOLS",
    "ORDER_TOOLS",
    "MARKET_TOOLS",
    "TRADING_TOOLS",
    "TRANSACTION_TOOLS",
    "API_KEY_TOOLS",
    "BRIDGE_TOOLS",
    "INFO_TOOLS",
    "ALL_TOOLS",
]
