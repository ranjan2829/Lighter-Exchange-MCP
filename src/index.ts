#!/usr/bin/env node

/**
 * Lighter Exchange MCP Server
 * 
 * A Model Context Protocol server providing access to the Lighter Exchange API.
 * Enables AI assistants to interact with Lighter's perpetual and spot trading platform.
 * 
 * @see https://docs.lighter.xyz - Lighter API Documentation
 * @see https://modelcontextprotocol.io - MCP Specification
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

import { allTools } from "./tools/index.js";
import { handleToolCall } from "./handlers/index.js";

const SERVER_NAME = "lighter-exchange-mcp";
const SERVER_VERSION = "1.0.0";

/**
 * Create and configure the MCP server
 */
function createServer(): Server {
  const server = new Server(
    {
      name: SERVER_NAME,
      version: SERVER_VERSION,
    },
    {
      capabilities: {
        tools: {},
      },
    }
  );

  // Register tool list handler
  server.setRequestHandler(ListToolsRequestSchema, async () => {
    return { tools: allTools };
  });

  // Register tool execution handler
  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    const result = await handleToolCall(name, args ?? {});
    return result as { content: Array<{ type: "text"; text: string }> };
  });

  return server;
}

/**
 * Main entry point
 */
async function main(): Promise<void> {
  const server = createServer();
  const transport = new StdioServerTransport();
  
  await server.connect(transport);
  
  console.error(`${SERVER_NAME} v${SERVER_VERSION} running on stdio`);
  console.error(`Loaded ${allTools.length} tools`);
}

// Run the server
main().catch((error) => {
  console.error("Fatal error:", error);
  process.exit(1);
});
