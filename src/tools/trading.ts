/**
 * Trading-related tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const tradingTools: Tool[] = [
  {
    name: "lighter_get_trades",
    description: "Get trade history for an account or market.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Filter by account index",
        },
        market_id: {
          type: "number",
          description: "Filter by market ID",
        },
        cursor: {
          type: "string",
          description: "Pagination cursor",
        },
        limit: {
          type: "number",
          description: "Number of results (1-100)",
        },
        auth: {
          type: "string",
          description: "Authentication token",
        },
      },
      required: ["limit"],
    },
  },
  {
    name: "lighter_get_recent_trades",
    description: "Get the most recent trades for a market.",
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID",
        },
        limit: {
          type: "number",
          description: "Number of trades to return",
        },
      },
      required: ["market_id"],
    },
  },
  {
    name: "lighter_get_candlesticks",
    description: `Get OHLCV (Open, High, Low, Close, Volume) candlestick data for charting.

Supported resolutions:
- 1m, 5m, 15m: Intraday analysis
- 1h, 4h: Swing trading
- 1d: Daily charts`,
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID",
        },
        resolution: {
          type: "string",
          enum: ["1m", "5m", "15m", "1h", "4h", "1d"],
          description: "Candlestick time resolution",
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
          description: "Number of candles to return",
        },
      },
      required: ["market_id", "resolution"],
    },
  },
  {
    name: "lighter_get_funding_rates",
    description: "Get funding rate history for perpetual markets. Funding rates are periodic payments between long and short positions.",
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID",
        },
        cursor: {
          type: "string",
          description: "Pagination cursor",
        },
        limit: {
          type: "number",
          description: "Number of results",
        },
      },
      required: ["market_id"],
    },
  },
];
