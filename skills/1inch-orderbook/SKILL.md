---
name: 1inch-orderbook
description: >-
  Build, sign, create, list, and cancel limit orders via the 1inch MCP `orderbook` tool
  (Limit Order Protocol v4.1). Use when the user wants buy/sell at a target price,
  maker orders, or partial fills.
license: MIT
compatibility: Requires 1inch MCP server with authentication.
---

# 1inch Orderbook (limit orders)

Use the authenticated MCP tool **`orderbook`**. Required field: `action` — `build` | `create` | `list` | `cancel`.

## Flow

1. **build** — server returns EIP-712 `typedData`, `orderHash`, `orderData`. Amounts in smallest units; assets as address or symbol.
2. **sign** — `eth_signTypedData_v4` with the maker wallet.
3. **create** — submit `orderHash`, `signature`, `orderData`.
4. **list** — `listMode`: `by_maker` | `by_hash` | `all`.
5. **cancel** — loads on-chain cancel guidance (no HTTP cancel).

If build returns an `approval` block, broadcast `approveTx` first (native gas), then sign.

Full playbook (parameters, approval & gas, list modes, chain IDs): [references/WORKFLOW.md](references/WORKFLOW.md). Same content is served live as MCP resource `file://1inch-mcp/guides/orderbook-workflow` for clients that read resources.

## Example prompts

- "Build a limit order to sell 1 WETH for USDC on Ethereum"
- "List my open limit orders for 0x…"
