---
name: 1inch-walletconnect
description: >-
  Pair an EVM or Solana wallet via WalletConnect (non-custodial) using the 1inch
  MCP `walletconnect` tool, then sign messages or send transactions. Use when
  the user wants to connect a wallet, scan a QR, or execute with WalletConnect.
license: MIT
compatibility: Requires 1inch MCP server with walletconnect tool registered (WALLETCONNECT_PROJECT_ID).
---

# WalletConnect

Use the MCP tool **`walletconnect`**. The server never holds private keys — the user approves every request in their wallet.

## Actions

- `connect` — returns pairing QR resource + `wc:` URI (+ mobile deeplinks). Set `pairingTarget`: `eth` | `solana` | `both`.
- `status` — poll until connected (pending is success while waiting).
- `sign` / `send_transaction` — after session is active.
- `accept_terms` — when required for anonymous write flows.
- `disconnect` — end session.

Swap/orderbook may accept `execute: true` when a WC session is active.

Pairing QR resource template: `file://1inch-mcp/walletconnect/pairing-qr/{token}`.

## Tips

- Do not call `connect` again just to refresh while pending with the same `pairingTarget`.
- Many mobile wallets reject EVM+Solana together — start with one namespace.
- QR expires ~10 minutes.
