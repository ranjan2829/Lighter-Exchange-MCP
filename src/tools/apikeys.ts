/**
 * API Key management tool definitions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";

export const apiKeyTools: Tool[] = [
  {
    name: "lighter_get_api_keys",
    description: `Get API keys for an account.

API Key Index Reference:
- 0: Reserved for desktop application
- 1: Reserved for mobile PWA
- 2: Reserved for mobile app
- 3-254: Available for custom API keys (up to 252 keys)
- 255: Query all API keys

Use index 255 to retrieve information about all API keys.`,
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        api_key_index: {
          type: "number",
          description: "API key index (0-254 for specific key, 255 for all)",
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
    name: "lighter_create_api_key",
    description: `Create a new API key for an account.

You can create up to 252 custom API keys (indices 3-254).
The public key should be generated securely and the corresponding private key stored safely.

Requires authentication.`,
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        api_key_index: {
          type: "number",
          description: "API key index to create (3-254)",
        },
        public_key: {
          type: "string",
          description: "Public key for the new API key",
        },
        auth: {
          type: "string",
          description: "Authentication token (required)",
        },
      },
      required: ["account_index", "api_key_index", "public_key", "auth"],
    },
  },
  {
    name: "lighter_delete_api_key",
    description: "Delete an API key from an account. Requires authentication.",
    inputSchema: {
      type: "object",
      properties: {
        account_index: {
          type: "number",
          description: "Account index",
        },
        api_key_index: {
          type: "number",
          description: "API key index to delete (3-254)",
        },
        auth: {
          type: "string",
          description: "Authentication token (required)",
        },
      },
      required: ["account_index", "api_key_index", "auth"],
    },
  },
];
