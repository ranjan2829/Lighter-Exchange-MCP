/**
 * Tool handlers for Lighter Exchange MCP Server
 * 
 * This module contains all the handler implementations for each tool.
 */

import { apiClient, LighterApiError } from "../api/client.js";
import type { ToolArguments } from "../types.js";

interface CallToolResult {
  content: Array<{
    type: "text";
    text: string;
  }>;
  isError?: boolean;
}

/**
 * Handle tool execution and return formatted result
 */
export async function handleToolCall(
  name: string,
  args: ToolArguments
): Promise<CallToolResult> {
  try {
    const result = await executeToolHandler(name, args);
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(result, null, 2),
        },
      ],
    };
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : "An unknown error occurred";
    const errorDetails = error instanceof LighterApiError 
      ? { error: errorMessage, endpoint: error.endpoint, statusCode: error.statusCode }
      : { error: errorMessage };
    
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(errorDetails, null, 2),
        },
      ],
      isError: true,
    };
  }
}

/**
 * Execute the appropriate handler for a tool
 */
async function executeToolHandler(
  name: string,
  args: ToolArguments
): Promise<unknown> {
  const headers: Record<string, string> = {};
  if (args.authorization) {
    headers["authorization"] = String(args.authorization);
  }

  switch (name) {
    // ============ ACCOUNT ============
    case "lighter_get_account":
      return apiClient.get("/account", {
        by: args.by as string,
        value: args.value as string,
      });

    case "lighter_get_accounts_by_l1_address":
      return apiClient.get("/accountsByL1Address", {
        l1_address: args.l1_address as string,
      });

    case "lighter_get_account_limits":
      return apiClient.get("/accountLimits", {
        by: args.by as string,
        value: args.value as string,
      });

    case "lighter_get_account_metadata":
      return apiClient.get("/accountMetadata", {
        by: args.by as string,
        value: args.value as string,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_pnl":
      return apiClient.get("/pnl", {
        by: args.by as string,
        value: args.value as string,
        resolution: args.resolution as string,
        start_timestamp: args.start_timestamp as number,
        end_timestamp: args.end_timestamp as number,
        count_back: args.count_back as number,
        ignore_transfers: args.ignore_transfers as boolean | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_l1_metadata":
      return apiClient.get("/l1Metadata", {
        by: args.by as string,
        value: args.value as string,
      });

    case "lighter_change_account_tier":
      return apiClient.post("/changeAccountTier", {
        account_index: args.account_index,
        tier: args.tier,
        auth: args.auth,
      }, headers);

    case "lighter_get_liquidations":
      return apiClient.get("/liquidations", {
        account_index: args.account_index as number,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number,
      });

    case "lighter_get_position_funding":
      return apiClient.get("/positionFunding", {
        account_index: args.account_index as number,
        market_id: args.market_id as number | undefined,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number,
        side: args.side as string | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_public_pools_metadata":
      return apiClient.get("/publicPoolsMetadata", {});

    case "lighter_get_positions":
      return apiClient.getExplorer(`/accounts/${args.param}/positions`);

    // ============ ORDERS ============
    case "lighter_get_orders":
      return apiClient.get("/orders", {
        account_index: args.account_index as number,
        market_id: args.market_id as number | undefined,
        status: args.status as string | undefined,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_account_active_orders":
      return apiClient.get("/accountActiveOrders", {
        account_index: args.account_index as number,
        market_id: args.market_id as number | undefined,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_account_inactive_orders":
      return apiClient.get("/accountInactiveOrders", {
        account_index: args.account_index as number,
        market_id: args.market_id as number | undefined,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_orderbook_orders":
      return apiClient.get("/orderBookOrders", {
        market_id: args.market_id as number,
        side: args.side as string | undefined,
        limit: args.limit as number | undefined,
      });

    case "lighter_export_orders":
      return apiClient.get("/export", {
        account_index: args.account_index as number,
        market_id: args.market_id as number | undefined,
        start_timestamp: args.start_timestamp as number | undefined,
        end_timestamp: args.end_timestamp as number | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    // ============ MARKETS ============
    case "lighter_get_markets":
      return apiClient.get("/markets", {});

    case "lighter_get_market":
      return apiClient.get("/market", {
        market_id: args.market_id as number,
      });

    case "lighter_get_orderbook":
      return apiClient.get("/orderbook", {
        market_id: args.market_id as number,
        limit: args.limit as number | undefined,
      });

    case "lighter_get_orderbook_details":
      return apiClient.get("/orderBookDetails", {
        market_id: args.market_id as number | undefined,
        filter: args.filter as string | undefined,
      });

    case "lighter_get_ticker":
      return apiClient.get("/ticker", {
        market_id: args.market_id as number,
      });

    case "lighter_get_asset_details":
      return apiClient.get("/assetDetails", {
        asset_index: args.asset_index as number | undefined,
      });

    // ============ TRADING ============
    case "lighter_get_trades":
      return apiClient.get("/trades", {
        account_index: args.account_index as number | undefined,
        market_id: args.market_id as number | undefined,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_recent_trades":
      return apiClient.get("/recentTrades", {
        market_id: args.market_id as number,
        limit: args.limit as number | undefined,
      });

    case "lighter_get_candlesticks":
      return apiClient.get("/candlestick", {
        market_id: args.market_id as number,
        resolution: args.resolution as string,
        start_timestamp: args.start_timestamp as number | undefined,
        end_timestamp: args.end_timestamp as number | undefined,
        count_back: args.count_back as number | undefined,
      });

    case "lighter_get_funding_rates":
      return apiClient.get("/funding", {
        market_id: args.market_id as number,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number | undefined,
      });

    // ============ TRANSACTIONS ============
    case "lighter_get_next_nonce":
      return apiClient.get("/nextNonce", {
        account_index: args.account_index as number,
        api_key_index: args.api_key_index as number,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_send_transaction":
      return apiClient.post("/sendTx", { tx: args.tx }, headers);

    case "lighter_send_transaction_batch":
      return apiClient.post("/sendTxBatch", { txs: args.txs }, headers);

    // ============ API KEYS ============
    case "lighter_get_api_keys":
      return apiClient.get("/apikeys", {
        account_index: args.account_index as number,
        api_key_index: args.api_key_index as number | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_create_api_key":
      return apiClient.post("/apikeys", {
        account_index: args.account_index,
        api_key_index: args.api_key_index,
        public_key: args.public_key,
        auth: args.auth,
      }, headers);

    case "lighter_delete_api_key":
      return apiClient.delete("/apikeys", {
        account_index: args.account_index,
        api_key_index: args.api_key_index,
        auth: args.auth,
      }, headers);

    // ============ BRIDGE ============
    case "lighter_get_bridge_info":
      return apiClient.get("/bridge", {
        account_index: args.account_index as number | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_deposits":
      return apiClient.get("/deposits", {
        account_index: args.account_index as number,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_withdrawals":
      return apiClient.get("/withdrawals", {
        account_index: args.account_index as number,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    // ============ INFO ============
    case "lighter_get_info":
      return apiClient.get("/info", {});

    case "lighter_get_exchange_stats":
      return apiClient.get("/exchangeStats", {});

    case "lighter_get_announcements":
      return apiClient.get("/announcements", {
        cursor: args.cursor as string | undefined,
        limit: args.limit as number | undefined,
      });

    case "lighter_get_notifications":
      return apiClient.get("/notifications", {
        account_index: args.account_index as number,
        cursor: args.cursor as string | undefined,
        limit: args.limit as number | undefined,
        auth: args.auth as string | undefined,
      }, headers);

    case "lighter_get_referral_info":
      return apiClient.get("/referral", {
        account_index: args.account_index as number,
        auth: args.auth as string | undefined,
      }, headers);

    default:
      throw new Error(`Unknown tool: ${name}`);
  }
}
