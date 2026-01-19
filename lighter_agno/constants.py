"""
Lighter Exchange API Constants
"""

# API Configuration
BASE_URL = "https://mainnet.zklighter.elliot.ai/api/v1"
EXPLORER_URL = "https://explorer.elliot.ai/api"
TIMEOUT = 30  # seconds

# API Key Index Reference
API_KEY_INDICES = {
    "DESKTOP": 0,        # Reserved for desktop application
    "MOBILE_PWA": 1,     # Reserved for mobile PWA
    "MOBILE_APP": 2,     # Reserved for mobile app
    "CUSTOM_START": 3,   # First index available for custom API keys
    "CUSTOM_END": 254,   # Last index available for custom API keys
    "ALL": 255,          # Special index to query all API keys
}

# Order Types
ORDER_TYPES = {
    "LIMIT": "ORDER_TYPE_LIMIT",
    "MARKET": "ORDER_TYPE_MARKET",
    "STOP_LOSS": "ORDER_TYPE_STOP_LOSS",
    "STOP_LOSS_LIMIT": "ORDER_TYPE_STOP_LOSS_LIMIT",
    "TAKE_PROFIT": "ORDER_TYPE_TAKE_PROFIT",
    "TAKE_PROFIT_LIMIT": "ORDER_TYPE_TAKE_PROFIT_LIMIT",
    "TWAP": "ORDER_TYPE_TWAP",
}

# Time in Force options
TIME_IN_FORCE = {
    "IMMEDIATE_OR_CANCEL": "ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL",
    "GOOD_TILL_TIME": "ORDER_TIME_IN_FORCE_GOOD_TILL_TIME",
    "POST_ONLY": "ORDER_TIME_IN_FORCE_POST_ONLY",
}

# Valid resolutions for candlesticks and PnL
RESOLUTIONS = ["1m", "5m", "15m", "1h", "4h", "1d"]

# Market filter options
MARKET_FILTERS = ["all", "spot", "perp"]

# Position side options
POSITION_SIDES = ["long", "short", "all"]

# Order status options
ORDER_STATUSES = ["open", "filled", "cancelled", "all"]

# Order side options
ORDER_SIDES = ["buy", "sell", "all"]
