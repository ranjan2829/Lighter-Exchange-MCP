"""
API Key management tools for Lighter Exchange.

Provides 3 tools for managing API keys.
"""

import json
from typing import Optional
from lighter_agno.client import get_client


def get_api_keys(
    account_index: int,
    api_key_index: Optional[int] = None,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get API keys for an account.

    API Key Index Reference:
    - 0: Reserved for desktop application
    - 1: Reserved for mobile PWA
    - 2: Reserved for mobile app
    - 3-254: Available for custom API keys (up to 252 keys)
    - 255: Query all API keys

    Use index 255 to retrieve information about all API keys.

    Args:
        account_index: Account index
        api_key_index: API key index (0-254 for specific key, 255 for all)
        auth: Authentication token

    Returns:
        JSON string with API key information
    """
    client = get_client(authorization)
    result = client.get("/apikeys", {
        "account_index": account_index,
        "api_key_index": api_key_index,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def create_api_key(
    account_index: int,
    api_key_index: int,
    public_key: str,
    auth: str,
    authorization: Optional[str] = None
) -> str:
    """Create a new API key for an account.

    You can create up to 252 custom API keys (indices 3-254).
    The public key should be generated securely and the corresponding
    private key stored safely.

    Requires authentication.

    Args:
        account_index: Account index
        api_key_index: API key index to create (3-254)
        public_key: Public key for the new API key
        auth: Authentication token (required)

    Returns:
        JSON string with created API key details
    """
    client = get_client(authorization)
    result = client.post("/apikeys", {
        "account_index": account_index,
        "api_key_index": api_key_index,
        "public_key": public_key,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def delete_api_key(
    account_index: int,
    api_key_index: int,
    auth: str,
    authorization: Optional[str] = None
) -> str:
    """Delete an API key from an account.

    Requires authentication.

    Args:
        account_index: Account index
        api_key_index: API key index to delete (3-254)
        auth: Authentication token (required)

    Returns:
        JSON string with deletion result
    """
    client = get_client(authorization)
    result = client.delete("/apikeys", {
        "account_index": account_index,
        "api_key_index": api_key_index,
        "auth": auth,
    })
    return json.dumps(result, indent=2)
