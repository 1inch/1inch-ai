# 1inch AI

Public distribution hub for 1inch AI integrations — [Agent Skills](https://agentskills.io/specification), [MCP](https://modelcontextprotocol.io/) server configs, and marketplace listings for Claude, Cursor, and other AI assistants.

## MCP server

The 1inch MCP server is hosted at:

```
https://api.1inch.com/mcp/protocol
```

It provides tools for documentation search, SDK examples, token swaps, limit orders, authenticated product API access, WalletConnect, Aqua analytics, and (when enabled) org-scoped log lookup. Full documentation: [1inch MCP Server](https://business.1inch.com/portal/documentation/ai-integration).

## Quick setup

### Cursor

Create `.cursor/mcp.json` in your project:

```json
{
  "mcpServers": {
    "1inch-mcp": {
      "url": "https://api.1inch.com/mcp/protocol"
    }
  }
}
```

### Claude Code

```bash
claude mcp add --transport http --scope user 1inch-mcp https://api.1inch.com/mcp/protocol
```

### VS Code (Copilot)

Create `.vscode/mcp.json` in your project:

```json
{
  "servers": {
    "1inch-mcp": {
      "type": "http",
      "url": "https://api.1inch.com/mcp/protocol"
    }
  }
}
```

### Other clients

See the [full setup guide](https://business.1inch.com/portal/documentation/ai-integration/supported-clients) for Claude Desktop, Windsurf, JetBrains, OpenAI Codex, Gemini CLI, ChatGPT, Grok, and more.

## Agent Skills

Install the 1inch skills so your AI agent knows the server URL, auth patterns, and exact `product_api` call recipes:

```bash
npx skills add 1inch/1inch-ai
```

| Skill                                                          | Role                                                         |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| [`1inch-mcp-server`](skills/1inch-mcp-server/SKILL.md)         | Hub — MCP URL, auth, client setup, tool overview             |
| [`1inch-swap`](skills/1inch-swap/SKILL.md)                     | Classic / Fusion / cross-chain via `swap`                    |
| [`1inch-orderbook`](skills/1inch-orderbook/SKILL.md)           | Limit orders via `orderbook`                                 |
| [`1inch-wallet-data`](skills/1inch-wallet-data/SKILL.md)       | Portfolio, balances, history, NFTs, tokens via `product_api` |
| [`1inch-market-data`](skills/1inch-market-data/SKILL.md)       | Spot prices, gas price, charts via `product_api`             |
| [`1inch-infrastructure`](skills/1inch-infrastructure/SKILL.md) | Web3 RPC, tx gateway, domains via `product_api`              |
| [`1inch-walletconnect`](skills/1inch-walletconnect/SKILL.md)   | Non-custodial WalletConnect pairing                          |
| [`1inch-aqua`](skills/1inch-aqua/SKILL.md)                     | Aqua strategy analytics                                      |
| [`1inch-debug`](skills/1inch-debug/SKILL.md)                   | Org-scoped request log lookup                                |

Skills load on demand (~30–50 tokens until invoked). Prefer a domain skill for concrete tasks — e.g. gas price → `1inch-market-data` teaches `GET /gas-price/v1.6/{chainId}`.

See the [Agent Skills specification](https://agentskills.io/specification).

## Repository structure

```
.cursor-plugin/          Cursor Marketplace plugin manifest
.claude-plugin/          Claude Code plugin manifest
skills/                  Agent Skills (agentskills.io)
  1inch-mcp-server/      Hub skill (SKILL.md + AUTH/TOOLS references)
  1inch-swap/            Swap workflows
  1inch-orderbook/       Limit orders
  1inch-wallet-data/     product_api recipes (Wallet & Data)
  1inch-market-data/     product_api recipes (Market Data)
  1inch-infrastructure/  product_api recipes (Infrastructure)
  1inch-walletconnect/   WalletConnect
  1inch-aqua/            Aqua analytics
  1inch-debug/           Request log lookup
cursor/                  Cursor plugin README and docs
claude/                  Claude Connectors Directory pointer
assets/                  Logo and branding
mcp.json                 MCP server configuration (remote URL)
server.json              Official MCP Registry pointer
SECURITY.md              Security policy and vulnerability reporting
```

## Authentication

Public tools (`search`, `list_examples`, `get_example`, and read-only `aqua` when enabled) work without authentication. Authenticated tools (`swap`, `orderbook`, `product_api`, and optional `debug`) require an API key or OAuth login. See the [MCP product docs](https://business.1inch.com/portal/documentation/ai-integration/mcp-server).

Get an API key from the [1inch Business Portal](https://business.1inch.com/portal).

## Links

- [Product documentation](https://business.1inch.com/portal/documentation/ai-integration)
- [AI Skills](https://business.1inch.com/portal/documentation/ai-integration/ai-skills)
- [Agent Skills specification](https://agentskills.io/specification)
- [Machine-readable API index](https://business.1inch.com/portal/llms.txt)

## License

MIT
