/**
 * Transaction-related tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const transactionTools: Tool[] = [
  {
    name: "lighter_get_next_nonce",
    description: `Get the next nonce for signing transactions.

Nonces are "number used once" values that must be incremented for each transaction signed with the same API key. This prevents replay attacks.

Each API key maintains its own nonce counter.`,
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        api_key_index: {
          type: "number",
          description: "API key index (3-254 for custom keys)",
        },
        auth: {
          type: "string",
          description: "Authentication token",
        },
      },
      required: ["account_index", "api_key_index"],
    },
  },
  {
    name: "lighter_send_transaction",
    description: `Send a signed transaction to the Lighter exchange.

Transaction types include:
- Create order (limit, market, stop-loss, take-profit, TWAP)
- Modify order
- Cancel order
- Cancel all orders

The transaction must be pre-signed using the Lighter SDK's SignerClient.`,
    inputSchema: {
      type: "object",
      properties: {
        tx: {
          type: "string",
          description: "Signed transaction data (hex encoded)",
        },
      },
      required: ["tx"],
    },
  },
  {
    name: "lighter_send_transaction_batch",
    description: `Send multiple signed transactions in a single batch.

All transactions are processed atomically. Useful for:
- Submitting multiple orders at once
- Replacing orders (cancel + create)
- Complex trading strategies`,
    inputSchema: {
      type: "object",
      properties: {
        txs: {
          type: "array",
          items: { type: "string" },
          description: "Array of signed transaction data (hex encoded)",
        },
      },
      required: ["txs"],
    },
  },
];
