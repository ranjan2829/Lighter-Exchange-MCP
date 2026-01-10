/**
 * Lighter Exchange API Client
 * 
 * Handles all HTTP requests to the Lighter Exchange APIs.
 */

import { API_CONFIG } from "../constants.js";
import type { ApiRequestParams, ApiHeaders } from "../types.js";

/**
 * API Client for Lighter Exchange
 */
export class LighterApiClient {
  private baseUrl: string;
  private explorerUrl: string;

  constructor(
    baseUrl: string = API_CONFIG.BASE_URL,
    explorerUrl: string = API_CONFIG.EXPLORER_URL
  ) {
    this.baseUrl = baseUrl;
    this.explorerUrl = explorerUrl;
  }

  /**
   * Build URL with query parameters
   */
  private buildUrl(baseUrl: string, endpoint: string, params: ApiRequestParams): URL {
    const url = new URL(`${baseUrl}${endpoint}`);
    const filteredParams: Record<string, string> = {};

    for (const [key, value] of Object.entries(params)) {
      if (value !== undefined && value !== null && value !== "") {
        filteredParams[key] = String(value);
      }
    }

    url.search = new URLSearchParams(filteredParams).toString();
    return url;
  }

  /**
   * Make a GET request to the main API
   */
  async get<T = unknown>(
    endpoint: string,
    params: ApiRequestParams = {},
    headers: ApiHeaders = {}
  ): Promise<T> {
    const url = this.buildUrl(this.baseUrl, endpoint, params);

    const response = await fetch(url.toString(), {
      method: "GET",
      headers: {
        accept: "application/json",
        ...headers,
      },
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new LighterApiError(
        `API request failed: ${response.status} - ${errorText}`,
        response.status,
        endpoint
      );
    }

    return response.json() as Promise<T>;
  }

  /**
   * Make a POST request to the main API
   */
  async post<T = unknown>(
    endpoint: string,
    body: Record<string, unknown>,
    headers: ApiHeaders = {}
  ): Promise<T> {
    const url = new URL(`${this.baseUrl}${endpoint}`);

    const response = await fetch(url.toString(), {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        accept: "application/json",
        ...headers,
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new LighterApiError(
        `API request failed: ${response.status} - ${errorText}`,
        response.status,
        endpoint
      );
    }

    return response.json() as Promise<T>;
  }

  /**
   * Make a DELETE request to the main API
   */
  async delete<T = unknown>(
    endpoint: string,
    body: Record<string, unknown>,
    headers: ApiHeaders = {}
  ): Promise<T> {
    const url = new URL(`${this.baseUrl}${endpoint}`);

    const response = await fetch(url.toString(), {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        accept: "application/json",
        ...headers,
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new LighterApiError(
        `API request failed: ${response.status} - ${errorText}`,
        response.status,
        endpoint
      );
    }

    return response.json() as Promise<T>;
  }

  /**
   * Make a GET request to the Explorer API
   */
  async getExplorer<T = unknown>(
    endpoint: string,
    headers: ApiHeaders = {}
  ): Promise<T> {
    const url = new URL(`${this.explorerUrl}${endpoint}`);

    const response = await fetch(url.toString(), {
      method: "GET",
      headers: {
        accept: "application/json",
        ...headers,
      },
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new LighterApiError(
        `Explorer API request failed: ${response.status} - ${errorText}`,
        response.status,
        endpoint
      );
    }

    return response.json() as Promise<T>;
  }
}

/**
 * Custom error class for Lighter API errors
 */
export class LighterApiError extends Error {
  public statusCode: number;
  public endpoint: string;

  constructor(message: string, statusCode: number, endpoint: string) {
    super(message);
    this.name = "LighterApiError";
    this.statusCode = statusCode;
    this.endpoint = endpoint;
  }
}

// Export singleton instance
export const apiClient = new LighterApiClient();
