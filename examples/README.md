# Lighter Exchange Agent Examples

Production-ready examples for using Lighter Exchange agents with Agno.

## 🚀 Quick Start

1. **Install Dependencies**
```bash
pip install agno
pip install -e .  # Install lighter_agno package
```

2. **Setup Configuration**
```bash
cp api_key_config.example.json api_key_config.json
# Edit api_key_config.json with your actual credentials
```

3. **Run Examples**
```bash
python examples/trading_agent_example.py
```

## 🛡️ Security

- **NEVER commit** `api_key_config.json` to git
- Use environment variables in production
- Keep private keys secure and encrypted

## 📊 Available Agents

- **Trading Agent**: Full access (40+ tools, can execute trades)
- **Market Agent**: Read-only market data and analysis  
- **Account Agent**: Portfolio monitoring and risk management

## 🔧 Production Usage

```python
from lighter_agno.agent import create_trading_agent

# Create production agent
agent = create_trading_agent(
    model="gpt-4o",
    include_transactions=True
)

# Use the agent
agent.print_response("Check BTC price", stream=True)
```