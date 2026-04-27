# 1inch AI

Public distribution hub for 1inch AI integrations — [Agent Skills](https://agentskills.io/specification), [MCP](https://modelcontextprotocol.io/) server configs, and marketplace listings for Claude, Cursor, and other AI assistants.

## MCP server

The 1inch MCP server is hosted at:

```
https://api.1inch.com/mcp/protocol
```

It provides tools for documentation search, SDK examples, token swaps, limit orders, and authenticated product API access. Full documentation: [1inch MCP Server](https://business.1inch.com/portal/documentation/ai-integration/ecosystem).

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

See the [full setup guide](https://business.1inch.com/portal/documentation/ai-integration/ecosystem) for Claude Desktop, Windsurf, JetBrains, OpenAI Codex, Gemini CLI, and more.

## Agent Skills

Install the 1inch MCP skill so your AI agent knows the server URL, tools, and auth patterns automatically:

```bash
npx skills add 1inch/1inch-ai
```

The skill lives in [`skills/1inch-mcp-server/`](skills/1inch-mcp-server/SKILL.md). See the [Agent Skills specification](https://agentskills.io/specification) for how skills work.

## Repository structure

```
.cursor-plugin/          Cursor Marketplace plugin manifest
.claude-plugin/          Claude Code plugin manifest
skills/                  Agent Skills (agentskills.io)
  1inch-mcp-server/      MCP server skill (SKILL.md + references)
cursor/                  Cursor plugin README and docs
claude/                  Claude Connectors Directory pointer
assets/                  Logo and branding
mcp.json                 MCP server configuration (remote URL)
SECURITY.md              Security policy and vulnerability reporting
```

## Authentication

Public tools (`search`, `list_examples`, `get_example`) work without authentication. Authenticated tools (`swap`, `orderbook`, `product_api`) require an API key or OAuth login. The optional `debug` tool (organization-scoped log lookup) appears only when the deployment registers it; it uses the same authentication model as other protected tools. See the [MCP product docs](https://business.1inch.com/portal/documentation/ai-integration/ecosystem).

Get an API key from the [1inch Business Portal](https://business.1inch.com/portal).

## Links

- [Product documentation](https://business.1inch.com/portal/documentation/ai-integration/ecosystem)
- [Agent Skills specification](https://agentskills.io/specification)
- [Machine-readable API index](https://business.1inch.com/portal/llms.txt)

## License

MIT
