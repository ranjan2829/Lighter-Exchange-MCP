/**
 * General info tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const infoTools: Tool[] = [
  {
    name: "lighter_get_info",
    description: "Get general exchange information including status, version, and system health.",
    inputSchema: {
      type: "object",
      properties: {},
      required: [],
    },
  },
  {
    name: "lighter_get_exchange_stats",
    description: "Get exchange-wide statistics including total volume, number of users, and market metrics.",
    inputSchema: {
      type: "object",
      properties: {},
      required: [],
    },
  },
  {
    name: "lighter_get_announcements",
    description: "Get exchange announcements including maintenance notices, new features, and market updates.",
    inputSchema: {
      type: "object",
      properties: {
        cursor: {
          type: "string",
          description: "Pagination cursor",
        },
        limit: {
          type: "number",
          description: "Number of results",
        },
      },
      required: [],
    },
  },
  {
    name: "lighter_get_notifications",
    description: "Get account notifications including order fills, liquidation warnings, and system alerts.",
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
    name: "lighter_get_referral_info",
    description: "Get referral program information for an account including referral code, earnings, and referred users.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
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
