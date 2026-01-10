# Lighter Exchange MCP Server

A Model Context Protocol (MCP) server for interacting with the Lighter Exchange API. Provides 40 tools for account management, trading, market data, and more.

## Overview

Lighter is a high-performance perpetual and spot trading exchange built on zkSync. This MCP server enables AI assistants to query account data, market information, and execute trading operations through the Lighter API.

**API Endpoints:**
- Main API: `https://mainnet.zklighter.elliot.ai/api/v1`
- Explorer API: `https://explorer.elliot.ai/api`

## Installation

```bash
npm install
npm run build
```

## Configuration

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "lighter": {
      "command": "node",
      "args": ["/path/to/Lighter-Exchange-MCP/dist/index.js"]
    }
  }
}
```

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "lighter": {
      "command": "node",
      "args": ["/path/to/Lighter-Exchange-MCP/dist/index.js"]
    }
  }
}
```

## Project Structure

```
src/
├── index.ts              # Server entry point
├── constants.ts          # API URLs, enums
├── types.ts              # TypeScript interfaces
├── api/
│   ├── index.ts          # API exports
│   └── client.ts         # HTTP client
├── tools/
│   ├── index.ts          # Tool exports
│   ├── account.ts        # Account tools
│   ├── orders.ts         # Order tools
│   ├── markets.ts        # Market tools
│   ├── trading.ts        # Trading tools
│   ├── transactions.ts   # Transaction tools
│   ├── apikeys.ts        # API key tools
│   ├── bridge.ts         # Bridge tools
│   └── info.ts           # Info tools
└── handlers/
    └── index.ts          # Tool handlers
```

## Tools Reference

### Account (11 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_account` | Get account by index or L1 address |
| `lighter_get_accounts_by_l1_address` | Get all accounts for an L1 address |
| `lighter_get_account_limits` | Get trading limits |
| `lighter_get_account_metadata` | Get account metadata |
| `lighter_get_pnl` | Get PnL chart data |
| `lighter_get_l1_metadata` | Get L1 blockchain metadata |
| `lighter_change_account_tier` | Change account tier |
| `lighter_get_liquidations` | Get liquidation history |
| `lighter_get_position_funding` | Get funding payments |
| `lighter_get_public_pools_metadata` | Get public pools info |
| `lighter_get_positions` | Get positions (Explorer API) |

### Orders (5 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_orders` | Get orders with filters |
| `lighter_get_account_active_orders` | Get open orders |
| `lighter_get_account_inactive_orders` | Get filled/cancelled orders |
| `lighter_get_orderbook_orders` | Get orderbook orders |
| `lighter_export_orders` | Export order history |

### Markets (6 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_markets` | Get all markets |
| `lighter_get_market` | Get specific market |
| `lighter_get_orderbook` | Get orderbook |
| `lighter_get_orderbook_details` | Get market metadata |
| `lighter_get_ticker` | Get ticker data |
| `lighter_get_asset_details` | Get asset information |

### Trading (4 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_trades` | Get trade history |
| `lighter_get_recent_trades` | Get recent trades |
| `lighter_get_candlesticks` | Get OHLCV data |
| `lighter_get_funding_rates` | Get funding rate history |

### Transactions (3 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_next_nonce` | Get next nonce for signing |
| `lighter_send_transaction` | Send signed transaction |
| `lighter_send_transaction_batch` | Send transaction batch |

### API Keys (3 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_api_keys` | Get API keys |
| `lighter_create_api_key` | Create API key |
| `lighter_delete_api_key` | Delete API key |

### Bridge (3 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_bridge_info` | Get bridge information |
| `lighter_get_deposits` | Get deposit history |
| `lighter_get_withdrawals` | Get withdrawal history |

### Info (5 tools)

| Tool | Description |
|------|-------------|
| `lighter_get_info` | Get exchange info |
| `lighter_get_exchange_stats` | Get exchange statistics |
| `lighter_get_announcements` | Get announcements |
| `lighter_get_notifications` | Get notifications |
| `lighter_get_referral_info` | Get referral info |

## API Key System

| Index | Purpose |
|-------|---------|
| 0 | Desktop |
| 1 | Mobile PWA |
| 2 | Mobile App |
| 3-254 | Custom keys |
| 255 | Query all |

## Account Types

- **Standard**: Fee-free trading
- **Premium**: 0.2 bps maker / 2 bps taker

## Usage Examples

Get account by address:
```json
{
  "name": "lighter_get_account",
  "arguments": {
    "by": "l1_address",
    "value": "0x..."
  }
}
```

Get market data:
```json
{
  "name": "lighter_get_orderbook_details",
  "arguments": {
    "filter": "perp"
  }
}
```

Get candlesticks:
```json
{
  "name": "lighter_get_candlesticks",
  "arguments": {
    "market_id": 0,
    "resolution": "1h",
    "count_back": 100
  }
}
```

## Development

```bash
npm run dev    # Watch mode
npm run build  # Production build
npm start      # Run server
```

## License

MIT
