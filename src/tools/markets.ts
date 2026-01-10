/**
 * Market-related tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const marketTools: Tool[] = [
  {
    name: "lighter_get_markets",
    description: "Get information about all available trading markets on Lighter Exchange.",
    inputSchema: {
      type: "object",
      properties: {},
      required: [],
    },
  },
  {
    name: "lighter_get_market",
    description: "Get detailed information about a specific market.",
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID",
        },
      },
      required: ["market_id"],
    },
  },
  {
    name: "lighter_get_orderbook",
    description: "Get the order book (bids and asks) for a specific market.",
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID",
        },
        limit: {
          type: "number",
          description: "Number of price levels to return",
        },
      },
      required: ["market_id"],
    },
  },
  {
    name: "lighter_get_orderbook_details",
    description: `Get detailed metadata for order books including:
- Trading pair information
- Fee structure (maker/taker/liquidation fees)
- Margin requirements
- Price decimals and size constraints
- 24h volume and price statistics
- Open interest`,
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID (255 for all markets)",
        },
        filter: {
          type: "string",
          enum: ["all", "spot", "perp"],
          description: "Filter by market type",
        },
      },
      required: [],
    },
  },
  {
    name: "lighter_get_ticker",
    description: "Get current ticker data for a market including last price, 24h volume, and price change.",
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID",
        },
      },
      required: ["market_id"],
    },
  },
  {
    name: "lighter_get_asset_details",
    description: `Get details about supported assets including:
- Asset symbol and ID
- Decimal precision
- Minimum transfer/withdrawal amounts
- Margin mode status
- Current index price
- L1 contract address`,
    inputSchema: {
      type: "object",
      properties: {
        asset_index: {
          type: "number",
          description: "Asset index (omit for all assets)",
        },
      },
      required: [],
    },
  },
];
