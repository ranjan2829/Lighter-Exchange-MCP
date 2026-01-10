/**
 * Bridge (deposits/withdrawals) tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const bridgeTools: Tool[] = [
  {
    name: "lighter_get_bridge_info",
    description: "Get bridge information including supported assets, minimum amounts, and deposit/withdrawal instructions.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index (optional)",
        },
        auth: {
          type: "string",
          description: "Authentication token",
        },
      },
      required: [],
    },
  },
  {
    name: "lighter_get_deposits",
    description: "Get deposit history for an account including pending and completed deposits.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        cursor: {
          type: "string",
          description: "Pagination cursor",
        },
        limit: {
          type: "number",
          description: "Number of results",
        },
        auth: {
          type: "string",
          description: "Authentication token",
        },
      },
      required: ["account_index"],
    },
  },
  {
    name: "lighter_get_withdrawals",
    description: "Get withdrawal history for an account including pending and completed withdrawals.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        cursor: {
          type: "string",
          description: "Pagination cursor",
        },
        limit: {
          type: "number",
          description: "Number of results",
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
