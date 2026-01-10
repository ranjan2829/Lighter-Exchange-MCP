# Lighter Exchange MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with the [Lighter Exchange API](https://mainnet.zklighter.elliot.ai/api/v1).

## Features

This MCP server exposes the following Lighter Exchange API endpoints as tools:

### Account Tools
- **`get_account`** - Get account details by index or L1 address
- **`get_accounts_by_l1_address`** - Get all accounts for an L1 address
- **`get_account_limits`** - Get account limits
- **`get_account_metadata`** - Get account metadata
- **`get_pnl`** - Get PnL chart data with various resolutions
- **`get_l1_metadata`** - Get L1 metadata
- **`change_account_tier`** - Change account tier (POST)
- **`get_liquidations`** - Get liquidation events
- **`get_position_funding`** - Get position funding data
- **`get_public_pools_metadata`** - Get public pools metadata
- **`get_positions`** - Get positions by address or account index (Explorer API)

### Order Tools
- **`get_orders`** - Get orders for an account
- **`get_account_active_orders`** - Get active (open) orders for an account
- **`get_account_inactive_orders`** - Get inactive (filled/cancelled) orders
- **`get_orderbook_orders`** - Get orders from the order book
- **`export_orders`** - Export order data for an account

### Market Tools
- **`get_markets`** - Get all available markets
- **`get_market`** - Get specific market info
- **`get_orderbook`** - Get orderbook data
- **`get_orderbook_details`** - Get order books metadata (filter by spot/perp)
- **`get_ticker`** - Get ticker data

### Trading Tools
- **`get_trades`** - Get trades for an account or market
- **`get_recent_trades`** - Get recent trades for a market

### Data Tools
- **`get_candlesticks`** - Get OHLCV candlestick data
- **`get_funding_rates`** - Get funding rate history
- **`get_asset_details`** - Get asset details

### Info & Stats
- **`get_info`** - Get exchange information
- **`get_exchange_stats`** - Get exchange statistics

### Transaction API
- **`get_next_nonce`** - Get next nonce for signing transactions
- **`send_transaction`** - Send a signed transaction
- **`send_transaction_batch`** - Send multiple signed transactions

### API Keys
- **`get_api_keys`** - Get API keys for an account
- **`create_api_key`** - Create a new API key
- **`delete_api_key`** - Delete an API key

### Bridge
- **`get_bridge_info`** - Get bridge information
- **`get_deposits`** - Get deposit history
- **`get_withdrawals`** - Get withdrawal history

### Other
- **`get_announcements`** - Get exchange announcements
- **`get_notifications`** - Get account notifications
- **`get_referral_info`** - Get referral information

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd Lighter-Exchange-MCP

# Install dependencies
npm install

# Build the project
npm run build
```

## Usage

### With Claude Desktop

Add this configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "lighter-exchange": {
      "command": "node",
      "args": ["/path/to/Lighter-Exchange-MCP/dist/index.js"]
    }
  }
}
```

### With Cursor

Add to your Cursor MCP settings (`.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "lighter-exchange": {
      "command": "node",
      "args": ["/path/to/Lighter-Exchange-MCP/dist/index.js"]
    }
  }
}
```

## Tool Examples

### Get Account by Index

```json
{
  "name": "get_account",
  "arguments": {
    "by": "index",
    "value": "123"
  }
}
```

### Get Account by L1 Address

```json
{
  "name": "get_account",
  "arguments": {
    "by": "l1_address",
    "value": "0x..."
  }
}
```

### Get PnL Data

```json
{
  "name": "get_pnl",
  "arguments": {
    "by": "index",
    "value": "123",
    "resolution": "1h",
    "start_timestamp": 1704067200000,
    "end_timestamp": 1704153600000,
    "count_back": 100
  }
}
```

### Get Position Funding

```json
{
  "name": "get_position_funding",
  "arguments": {
    "account_index": 123,
    "limit": 50,
    "side": "all"
  }
}
```

### Get Candlestick Data

```json
{
  "name": "get_candlesticks",
  "arguments": {
    "market_id": 0,
    "resolution": "1h",
    "count_back": 100
  }
}
```

### Get Markets

```json
{
  "name": "get_markets",
  "arguments": {}
}
```

### Get Asset Details

```json
{
  "name": "get_asset_details",
  "arguments": {
    "asset_index": 0
  }
}
```

### Get Orderbook Details

```json
{
  "name": "get_orderbook_details",
  "arguments": {
    "market_id": 255,
    "filter": "perp"
  }
}
```

### Get Positions (Explorer API)

```json
{
  "name": "get_positions",
  "arguments": {
    "param": "0x..."
  }
}
```

### Get Active Orders

```json
{
  "name": "get_account_active_orders",
  "arguments": {
    "account_index": 123,
    "limit": 50
  }
}
```

### Get Recent Trades

```json
{
  "name": "get_recent_trades",
  "arguments": {
    "market_id": 0,
    "limit": 100
  }
}
```

### Get Next Nonce (for signing transactions)

```json
{
  "name": "get_next_nonce",
  "arguments": {
    "account_index": 123,
    "api_key_index": 3
  }
}
```

### Get API Keys

```json
{
  "name": "get_api_keys",
  "arguments": {
    "account_index": 123,
    "api_key_index": 255
  }
}
```

### Get Deposits

```json
{
  "name": "get_deposits",
  "arguments": {
    "account_index": 123,
    "limit": 50
  }
}
```

## API Key System

Lighter uses an API key system for authentication and transaction signing:

| Index | Purpose |
|-------|---------|
| 0 | Desktop application |
| 1 | Mobile PWA |
| 2 | Mobile app |
| 3-254 | Custom API keys (up to 252) |
| 255 | Query all API keys |

### Nonces

When signing transactions, you must provide a nonce (number used once):
- Nonces must be incremented for each transaction
- Each nonce is handled per API_KEY
- Use `get_next_nonce` to get the next available nonce

### Account Types

- **Standard Account**: Fee-free trading
- **Premium Account**: 0.2 bps maker / 2 bps taker fees

## Response Details

### Account Response Fields

| Field | Description |
|-------|-------------|
| Status | 1 = active, 0 = inactive |
| Collateral | Amount of collateral in account |

### Position Details

| Field | Description |
|-------|-------------|
| OOC | Open order count in that market |
| Sign | 1 for Long, -1 for Short |
| Position | Amount of position in that market |
| Avg Entry Price | Average entry price of the position |
| Position Value | Value of the position |
| Unrealized PnL | Unrealized profit and loss |
| Realized PnL | Realized profit and loss |

## Development

```bash
# Run in development mode (watch for changes)
npm run dev

# Build for production
npm run build

# Run the server
npm start
```

## API Reference

This MCP server connects to two Lighter Exchange APIs:

### Main API
- **Base URL**: `https://mainnet.zklighter.elliot.ai/api/v1`
- **Endpoints**: Account, Orders, Markets, Trading, Candlesticks, Funding

### Explorer API
- **Base URL**: `https://explorer.elliot.ai/api`
- **Endpoints**: Positions (by address/account)

- **Documentation**: [Lighter API Docs](https://docs.lighter.xyz)

## License

MIT
