"""
Lighter Exchange Toolkit for Agno

Provides a complete toolkit with all 40 tools for Lighter Exchange integration.
"""

from typing import Optional, List, Callable

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


class LighterExchangeTools:
    """
    Agno-compatible toolkit for Lighter Exchange.

    Provides 40 tools organized into 8 categories:
    - Account (11 tools): Account management and queries
    - Orders (5 tools): Order management
    - Markets (6 tools): Market data
    - Trading (4 tools): Trade history and candlesticks
    - Transactions (3 tools): Transaction signing and submission
    - API Keys (3 tools): API key management
    - Bridge (3 tools): Deposits and withdrawals
    - Info (5 tools): Exchange information

    Usage with Agno:
        from agno.agent import Agent
        from lighter_agno import LighterExchangeTools

        agent = Agent(
            tools=[LighterExchangeTools()],
            markdown=True
        )
    """

    def __init__(
        self,
        include_account: bool = True,
        include_orders: bool = True,
        include_markets: bool = True,
        include_trading: bool = True,
        include_transactions: bool = True,
        include_apikeys: bool = True,
        include_bridge: bool = True,
        include_info: bool = True,
    ):
        """
        Initialize the toolkit with optional category filtering.

        Args:
            include_account: Include account management tools
            include_orders: Include order management tools
            include_markets: Include market data tools
            include_trading: Include trading history tools
            include_transactions: Include transaction tools
            include_apikeys: Include API key management tools
            include_bridge: Include bridge (deposit/withdrawal) tools
            include_info: Include exchange info tools
        """
        self._tools: List[Callable] = []

        if include_account:
            self._tools.extend([
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
            ])

        if include_orders:
            self._tools.extend([
                get_orders,
                get_account_active_orders,
                get_account_inactive_orders,
                get_orderbook_orders,
                export_orders,
            ])

        if include_markets:
            self._tools.extend([
                get_markets,
                get_market,
                get_orderbook,
                get_orderbook_details,
                get_ticker,
                get_asset_details,
            ])

        if include_trading:
            self._tools.extend([
                get_trades,
                get_recent_trades,
                get_candlesticks,
                get_funding_rates,
            ])

        if include_transactions:
            self._tools.extend([
                get_next_nonce,
                send_transaction,
                send_transaction_batch,
            ])

        if include_apikeys:
            self._tools.extend([
                get_api_keys,
                create_api_key,
                delete_api_key,
            ])

        if include_bridge:
            self._tools.extend([
                get_bridge_info,
                get_deposits,
                get_withdrawals,
            ])

        if include_info:
            self._tools.extend([
                get_info,
                get_exchange_stats,
                get_announcements,
                get_notifications,
                get_referral_info,
            ])

    def __iter__(self):
        """Allow iteration over tools for Agno compatibility."""
        return iter(self._tools)

    def __len__(self):
        """Return number of tools."""
        return len(self._tools)

    @property
    def tools(self) -> List[Callable]:
        """Get list of all tools."""
        return self._tools

    def get_tool_names(self) -> List[str]:
        """Get list of all tool function names."""
        return [tool.__name__ for tool in self._tools]


# Convenience function to get all tools as a flat list
def get_all_tools() -> List[Callable]:
    """
    Get all 40 Lighter Exchange tools as a flat list.

    This can be used directly with Agno:
        from agno.agent import Agent
        from lighter_agno.toolkit import get_all_tools

        agent = Agent(tools=get_all_tools())

    Returns:
        List of all 40 tool functions
    """
    return LighterExchangeTools().tools


# Category-specific tool getters
def get_account_tools() -> List[Callable]:
    """Get only account management tools (11 tools)."""
    return LighterExchangeTools(
        include_orders=False,
        include_markets=False,
        include_trading=False,
        include_transactions=False,
        include_apikeys=False,
        include_bridge=False,
        include_info=False,
    ).tools


def get_order_tools() -> List[Callable]:
    """Get only order management tools (5 tools)."""
    return LighterExchangeTools(
        include_account=False,
        include_markets=False,
        include_trading=False,
        include_transactions=False,
        include_apikeys=False,
        include_bridge=False,
        include_info=False,
    ).tools


def get_market_tools() -> List[Callable]:
    """Get only market data tools (6 tools)."""
    return LighterExchangeTools(
        include_account=False,
        include_orders=False,
        include_trading=False,
        include_transactions=False,
        include_apikeys=False,
        include_bridge=False,
        include_info=False,
    ).tools


def get_trading_tools() -> List[Callable]:
    """Get only trading history tools (4 tools)."""
    return LighterExchangeTools(
        include_account=False,
        include_orders=False,
        include_markets=False,
        include_transactions=False,
        include_apikeys=False,
        include_bridge=False,
        include_info=False,
    ).tools


def get_transaction_tools() -> List[Callable]:
    """Get only transaction tools (3 tools)."""
    return LighterExchangeTools(
        include_account=False,
        include_orders=False,
        include_markets=False,
        include_trading=False,
        include_apikeys=False,
        include_bridge=False,
        include_info=False,
    ).tools


def get_apikey_tools() -> List[Callable]:
    """Get only API key management tools (3 tools)."""
    return LighterExchangeTools(
        include_account=False,
        include_orders=False,
        include_markets=False,
        include_trading=False,
        include_transactions=False,
        include_bridge=False,
        include_info=False,
    ).tools


def get_bridge_tools() -> List[Callable]:
    """Get only bridge (deposit/withdrawal) tools (3 tools)."""
    return LighterExchangeTools(
        include_account=False,
        include_orders=False,
        include_markets=False,
        include_trading=False,
        include_transactions=False,
        include_apikeys=False,
        include_info=False,
    ).tools


def get_info_tools() -> List[Callable]:
    """Get only exchange info tools (5 tools)."""
    return LighterExchangeTools(
        include_account=False,
        include_orders=False,
        include_markets=False,
        include_trading=False,
        include_transactions=False,
        include_apikeys=False,
        include_bridge=False,
    ).tools
