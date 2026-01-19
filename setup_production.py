#!/usr/bin/env python3
"""
Production Setup Script for Lighter Exchange MCP

This script helps users set up the production environment correctly.
"""

import os
import json
import sys
from pathlib import Path


def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import agno
        print("✅ agno package installed")
    except ImportError:
        print("❌ agno package not found")
        print("   Install with: pip install agno")
        return False
    
    try:
        import lighter_agno
        print("✅ lighter_agno package available")
    except ImportError:
        print("❌ lighter_agno package not found")
        print("   Install with: pip install -e .")
        return False
    
    return True


def setup_config():
    """Setup configuration file from template."""
    example_path = Path("api_key_config.example.json")
    config_path = Path("api_key_config.json")
    
    if not example_path.exists():
        print("❌ api_key_config.example.json not found")
        return False
    
    if config_path.exists():
        print("✅ api_key_config.json already exists")
        return True
    
    # Copy template
    with open(example_path) as f:
        config = json.load(f)
    
    print("📝 Creating api_key_config.json from template...")
    print("⚠️  EDIT THIS FILE WITH YOUR ACTUAL CREDENTIALS")
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Created {config_path}")
    print("🔒 This file is git-ignored for security")
    return True


def verify_security():
    """Verify security setup."""
    gitignore_path = Path(".gitignore")
    
    if not gitignore_path.exists():
        print("⚠️  No .gitignore found")
        return False
    
    with open(gitignore_path) as f:
        gitignore_content = f.read()
    
    if "api_key_config.json" in gitignore_content:
        print("✅ api_key_config.json is git-ignored")
        return True
    else:
        print("❌ api_key_config.json NOT in .gitignore")
        return False


def main():
    """Main setup function."""
    print("🚀 Lighter Exchange MCP Production Setup\\n")
    
    # Check dependencies
    if not check_dependencies():
        print("\\n❌ Setup failed: Missing dependencies")
        sys.exit(1)
    
    # Setup config
    if not setup_config():
        print("\\n❌ Setup failed: Config setup error")
        sys.exit(1)
    
    # Verify security
    if not verify_security():
        print("\\n❌ Setup failed: Security verification failed")
        sys.exit(1)
    
    print("\\n🎉 Production setup complete!")
    print("\\nNext steps:")
    print("1. Edit api_key_config.json with your Lighter Exchange credentials")
    print("2. Run: python examples/trading_agent_example.py")
    print("\\n⚠️  NEVER commit api_key_config.json to git!")


if __name__ == "__main__":
    main()