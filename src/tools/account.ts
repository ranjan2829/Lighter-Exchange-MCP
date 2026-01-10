/**
 * Account-related tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const accountTools: Tool[] = [
  {
    name: "lighter_get_account",
    description: `Get account details by account index or L1 address.

Returns comprehensive account information including:
- Account status (1 = active, 0 = inactive)
- Collateral and available balance
- Position details for each market
- Asset balances (USDC, ETH, etc.)

Position fields explained:
- OOC: Open order count in that market
- Sign: 1 for Long, -1 for Short
- Position: Amount of position held
- Avg Entry Price: Average entry price
- Unrealized/Realized PnL: Profit and loss`,
    inputSchema: {
      type: "object",
      properties: {
        by: {
          type: "string",
          enum: ["index", "l1_address"],
          description: "Query type - 'index' for account index, 'l1_address' for Ethereum address",
        },
        value: {
          type: "string",
          description: "The account index number or L1 Ethereum address",
        },
      },
      required: ["by", "value"],
    },
  },
  {
    name: "lighter_get_accounts_by_l1_address",
    description: "Get all accounts (main and sub-accounts) associated with an L1 Ethereum address.",
    inputSchema: {
      type: "object",
      properties: {
        l1_address: {
          type: "string",
          description: "The L1 Ethereum address (0x...)",
        },
      },
      required: ["l1_address"],
    },
  },
  {
    name: "lighter_get_account_limits",
    description: "Get trading limits and restrictions for an account including position limits, leverage limits, and order size constraints.",
    inputSchema: {
      type: "object",
      properties: {
        by: {
          type: "string",
          enum: ["index", "l1_address"],
          description: "Query type",
        },
        value: {
          type: "string",
          description: "Account index or L1 address",
        },
      },
      required: ["by", "value"],
    },
  },
  {
    name: "lighter_get_account_metadata",
    description: "Get account metadata including name, description, and configuration settings.",
    inputSchema: {
      type: "object",
      properties: {
        by: {
          type: "string",
          enum: ["index", "l1_address"],
          description: "Query type",
        },
        value: {
          type: "string",
          description: "Account index or L1 address",
        },
        auth: {
          type: "string",
          description: "Authentication token (required for private data)",
        },
      },
      required: ["by", "value"],
    },
  },
  {
    name: "lighter_get_pnl",
    description: `Get account PnL (Profit and Loss) chart data over time.

Supports multiple time resolutions for different analysis needs:
- 1m, 5m, 15m: Short-term trading analysis
- 1h, 4h: Medium-term trends
- 1d: Long-term performance`,
    inputSchema: {
      type: "object",
      properties: {
        by: {
          type: "string",
          enum: ["index"],
          description: "Query type (currently only 'index' supported)",
        },
        value: {
          type: "string",
          description: "Account index",
        },
        resolution: {
          type: "string",
          enum: ["1m", "5m", "15m", "1h", "4h", "1d"],
          description: "Time resolution for PnL data points",
        },
        start_timestamp: {
          type: "number",
          description: "Start timestamp in milliseconds",
        },
        end_timestamp: {
          type: "number",
          description: "End timestamp in milliseconds",
        },
        count_back: {
          type: "number",
          description: "Number of data points to return",
        },
        ignore_transfers: {
          type: "boolean",
          description: "Exclude deposit/withdrawal effects from PnL calculation",
        },
        auth: {
          type: "string",
          description: "Authentication token",
        },
      },
      required: ["by", "value", "resolution", "start_timestamp", "end_timestamp", "count_back"],
    },
  },
  {
    name: "lighter_get_l1_metadata",
    description: "Get L1 blockchain metadata for an account including on-chain registration details.",
    inputSchema: {
      type: "object",
      properties: {
        by: {
          type: "string",
          enum: ["index", "l1_address"],
          description: "Query type",
        },
        value: {
          type: "string",
          description: "Account index or L1 address",
        },
      },
      required: ["by", "value"],
    },
  },
  {
    name: "lighter_change_account_tier",
    description: `Change account tier between Standard and Premium.

- Standard: Fee-free trading
- Premium: 0.2 bps maker / 2 bps taker fees

Requires authentication.`,
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index to modify",
        },
        tier: {
          type: "string",
          description: "New tier to set",
        },
        auth: {
          type: "string",
          description: "Authentication token (required)",
        },
      },
      required: ["account_index", "tier", "auth"],
    },
  },
  {
    name: "lighter_get_liquidations",
    description: "Get liquidation events history for an account.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        cursor: {
          type: "string",
          description: "Pagination cursor for next page",
        },
        limit: {
          type: "number",
          description: "Number of results (1-100)",
        },
      },
      required: ["account_index", "limit"],
    },
  },
  {
    name: "lighter_get_position_funding",
    description: `Get funding payment history for positions.

Auth is required for accounts linked to main/sub-accounts, but can be omitted for public pools.`,
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        market_id: {
          type: "number",
          description: "Filter by market ID (255 for all markets)",
        },
        cursor: {
          type: "string",
          description: "Pagination cursor",
        },
        limit: {
          type: "number",
          description: "Number of results (1-100)",
        },
        side: {
          type: "string",
          enum: ["long", "short", "all"],
          description: "Filter by position side",
        },
        auth: {
          type: "string",
          description: "Authentication token",
        },
      },
      required: ["account_index", "limit"],
    },
  },
  {
    name: "lighter_get_public_pools_metadata",
    description: "Get metadata for all public liquidity pools.",
    inputSchema: {
      type: "object",
      properties: {},
      required: [],
    },
  },
  {
    name: "lighter_get_positions",
    description: "Get all open positions for an account using the Explorer API.",
    inputSchema: {
      type: "object",
      properties: {
        param: {
          type: "string",
          description: "L1 address or account index",
        },
      },
      required: ["param"],
    },
  },
];
