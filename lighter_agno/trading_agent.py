"""
Lighter Exchange Trading Agent

Pure Agno agent with Lighter Exchange tools.
The agent automatically calls the right tools based on user messages.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Import all Lighter Exchange tools
from lighter_agno.tools.markets import (
    get_markets,
    get_market,
    get_orderbook,
    get_orderbook_details,
    get_ticker,
    get_asset_details,
)
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


# All 40 tools
ALL_LIGHTER_TOOLS = [
    # Market tools (6)
    get_markets,
    get_market,
    get_orderbook,
    get_orderbook_details,
    get_ticker,
    get_asset_details,
    # Account tools (11)
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
    # Order tools (5)
    get_orders,
    get_account_active_orders,
    get_account_inactive_orders,
    get_orderbook_orders,
    export_orders,
    # Trading tools (4)
    get_trades,
    get_recent_trades,
    get_candlesticks,
    get_funding_rates,
    # Transaction tools (3)
    get_next_nonce,
    send_transaction,
    send_transaction_batch,
    # API key tools (3)
    get_api_keys,
    create_api_key,
    delete_api_key,
    # Bridge tools (3)
    get_bridge_info,
    get_deposits,
    get_withdrawals,
    # Info tools (5)
    get_info,
    get_exchange_stats,
    get_announcements,
    get_notifications,
    get_referral_info,
]


# Agent instructions
INSTRUCTIONS = """You are a trading assistant for Lighter Exchange (zkSync).

You have 40 tools to interact with Lighter Exchange:

MARKET DATA:
- get_markets: List all markets
- get_ticker: Get price for a market (market_id required)
- get_orderbook: Get bids/asks (market_id required)
- get_candlesticks: Get OHLCV data (market_id, resolution required)
- get_funding_rates: Get funding rates (market_id required)

ACCOUNT:
- get_account: Get account details (by="index" or "l1_address", value required)
- get_positions: Get positions (param = account index or address)
- get_orders: Get orders (account_index, limit required)

TRADING:
- get_trades: Get trade history
- get_recent_trades: Get recent trades for a market

When user asks about prices, markets, or trading - call the appropriate tools.
Market IDs: 0=BTC-PERP, 1=ETH-PERP, etc. Use get_markets to see all.
"""


# Create the agent
lighter_agent = Agent(
    name="Lighter Trading Agent",
    model=OpenAIChat(id="gpt-5"),
    instructions=INSTRUCTIONS,
    tools=ALL_LIGHTER_TOOLS,
    markdown=True,
    show_tool_calls=True,
)


# Example usage
if __name__ == "__main__":
    # Simple chat
    lighter_agent.print_response("What markets are available on Lighter?", stream=True)

    print("\n" + "="*50 + "\n")

    lighter_agent.print_response("What's the current BTC price?", stream=True)
