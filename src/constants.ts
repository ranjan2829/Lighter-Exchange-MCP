/**
 * Lighter Exchange MCP Server Constants
 */

export const API_CONFIG = {
  /** Main Lighter Exchange API */
  BASE_URL: "https://mainnet.zklighter.elliot.ai/api/v1",
  
  /** Lighter Explorer API */
  EXPLORER_URL: "https://explorer.elliot.ai/api",
  
  /** Default timeout in milliseconds */
  TIMEOUT: 30000,
} as const;

export const API_KEY_INDICES = {
  /** Reserved for desktop application */
  DESKTOP: 0,
  /** Reserved for mobile PWA */
  MOBILE_PWA: 1,
  /** Reserved for mobile app */
  MOBILE_APP: 2,
  /** First index available for custom API keys */
  CUSTOM_START: 3,
  /** Last index available for custom API keys */
  CUSTOM_END: 254,
  /** Special index to query all API keys */
  ALL: 255,
} as const;

export const ORDER_TYPES = {
  LIMIT: "ORDER_TYPE_LIMIT",
  MARKET: "ORDER_TYPE_MARKET",
  STOP_LOSS: "ORDER_TYPE_STOP_LOSS",
  STOP_LOSS_LIMIT: "ORDER_TYPE_STOP_LOSS_LIMIT",
  TAKE_PROFIT: "ORDER_TYPE_TAKE_PROFIT",
  TAKE_PROFIT_LIMIT: "ORDER_TYPE_TAKE_PROFIT_LIMIT",
  TWAP: "ORDER_TYPE_TWAP",
} as const;

export const TIME_IN_FORCE = {
  IMMEDIATE_OR_CANCEL: "ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL",
  GOOD_TILL_TIME: "ORDER_TIME_IN_FORCE_GOOD_TILL_TIME",
  POST_ONLY: "ORDER_TIME_IN_FORCE_POST_ONLY",
} as const;

export const RESOLUTIONS = ["1m", "5m", "15m", "1h", "4h", "1d"] as const;

export const MARKET_FILTERS = ["all", "spot", "perp"] as const;

export const POSITION_SIDES = ["long", "short", "all"] as const;

export const ORDER_STATUSES = ["open", "filled", "cancelled", "all"] as const;
