---
name: 1inch-aqua
description: >-
  Read 1inch Aqua shared-liquidity analytics: maker TVL, fees, APY, strategies, activity and
  volume. Use when the user asks about Aqua maker performance or open strategies. Analytics only:
  this plugin cannot open or close a position.
license: MIT
compatibility: Requires the 1inch MCP server, which registers `aqua` for every caller with no authentication.
---

# Aqua strategy analytics

Use the MCP tool **`aqua`**. Every action below needs no account and no API key.

Full action examples and `priceRange` semantics: [references/WORKFLOW.md](references/WORKFLOW.md).

## Read actions

| Action                  | Answers                                                     |
| ----------------------- | ----------------------------------------------------------- |
| `maker_stats`           | TVL, fees, APY and strategy counts for one maker             |
| `list_maker_strategies` | A maker's strategies, filterable by status                   |
| `strategy_overview`     | State, performance and token balances of one strategy        |
| `strategy_activity`     | On-chain events for one strategy: opens, closes, swaps       |
| `strategy_volume`       | Volume over time for one strategy                            |
| `list_opened`           | Open strategies across chains, the discovery entry point     |

## Not available here

This endpoint cannot create or close a position, quote a trade, or build a swap. It also has no
`walletconnect` tool, so there is no way to sign anything. If the user wants to open or close a
position, say that this connection is analytics-only and that the full 1inch MCP server at
`https://api.1inch.com/mcp/protocol` handles writes.

Do not construct calldata, RPC calls or transactions by hand. The user cannot review or sign
anything this connection produces.
