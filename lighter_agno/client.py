"""
Lighter Exchange API Client

Handles all HTTP requests to the Lighter Exchange APIs.
"""

import httpx
from typing import Any, Optional
from lighter_agno.constants import BASE_URL, EXPLORER_URL, TIMEOUT


class LighterApiError(Exception):
    """Custom exception for Lighter API errors."""

    def __init__(self, message: str, status_code: int, endpoint: str):
        super().__init__(message)
        self.status_code = status_code
        self.endpoint = endpoint


class LighterClient:
    """
    API Client for Lighter Exchange.

    Supports both synchronous and asynchronous requests.
    """

    def __init__(
        self,
        base_url: str = BASE_URL,
        explorer_url: str = EXPLORER_URL,
        authorization: Optional[str] = None,
        timeout: int = TIMEOUT
    ):
        self.base_url = base_url
        self.explorer_url = explorer_url
        self.authorization = authorization
        self.timeout = timeout

    def _filter_params(self, params: dict) -> dict:
        """Remove None and empty string values from params."""
        return {
            k: v for k, v in params.items()
            if v is not None and v != ""
        }

    def _get_headers(self, additional_headers: Optional[dict] = None) -> dict:
        """Build request headers."""
        headers = {"accept": "application/json"}
        if self.authorization:
            headers["authorization"] = self.authorization
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def get(
        self,
        endpoint: str,
        params: Optional[dict] = None,
        headers: Optional[dict] = None
    ) -> Any:
        """
        Make a synchronous GET request to the main API.

        Args:
            endpoint: API endpoint (e.g., "/markets")
            params: Query parameters
            headers: Additional headers

        Returns:
            JSON response data
        """
        url = f"{self.base_url}{endpoint}"
        filtered_params = self._filter_params(params or {})
        request_headers = self._get_headers(headers)

        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(url, params=filtered_params, headers=request_headers)

            if not response.is_success:
                raise LighterApiError(
                    f"API request failed: {response.status_code} - {response.text}",
                    response.status_code,
                    endpoint
                )

            return response.json()

    def post(
        self,
        endpoint: str,
        body: dict,
        headers: Optional[dict] = None
    ) -> Any:
        """
        Make a synchronous POST request to the main API.

        Args:
            endpoint: API endpoint
            body: Request body (JSON)
            headers: Additional headers

        Returns:
            JSON response data
        """
        url = f"{self.base_url}{endpoint}"
        request_headers = self._get_headers(headers)
        request_headers["Content-Type"] = "application/json"

        with httpx.Client(timeout=self.timeout) as client:
            response = client.post(url, json=body, headers=request_headers)

            if not response.is_success:
                raise LighterApiError(
                    f"API request failed: {response.status_code} - {response.text}",
                    response.status_code,
                    endpoint
                )

            return response.json()

    def delete(
        self,
        endpoint: str,
        body: dict,
        headers: Optional[dict] = None
    ) -> Any:
        """
        Make a synchronous DELETE request to the main API.

        Args:
            endpoint: API endpoint
            body: Request body (JSON)
            headers: Additional headers

        Returns:
            JSON response data
        """
        url = f"{self.base_url}{endpoint}"
        request_headers = self._get_headers(headers)
        request_headers["Content-Type"] = "application/json"

        with httpx.Client(timeout=self.timeout) as client:
            response = client.request("DELETE", url, json=body, headers=request_headers)

            if not response.is_success:
                raise LighterApiError(
                    f"API request failed: {response.status_code} - {response.text}",
                    response.status_code,
                    endpoint
                )

            return response.json()

    def get_explorer(
        self,
        endpoint: str,
        headers: Optional[dict] = None
    ) -> Any:
        """
        Make a synchronous GET request to the Explorer API.

        Args:
            endpoint: API endpoint (e.g., "/accounts/0x.../positions")
            headers: Additional headers

        Returns:
            JSON response data
        """
        url = f"{self.explorer_url}{endpoint}"
        request_headers = self._get_headers(headers)

        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(url, headers=request_headers)

            if not response.is_success:
                raise LighterApiError(
                    f"Explorer API request failed: {response.status_code} - {response.text}",
                    response.status_code,
                    endpoint
                )

            return response.json()


# Singleton instance for convenience
_client: Optional[LighterClient] = None


def get_client(authorization: Optional[str] = None) -> LighterClient:
    """
    Get or create a LighterClient instance.

    Args:
        authorization: Optional auth token. If provided, creates a new client.

    Returns:
        LighterClient instance
    """
    global _client

    if authorization:
        return LighterClient(authorization=authorization)

    if _client is None:
        _client = LighterClient()

    return _client
