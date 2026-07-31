---
name: 1inch-swap
description: >-
  Quote and execute token swaps via the 1inch MCP `swap` tool: Classic (DEX aggregation),
  Fusion (gasless intent), and Fusion+/cross-chain. Use when the user wants best rate,
  gasless swap, bridge-less cross-chain, or quote comparison.
license: MIT
compatibility: Requires 1inch MCP server (see 1inch-mcp-server skill) with auth for execution.
---

# 1inch Swap

Use the authenticated MCP tool **`swap`**. Do not hand-build calldata for normal flows.

## Modes

- **Classic** — on-chain via aggregation router; user pays gas. `preferredType: "classic"`.
- **Fusion** — gasless intent; resolvers fill. `preferredType: "fusion"`.
- **Cross-chain** — set `dstChain`; `preferredType: "crosschain"`.

## Approaches

1. **Shortcut:** call `swap` with `src`, `dst`, `amount`, `chain`, `from`. Omit `preferredType` to let the server recommend, or set it explicitly.
2. **Full flow:** `quoteOnly: true` → compare quotes / `recommended` → execute with chosen `preferredType`.
3. **Fusion/cross-chain submit:** after signing typed data, call again with `signedOrder` + `orderHash`.

## Guides (MCP resources)

| Flow        | Resource URI                              |
| ----------- | ----------------------------------------- |
| Overview    | `file://1inch-mcp/guides/swap-workflow`   |
| Quote       | `file://1inch-mcp/guides/swap/quote`      |
| Classic     | `file://1inch-mcp/guides/swap/classic`    |
| Fusion      | `file://1inch-mcp/guides/swap/fusion`     |
| Cross-chain | `file://1inch-mcp/guides/swap/crosschain` |

With WalletConnect active, optional `execute: true` can send/sign in one step.

## Example prompts

- "Quote swapping 100 USDC to ETH on Base"
- "Swap 0.5 ETH to USDT on Arbitrum with Fusion"
- "Swap 100 USDC from Ethereum to Polygon"
