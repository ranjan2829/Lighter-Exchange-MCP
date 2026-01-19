#!/usr/bin/env python3
"""
Lighter Exchange Trading Agent Example

Production-ready example showing how to use the Lighter Exchange MCP toolkit.
This demonstrates the proper way to create and use trading agents.
"""

import os
from pathlib import Path

try:
    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
except ImportError:
    print("❌ Install agno: pip install agno")
    exit(1)

from lighter_agno.agent import (
    create_trading_agent,
    create_market_agent, 
    create_account_agent
)


def load_config():
    """Load configuration from environment or config file."""
    config_path = Path("api_key_config.json")
    if not config_path.exists():
        print("❌ Create api_key_config.json from api_key_config.example.json")
        print("❌ Add your actual API keys and account details")
        exit(1)
    
    import json
    with open(config_path) as f:
        return json.load(f)


def main():
    """Example usage of Lighter Exchange agents."""
    # Load configuration
    config = load_config()
    
    print("🚀 Lighter Exchange Trading Agent Demo\n")
    
    # Create different types of agents
    try:
        # Full trading agent (read + write)
        trading_agent = create_trading_agent(
            model="gpt-4o",
            include_transactions=True  # Enable trading
        )
        
        # Market analysis agent (read-only)
        market_agent = create_market_agent(model="gpt-4o")
        
        # Account monitoring agent
        account_agent = create_account_agent(model="gpt-4o")
        
        print("✅ All agents created successfully!\n")
        
        # Example interactions
        print("📊 Market Analysis:")
        market_agent.print_response(
            "What are the top 3 markets by volume?", 
            stream=True
        )
        
        print("\n" + "="*50 + "\n")
        
        print("💰 Account Status:")
        account_agent.print_response(
            f"Show me account {config['accountIndex']} positions and PnL",
            stream=True
        )
        
        print("\n" + "="*50 + "\n")
        
        print("⚡ Trading Agent:")
        trading_agent.print_response(
            "What's the current BTC-PERP price and funding rate?",
            stream=True
        )
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
