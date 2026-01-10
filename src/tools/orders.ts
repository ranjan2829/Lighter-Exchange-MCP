/**
 * Order-related tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const orderTools: Tool[] = [
  {
    name: "lighter_get_orders",
    description: "Get orders for an account with optional filtering by market and status.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        market_id: {
          type: "number",
          description: "Filter by market ID",
        },
        status: {
          type: "string",
          enum: ["open", "filled", "cancelled", "all"],
          description: "Filter by order status",
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
      required: ["account_index", "limit"],
    },
  },
  {
    name: "lighter_get_account_active_orders",
    description: "Get all active (open) orders for an account.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
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
      required: ["account_index", "limit"],
    },
  },
  {
    name: "lighter_get_account_inactive_orders",
    description: "Get inactive (filled/cancelled) orders history for an account.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
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
      required: ["account_index", "limit"],
    },
  },
  {
    name: "lighter_get_orderbook_orders",
    description: "Get orders directly from the order book for a specific market.",
    inputSchema: {
      type: "object",
      properties: {
        market_id: {
          type: "number",
          description: "Market ID",
        },
        side: {
          type: "string",
          enum: ["buy", "sell", "all"],
          description: "Filter by order side",
        },
        limit: {
          type: "number",
          description: "Number of orders to return",
        },
      },
      required: ["market_id"],
    },
  },
  {
    name: "lighter_export_orders",
    description: "Export order data for an account within a time range. Useful for record keeping and analysis.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        market_id: {
          type: "number",
          description: "Filter by market ID",
        },
        start_timestamp: {
          type: "number",
          description: "Start timestamp in milliseconds",
        },
        end_timestamp: {
          type: "number",
          description: "End timestamp in milliseconds",
        },
        auth: {
          type: "string",
          description: "Authentication token",
        },
      },
      required: ["account_index"],
    },
  },
];
