"""
Transaction-related tools for Lighter Exchange.

Provides 3 tools for transaction signing and submission.
"""

import json
from typing import Optional, List
from lighter_agno.client import get_client


def get_next_nonce(
    account_index: int,
    api_key_index: int,
    auth: Optional[str] = None,
    authorization: Optional[str] = None
) -> str:
    """Get the next nonce for signing transactions.

    Nonces are "number used once" values that must be incremented for each
    transaction signed with the same API key. This prevents replay attacks.

    Each API key maintains its own nonce counter.

    Args:
        account_index: Account index
        api_key_index: API key index (3-254 for custom keys)
        auth: Authentication token

    Returns:
        JSON string with next nonce value
    """
    client = get_client(authorization)
    result = client.get("/nextNonce", {
        "account_index": account_index,
        "api_key_index": api_key_index,
        "auth": auth,
    })
    return json.dumps(result, indent=2)


def send_transaction(
    tx: str,
    authorization: Optional[str] = None
) -> str:
    """Send a signed transaction to the Lighter exchange.

    Transaction types include:
    - Create order (limit, market, stop-loss, take-profit, TWAP)
    - Modify order
    - Cancel order
    - Cancel all orders

    The transaction must be pre-signed using the Lighter SDK's SignerClient.

    Args:
        tx: Signed transaction data (hex encoded)

    Returns:
        JSON string with transaction result
    """
    client = get_client(authorization)
    result = client.post("/sendTx", {"tx": tx})
    return json.dumps(result, indent=2)


def send_transaction_batch(
    txs: List[str],
    authorization: Optional[str] = None
) -> str:
    """Send multiple signed transactions in a single batch.

    All transactions are processed atomically. Useful for:
    - Submitting multiple orders at once
    - Replacing orders (cancel + create)
    - Complex trading strategies

    Args:
        txs: Array of signed transaction data (hex encoded)

    Returns:
        JSON string with batch transaction results
    """
    client = get_client(authorization)
    result = client.post("/sendTxBatch", {"txs": txs})
    return json.dumps(result, indent=2)
