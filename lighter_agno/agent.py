from typing import Optional

from lighter_agno.toolkit import LighterExchangeTools

try:
    from agno.agent import Agent
    AGNO_AVAILABLE = True
except ImportError:
    AGNO_AVAILABLE = False
    Agent = None


TRADING_AGENT_INSTRUCTIONS = """You are an elite trading assistant for Lighter Exchange - \
a high-performance zkSync DEX.

🛠️ YOUR ARSENAL (40+ TOOLS):
• Markets: get_ticker, get_orderbook, get_markets, get_asset_details
• Trading: get_trades, get_candlesticks, get_funding_rates
• Account: get_account, get_positions, get_pnl, get_liquidations
• Orders: get_orders, get_account_active_orders, export_orders
• Bridge: get_deposits, get_withdrawals, get_bridge_info
• API: create_api_key, manage keys
• Transactions: send_transaction (when enabled)

⚡ EXECUTION PROTOCOL:
1. Check market conditions FIRST (get_ticker/orderbook)
2. Verify account state before advice (positions, PnL, limits)
3. Warn about leverage risks explicitly
4. Confirm transaction details before execution
5. Use tables for data visualization

Master these tools. Trade smart. Stay profitable."""

MARKET_ANALYSIS_INSTRUCTIONS = """You are a market intelligence specialist for Lighter Exchange.

🎯 FOCUS: Pure data-driven analysis using:
• Real-time: get_ticker, get_orderbook, get_markets
• Historical: get_candlesticks, get_trades, get_funding_rates
• Deep-dive: get_orderbook_details, get_asset_details

📊 DELIVER: Sharp insights, pattern recognition, comparative analysis.
🚫 AVOID: Price predictions, financial advice.
✅ ALWAYS: Cite specific data sources."""

ACCOUNT_MONITOR_INSTRUCTIONS = """You are an account guardian for Lighter Exchange.

🔍 MONITOR USING:
• Portfolio: get_account, get_positions, get_pnl
• Risk: get_liquidations, get_account_limits
• Activity: get_orders, get_deposits, get_withdrawals
• Funding: get_position_funding

⚠️ ALERT ON: Liquidation risks, unusual PnL movements, limit breaches.
📋 REPORT: Clear status summaries with actionable insights."""


def create_trading_agent(
    model: str = "gpt-4o",
    include_transactions: bool = False,
    **kwargs
) -> Optional["Agent"]:
    """Create full-featured trading agent with all tools."""
    if not AGNO_AVAILABLE:
        raise ImportError("Install agno: pip install agno")

    tools = LighterExchangeTools(include_transactions=include_transactions)
    return Agent(
        model=model,
        instructions=TRADING_AGENT_INSTRUCTIONS,
        tools=list(tools),
        markdown=True,
        **kwargs
    )


def create_market_agent(model: str = "gpt-4o", **kwargs) -> Optional["Agent"]:
    """Create market analysis agent (read-only)."""
    if not AGNO_AVAILABLE:
        raise ImportError("Install agno: pip install agno")

    tools = LighterExchangeTools(
        include_account=False,
        include_orders=False,
        include_transactions=False,
        include_apikeys=False,
        include_bridge=False,
    )
    return Agent(
        model=model,
        instructions=MARKET_ANALYSIS_INSTRUCTIONS,
        tools=list(tools),
        markdown=True,
        **kwargs
    )


def create_account_agent(model: str = "gpt-4o", **kwargs) -> Optional["Agent"]:
    """Create account monitoring agent."""
    if not AGNO_AVAILABLE:
        raise ImportError("Install agno: pip install agno")

    tools = LighterExchangeTools(
        include_markets=False,
        include_trading=False,
        include_transactions=False,
        include_apikeys=False,
        include_info=True,
    )
    return Agent(
        model=model,
        instructions=ACCOUNT_MONITOR_INSTRUCTIONS,
        tools=list(tools),
        markdown=True,
        **kwargs
    )


if __name__ == "__main__":
    try:
        agent = create_trading_agent()
        print(f"✅ Trading agent created with {len(LighterExchangeTools())} tools")
        print("Usage: agent.print_response('What markets are available?', stream=True)")
    except ImportError as e:
        print(f"❌ {e}")
