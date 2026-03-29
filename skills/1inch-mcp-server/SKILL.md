---
name: 1inch-mcp-server
description: >-
  Connect to the 1inch Dev Portal MCP server for documentation search, SDK examples, token swaps,
  limit orders, and authenticated product API access. Use when the user asks about 1inch integration,
  DeFi swaps, limit orders, API keys, or blockchain development with 1inch.
license: MIT
compatibility: Requires an MCP-capable client with HTTP transport (preferred) or stdio plus Node.js 18+ for supergateway bridging.
metadata:
  mcp_url_production: https://api.1inch.com/mcp/protocol
  documentation: https://business.1inch.com/portal/documentation/ai-integration/mcp-server
---

# 1inch Dev Portal MCP Server

This skill teaches agents how to wire and use the **1inch MCP server** so users get docs, examples, and (with auth) swaps and APIs without re-explaining setup each session.

## When to use this skill

- The user wants to integrate 1inch (swap, orderbook, portfolio, APIs).
- The user mentions MCP, Cursor, Claude, or "connect to 1inch APIs from the IDE."
- You need the canonical **server URL**, **tool list**, or **auth** patterns for 1inch Business.

## Server URL (production)

`https://api.1inch.com/mcp/protocol` (Streamable HTTP)

For local development against a running `mcp-service`, use the URL your team documents (typically `http://localhost:<port>/mcp/protocol`).

## Client setup (summary)

| Client                           | Transport | Config pattern                                                                                                             |
| -------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| Cursor                           | HTTP      | `.cursor/mcp.json` -> `"url": "https://api.1inch.com/mcp/protocol"`                                                       |
| VS Code Copilot                  | HTTP      | `.vscode/mcp.json` -> `type: "http"`, same URL                                                                             |
| Claude Code / Codex / Gemini CLI | HTTP      | CLI `mcp add` with `--transport http` and the URL                                                                          |
| Claude Desktop                   | stdio     | Launch `npx -y supergateway --streamableHttp <URL> --outputTransport stdio` (see [references/AUTH.md](references/AUTH.md)) |

Prefer **HTTP** when the client supports it; use **supergateway** only for stdio-only clients.

## Tools overview

| Tool            | Auth          | Purpose                               |
| --------------- | ------------- | ------------------------------------- |
| `search`        | Public        | Search 1inch docs and API reference   |
| `list_examples` | Public        | List SDK example packages             |
| `get_example`   | Public        | Fetch example source files            |
| `swap`          | Authenticated | Quotes and swap execution flows       |
| `orderbook`     | Authenticated | Build/create/list/cancel limit orders |
| `product_api`   | Authenticated | Call other 1inch product APIs         |

Full parameters: [references/TOOLS.md](references/TOOLS.md).

## Authentication

- **API key:** `Authorization: Bearer <key>` on the HTTP transport where the client allows headers.
- **OAuth:** Supported by the server for interactive login when no API key is set.

Details and client-specific snippets: [references/AUTH.md](references/AUTH.md).

## Example prompts (for the user)

- "Search 1inch docs for how to set slippage on Base."
- "Show the TypeScript swap example for Fusion on Ethereum."
- "Quote swapping 100 USDC to ETH on Arbitrum" (requires auth for execution tools).

## Progressive disclosure

- Load [references/TOOLS.md](references/TOOLS.md) when you need exact tool arguments or edge cases.
- Load [references/AUTH.md](references/AUTH.md) when configuring headers, OAuth, or Claude Desktop bridging.

## Legal

Use of the MCP server is subject to 1inch Business Portal terms linked from the [product documentation](https://business.1inch.com/portal/documentation/ai-integration/mcp-server).
