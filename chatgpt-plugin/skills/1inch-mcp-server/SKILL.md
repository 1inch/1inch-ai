---
name: 1inch-mcp-server
description: >-
  Connect to the 1inch read-only MCP server for developer documentation search, SDK examples
  and 1inch Aqua shared-liquidity analytics. Use when the user asks about 1inch API endpoints,
  SDK usage, or Aqua maker stats, strategies, activity and volume. This endpoint cannot swap,
  place limit orders or open and close positions.
license: MIT
compatibility: Requires an MCP-capable client with HTTP transport.
metadata:
  mcp_url_production: https://api.1inch.com/mcp/read-only
  documentation: https://business.1inch.com/portal/documentation/ai-integration
---

# 1inch MCP Server (read-only)

Hub skill for the **read-only** 1inch MCP endpoint. The companion `1inch-aqua` skill teaches the
analytics workflows.

## Server URL (production)

`https://api.1inch.com/mcp/read-only` (Streamable HTTP)

No account, OAuth sign-in or API key is needed. Every tool on this endpoint is public.

## Tools

| Tool                            | Purpose                                     |
| ------------------------------- | ------------------------------------------- |
| `search`                        | Search 1inch docs and API reference         |
| `list_examples` / `get_example` | SDK example packages                        |
| `aqua`                          | Aqua shared-liquidity analytics (read-only) |

Full parameters: [references/TOOLS.md](references/TOOLS.md).

## What this endpoint cannot do

It serves analytics and documentation only. There is no tool here that swaps tokens, builds or
places a limit order, opens or closes an Aqua position, quotes a trade, calls other 1inch product
APIs, or pairs a wallet. If the user asks for any of that, tell them plainly that this connection
cannot do it and that the full 1inch MCP server at
`https://api.1inch.com/mcp/protocol` covers it.

Never hand-build calldata, RPC payloads or signed transactions to work around a missing tool. The
user has no way to review or sign anything this connection produces.

## Typical questions

| The user asks                              | Use                                          |
| ------------------------------------------ | -------------------------------------------- |
| "What's the 1inch spot price endpoint?"    | `search`                                     |
| "Show me a 1inch SDK example"              | `list_examples`, then `get_example`          |
| "Which Aqua strategies are open on Base?"  | `aqua` → `list_opened`                        |
| "What are this maker's fees and APY?"      | `aqua` → `maker_stats`                        |
| "Swap 100 USDC for ETH"                    | Not available here — explain and point above |

## Client setup

Add the URL above as a custom MCP server in the client. No headers, no API key.
