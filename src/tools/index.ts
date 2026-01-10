/**
 * Tool definitions for Lighter Exchange MCP Server
 * 
 * This module exports all available tools organized by category.
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

import { accountTools } from "./account.js";
import { orderTools } from "./orders.js";
import { marketTools } from "./markets.js";
import { tradingTools } from "./trading.js";
import { transactionTools } from "./transactions.js";
import { apiKeyTools } from "./apikeys.js";
import { bridgeTools } from "./bridge.js";
import { infoTools } from "./info.js";

/**
 * All available tools for the Lighter Exchange MCP Server
 */
export const allTools: Tool[] = [
  ...accountTools,
  ...orderTools,
  ...marketTools,
  ...tradingTools,
  ...transactionTools,
  ...apiKeyTools,
  ...bridgeTools,
  ...infoTools,
];

// Re-export individual tool categories
export {
  accountTools,
  orderTools,
  marketTools,
  tradingTools,
  transactionTools,
  apiKeyTools,
  bridgeTools,
  infoTools,
};

/**
 * Get tool by name
 */
export function getToolByName(name: string): Tool | undefined {
  return allTools.find((tool) => tool.name === name);
}

/**
 * Tool categories for documentation
 */
export const toolCategories = {
  account: {
    name: "Account",
    description: "Account management and information",
    tools: accountTools.map((t) => t.name),
  },
  orders: {
    name: "Orders",
    description: "Order management and history",
    tools: orderTools.map((t) => t.name),
  },
  markets: {
    name: "Markets",
    description: "Market data and information",
    tools: marketTools.map((t) => t.name),
  },
  trading: {
    name: "Trading",
    description: "Trade history and market data",
    tools: tradingTools.map((t) => t.name),
  },
  transactions: {
    name: "Transactions",
    description: "Transaction signing and submission",
    tools: transactionTools.map((t) => t.name),
  },
  apiKeys: {
    name: "API Keys",
    description: "API key management",
    tools: apiKeyTools.map((t) => t.name),
  },
  bridge: {
    name: "Bridge",
    description: "Deposits and withdrawals",
    tools: bridgeTools.map((t) => t.name),
  },
  info: {
    name: "Info",
    description: "Exchange information and notifications",
    tools: infoTools.map((t) => t.name),
  },
} as const;
