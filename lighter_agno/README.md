# Lighter Exchange Agno Toolkit

A Python toolkit for integrating **Lighter Exchange** with **Agno AI agents**. Provides 40 tools for trading, account management, and market data on Lighter Exchange (zkSync).

## Installation

```bash
# Install core package
pip install httpx

# For Agno integration
pip install agno openai

# Or install from this directory
cd lighter_agno
pip install -e .
```

## Quick Start

### Basic Usage with Agno

```python
from agno.agent import Agent
from lighter_agno import LighterExchangeTools

# Create an agent with all 40 Lighter Exchange tools
agent = Agent(
    tools=[LighterExchangeTools()],
    markdown=True
)

# Ask about markets
agent.print_response("What trading pairs are available on Lighter Exchange?", stream=True)

# Check a specific market
agent.print_response("What's the current BTC-PERP price and orderbook?", stream=True)
```

### Using Pre-configured Agents

```python
from lighter_agno.agent import create_trading_agent, create_market_agent

# Full trading agent (read + write capabilities)
trading_agent = create_trading_agent(include_transactions=True)

# Market analysis agent (read-only)
market_agent = create_market_agent()

# Start chatting
market_agent.print_response("Analyze the ETH-PERP funding rates", stream=True)
```

### Direct Tool Usage (without Agno)

```python
from lighter_agno.tools.markets import get_markets, get_ticker, get_orderbook
from lighter_agno.tools.trading import get_candlesticks

# Get all markets
markets = get_markets()
print(markets)

# Get BTC ticker (market_id=0)
ticker = get_ticker(market_id=0)
print(ticker)

# Get orderbook
orderbook = get_orderbook(market_id=0, limit=10)
print(orderbook)

# Get candlestick data
candles = get_candlesticks(market_id=0, resolution="1h", count_back=24)
print(candles)
```

## Available Tools (40 Total)

### Account Tools (11)
| Tool | Description |
|------|-------------|
| `get_account` | Get account details by index or L1 address |
| `get_accounts_by_l1_address` | Get all accounts for an Ethereum address |
| `get_account_limits` | Get trading limits and restrictions |
| `get_account_metadata` | Get account name and configuration |
| `get_pnl` | Get PnL chart data over time |
| `get_l1_metadata` | Get blockchain registration info |
| `change_account_tier` | Switch between Standard/Premium tiers |
| `get_liquidations` | Get liquidation history |
| `get_position_funding` | Get funding payment history |
| `get_public_pools_metadata` | Get liquidity pool information |
| `get_positions` | Get all open positions |

### Order Tools (5)
| Tool | Description |
|------|-------------|
| `get_orders` | Get orders with filtering options |
| `get_account_active_orders` | Get open orders |
| `get_account_inactive_orders` | Get filled/cancelled orders |
| `get_orderbook_orders` | Get live orderbook orders |
| `export_orders` | Export order history |

### Market Tools (6)
| Tool | Description |
|------|-------------|
| `get_markets` | Get all available markets |
| `get_market` | Get specific market details |
| `get_orderbook` | Get bid/ask price levels |
| `get_orderbook_details` | Get market metadata (fees, margins) |
| `get_ticker` | Get current price and 24h volume |
| `get_asset_details` | Get supported assets info |

### Trading Tools (4)
| Tool | Description |
|------|-------------|
| `get_trades` | Get trade history |
| `get_recent_trades` | Get recent market trades |
| `get_candlesticks` | Get OHLCV data |
| `get_funding_rates` | Get funding rate history |

### Transaction Tools (3)
| Tool | Description |
|------|-------------|
| `get_next_nonce` | Get nonce for signing |
| `send_transaction` | Send signed transaction |
| `send_transaction_batch` | Send multiple transactions |

### API Key Tools (3)
| Tool | Description |
|------|-------------|
| `get_api_keys` | Get account API keys |
| `create_api_key` | Create new API key |
| `delete_api_key` | Delete API key |

### Bridge Tools (3)
| Tool | Description |
|------|-------------|
| `get_bridge_info` | Get bridge details |
| `get_deposits` | Get deposit history |
| `get_withdrawals` | Get withdrawal history |

### Info Tools (5)
| Tool | Description |
|------|-------------|
| `get_info` | Get exchange status |
| `get_exchange_stats` | Get volume and metrics |
| `get_announcements` | Get maintenance notices |
| `get_notifications` | Get account notifications |
| `get_referral_info` | Get referral program details |

## Selective Tool Loading

Load only the tools you need:

```python
from lighter_agno.toolkit import LighterExchangeTools

# Only market data tools (read-only)
tools = LighterExchangeTools(
    include_account=False,
    include_orders=False,
    include_transactions=False,
    include_apikeys=False,
    include_bridge=False,
)

# Or use convenience functions
from lighter_agno.toolkit import get_market_tools, get_account_tools
market_tools = get_market_tools()  # 6 tools
account_tools = get_account_tools()  # 11 tools
```

## Authentication

For authenticated endpoints, pass the authorization token:

```python
from lighter_agno.tools.account import get_account_metadata

# With authentication
result = get_account_metadata(
    by="index",
    value="123",
    auth="your-auth-token",
    authorization="Bearer your-token"
)
```

## API Reference

### Lighter Exchange API
- Main API: `https://mainnet.zklighter.elliot.ai/api/v1`
- Explorer API: `https://explorer.elliot.ai/api`

### Supported Resolutions
- Candlesticks/PnL: `1m`, `5m`, `15m`, `1h`, `4h`, `1d`

### Order Types
- `LIMIT`, `MARKET`, `STOP_LOSS`, `STOP_LOSS_LIMIT`
- `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`, `TWAP`

## License

MIT License
