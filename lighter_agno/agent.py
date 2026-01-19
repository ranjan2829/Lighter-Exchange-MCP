from typing import Optional

try:
    from agno.agent import Agent
    AGNO_AVAILABLE = True
except ImportError:
    AGNO_AVAILABLE = False
    Agent = None

from lighter_agno.toolkit import (
    LighterExchangeTools,
    get_all_tools,
    get_market_tools,
    get_account_tools,
)


TRADING_AGENT_INSTRUCTIONS = """You are a professional trading assistant for Lighter Exchange,
a high-performance perpetual and spot trading platform on zkSync.

Your capabilities include:
- Checking market prices, orderbooks, and trading volumes
- Viewing account balances, positions, and PnL
- Analyzing trade history and funding rates
- Providing market insights based on candlestick data

When users ask about trading:
1. Always check current market conditions first using get_ticker or get_orderbook
2. For account queries, use the appropriate account tools
3. Provide clear, actionable information
4. Warn users about risks when discussing leveraged positions

For placing orders (if transaction tools are enabled):
1. Always confirm order details before submission
2. Explain the implications of different order types
3. Check account balance and positions before recommending trades

Be concise but thorough. Use tables for displaying market data when appropriate."""

MARKET_ANALYSIS_INSTRUCTIONS = """You are a market analysis assistant for Lighter Exchange.

Your role is to:
- Provide real-time market data and analysis
- Explain market trends using candlestick patterns
- Compare different trading pairs
- Monitor funding rates for perpetual markets

Focus on delivering accurate, data-driven insights without making price predictions.
Always cite the specific data you're referencing."""

ACCOUNT_MONITOR_INSTRUCTIONS = """You are an account monitoring assistant for Lighter Exchange.

Your role is to:
- Track account balances and positions
- Monitor PnL and performance metrics
- Alert about liquidation risks
- Track deposit and withdrawal history

Provide clear summaries of account status and highlight any concerns."""


def create_trading_agent(
    model: str = "gpt-4",
    include_transactions: bool = False,
    **kwargs
) -> Optional["Agent"]:
    if not AGNO_AVAILABLE:
        print("Error: 'agno' package is not installed. Install with: pip install agno")
        return None

    tools = LighterExchangeTools(include_transactions=include_transactions)

    return Agent(
        model=model,
        instructions=TRADING_AGENT_INSTRUCTIONS,
        tools=list(tools),
        markdown=True,
        **kwargs
    )


def create_market_agent(model: str = "gpt-4", **kwargs) -> Optional["Agent"]:
    if not AGNO_AVAILABLE:
        print("Error: 'agno' package is not installed. Install with: pip install agno")
        return None

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


def create_account_agent(model: str = "gpt-4", **kwargs) -> Optional["Agent"]:
    if not AGNO_AVAILABLE:
        print("Error: 'agno' package is not installed. Install with: pip install agno")
        return None

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
    if not AGNO_AVAILABLE:
        print("To use this module, install agno: pip install agno")
        print("\nExample code:")
        print("""
from agno.agent import Agent
from lighter_agno import LighterExchangeTools

# Create agent with all tools
agent = Agent(
    tools=[LighterExchangeTools()],
    markdown=True
)

# Or use the helper functions
from lighter_agno.agent import create_trading_agent
agent = create_trading_agent()

# Chat with the agent
agent.print_response("What's the current BTC price on Lighter?", stream=True)
""")
    else:
        print("Creating example trading agent...")
        agent = create_trading_agent()
        if agent:
            print("Agent created successfully!")
            print(f"Tools available: {len(LighterExchangeTools())}")
            print("\nExample usage:")
            print('agent.print_response("What markets are available?", stream=True)')
