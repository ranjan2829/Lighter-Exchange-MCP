/**
 * Lighter Exchange MCP Server Types
 */

import type { RESOLUTIONS, MARKET_FILTERS, POSITION_SIDES, ORDER_STATUSES } from "./constants.js";

// ============ API Types ============

export type Resolution = typeof RESOLUTIONS[number];
export type MarketFilter = typeof MARKET_FILTERS[number];
export type PositionSide = typeof POSITION_SIDES[number];
export type OrderStatus = typeof ORDER_STATUSES[number];

export interface ApiRequestParams {
  [key: string]: string | number | boolean | undefined;
}

export interface ApiHeaders {
  [key: string]: string;
}

// ============ Account Types ============

export interface Position {
  market_id: number;
  symbol: string;
  initial_margin_fraction: string;
  open_order_count: number;
  pending_order_count: number;
  position_tied_order_count: number;
  sign: number;
  position: string;
  avg_entry_price: string;
  position_value: string;
  unrealized_pnl: string;
  realized_pnl: string;
  liquidation_price: string;
  margin_mode: number;
  allocated_margin: string;
}

export interface Asset {
  symbol: string;
  asset_id: number;
  balance: string;
  locked_balance: string;
}

export interface Account {
  code: number;
  account_type: number;
  index: number;
  l1_address: string;
  cancel_all_time: number;
  total_order_count: number;
  total_isolated_order_count: number;
  pending_order_count: number;
  available_balance: string;
  status: number;
  collateral: string;
  transaction_time: number;
  account_index: number;
  name: string;
  description: string;
  can_invite: boolean;
  referral_points_percentage: string;
  positions: Position[];
  assets: Asset[];
  total_asset_value: string;
  cross_asset_value: string;
  shares: unknown[];
}

// ============ Market Types ============

export interface MarketConfig {
  market_margin_mode: number;
  insurance_fund_account_index: number;
  liquidation_mode: number;
  force_reduce_only: boolean;
  trading_hours: string;
}

export interface OrderBookDetail {
  symbol: string;
  market_id: number;
  market_type: "perp" | "spot";
  base_asset_id: number;
  quote_asset_id: number;
  status: string;
  taker_fee: string;
  maker_fee: string;
  liquidation_fee: string;
  min_base_amount: string;
  min_quote_amount: string;
  order_quote_limit: string;
  supported_size_decimals: number;
  supported_price_decimals: number;
  supported_quote_decimals: number;
  size_decimals: number;
  price_decimals: number;
  quote_multiplier: number;
  default_initial_margin_fraction: number;
  min_initial_margin_fraction: number;
  maintenance_margin_fraction: number;
  closeout_margin_fraction: number;
  last_trade_price: number;
  daily_trades_count: number;
  daily_base_token_volume: number;
  daily_quote_token_volume: number;
  daily_price_low: number;
  daily_price_high: number;
  daily_price_change: number;
  open_interest: number;
  daily_chart: Record<string, unknown>;
  market_config: MarketConfig;
}

// ============ Asset Types ============

export interface AssetDetail {
  asset_id: number;
  symbol: string;
  l1_decimals: number;
  decimals: number;
  min_transfer_amount: string;
  min_withdrawal_amount: string;
  margin_mode: string;
  index_price: string;
  l1_address: string;
}

// ============ Tool Types ============

export interface ToolArguments {
  [key: string]: unknown;
}

export interface ToolResult {
  content: Array<{
    type: "text";
    text: string;
  }>;
}
