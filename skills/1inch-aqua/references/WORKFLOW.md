# 1inch Aqua Workflow — Strategy Analytics & Maker/Taker Transactions

Aqua is shared-liquidity market making: makers **ship** strategies (XYC AMM programs executed by
the Swap VM), takers swap against them through the AquaSwapVMRouter. The **aqua** tool exposes
read-only analytics (no OAuth) and SDK-backed write actions that build transaction calldata
(non-custodial, the user's wallet signs everything). Write access is granted per organization
(OAuth) or, where the anonymous flow is enabled, to unauthenticated users through the WalletConnect
compliance flow described below.

## Read actions (analytics, no OAuth)

1. **maker_stats** — aggregated TVL, fees, APY, strategy counts for a maker:
   `{ "action": "maker_stats", "address": "0xabc...", "chainId": [1, 8453] }`

2. **list_maker_strategies** — paginated strategies for a maker:
   `{ "action": "list_maker_strategies", "address": "0xabc...", "status": ["open"], "limit": 100 }`

3. **strategy_overview** — state, performance, token balances of one strategy:
   `{ "action": "strategy_overview", "chainId": 1, "maker": "0xabc...", "app": "0x4a05...", "strategyHash": "0xaaaa...aaaa" }`

4. **strategy_activity** — on-chain events (opens, closes, swaps):
   `{ "action": "strategy_activity", "chainId": 1, "maker": "0xabc...", "app": "0x4a05...", "strategyHash": "0xaaaa...aaaa", "sort": "desc" }`

5. **strategy_volume** — time-bucketed volume series:
   `{ "action": "strategy_volume", "chainId": 1, "maker": "0xabc...", "app": "0x4a05...", "strategyHash": "0xaaaa...aaaa", "granularity": "1d" }`

6. **list_opened** — system-wide feed of currently open strategies across chains:
   `{ "action": "list_opened", "chainId": [1], "app": "0x4a05...", "limit": 100 }`

For raw HTTP access to any Aqua endpoint (with OAuth), use **product_api** with path prefix
`/aqua/v1.0/strategies/...`.

## Write actions (build calldata; access gated — see below)

The service never holds keys — every returned transaction (`tx: { to, data, value }`) is signed
and sent by the user's wallet. Writes are enabled for every organization; if a call is refused,
the structured error below names the missing prerequisite and the read actions keep working.

**Access paths:**

- **Authenticated (OAuth):** write actions need a bearer token; nothing else is required.
- **Anonymous (no OAuth):** every write call requires a wallet verified through the compliance flow
  below. Using write actions means accepting the 1inch Terms of Use.

### Anonymous write compliance flow (one-time per wallet)

1. **Connect** — `walletconnect { "action": "connect" }`; the user approves the pairing in their
   wallet. Poll `{ "action": "status" }` until `kind` is `"session"`. The status response includes
   a `terms` block showing whether the connected wallet already accepted the Terms of Use.
2. **Accept the Terms of Use** — `walletconnect { "action": "accept_terms" }`. The user signs the
   canonical acceptance message in their wallet (personal_sign, gas-free); the signed consent is
   stored durably. Idempotent — already-accepted wallets return immediately without a prompt.
3. **Write** — call aqua `create_position` / `close_position` / `quote` / `build_swap`. Each call
   verifies: the request region is allowed (geo/sanctions policy on the originating IP), the wallet
   in the request (`maker` / `taker`) belongs to the active WalletConnect session, the wallet passes
   risk screening, and the Terms of Use are accepted. Transactions are sent through the connected
   wallet by default (`execute: false` returns calldata for the verified wallet).

Structured errors tell you which step is missing: `geo_restricted` (region not served — not
retryable), `walletconnect_required` (no active session), `wallet_mismatch` (request wallet not in
the session), `tos_acceptance_required` (run `accept_terms`), `wallet_blocked` (screening rejected
the wallet), or `screening_unavailable` / `terms_unavailable` / `compliance_unavailable`
(temporary — retry shortly; writes fail closed).

### Actions

**`create_position`** — open an XYC AMM strategy. **Two-phase: preview, then confirm.**

Phase 1, no `confirmed`: returns a preview (market price, proposed opening price, range, fee,
amounts, advisories) plus a short-TTL `previewRef` and **no calldata**:

`{ "action": "create_position", "chainId": 1, "maker": "0xabc...", "tokens": [{ "token": "0xA0b8...", "amount": "4000000000" }, { "token": "0xC02a...", "amount": "1000000000000000000" }] }`

Phase 2, after the user reviews: same parameters plus the returned `previewRef` and `openingPrice`,
and `confirmed: true`:

`{ "action": "create_position", "chainId": 1, "maker": "0xabc...", "tokens": [...], "previewRef": "ap_...", "openingPrice": "...", "confirmed": true }`

- Exactly two token legs (`token` + `amount` in the token's smallest units). Native gas tokens are
  rejected.
- Optional `priceRange { rawPriceMin, rawPriceMax }` for concentrated liquidity (see below).
- Optional `feeBpsIn` — integer basis points, **1–500** (0.01%–5%). Default 30 bps.
- Optional `suggestedRanges` for range suggestions.
- Response includes `strategy` (encoded order bytes) and `strategyHash` — keep both.
- The salt is server-generated and cannot be supplied by the caller.

A missing `previewRef` returns `preview_required`; an unknown, expired, already-used or drifted one
returns `stale_preview` and nothing is encoded. Preview and confirm may land on different replicas,
so always pass the `previewRef` back verbatim.

**`create_status`** — progress of an asynchronous confirm (`async: true`, WalletConnect execution
only): `{ "action": "create_status", "sendRef": "..." }`. Returns the phase and every approval hash
so far. Optional otherwise; omit `async` to wait for the transaction hash in the same call.

**`close_position`** — withdraw all liquidity and close a strategy. Requires `confirmed: true`;
closing is permanent and the user's tokens stay in their wallet:

`{ "action": "close_position", "chainId": 1, "strategy": "0x...", "tokens": ["0xA0b8...", "0xC02a..."], "confirmed": true }`

- Provide `strategy` (encoded bytes from `create_position`) **or** `strategyHash`.
- Optional `app` (defaults to the AquaSwapVMRouter for the chain).

**`quote`** — taker-side price check; returns eth_call simulation calldata (never broadcast):

`{ "action": "quote", "chainId": 1, "strategy": "0x...", "tokenIn": "0xA0b8...", "tokenOut": "0xC02a...", "amount": "100000000" }`

- Run `eth_call` with the returned tx and decode `(amountIn uint256, amountOut uint256)`.
- OAuth only. Not executed through WalletConnect under any circumstances.

**`build_swap`** — taker swap against a strategy via the AquaSwapVMRouter. OAuth only:

`{ "action": "build_swap", "chainId": 1, "strategy": "0x...", "tokenIn": "0xA0b8...", "tokenOut": "0xC02a...", "amount": "100000000", "threshold": "49000000000000000" }`

- Optional `taker`, `exactIn` (default true), `threshold` (slippage guard), `deadline` (Unix
  seconds).

### Concentrated liquidity — priceRange semantics

Prices are **raw** fixed-point values: `P = tokenGt / tokenLt` in 1e18, where tokenGt/tokenLt is
the token ordering **by address value** (not by symbol). To convert a human price:

1. Order the two tokens by address (lowercase hex comparison): the higher address is tokenGt.
2. Express the price as tokenGt units per tokenLt unit, adjusting for decimals:
   `rawP = humanPrice * 10^(18 + decimals(tokenGt) - decimals(tokenLt))` when humanPrice is
   quoted as tokenGt/tokenLt (invert first if quoted the other way).
3. Pass `rawPriceMin` / `rawPriceMax` as decimal strings.

Omit `priceRange` entirely for a full-range XYC AMM.

## Typical flows

**Maker (open a strategy):**

1. `create_position` without `confirmed` → review the preview with the user.
2. `create_position` with `previewRef`, `openingPrice` and `confirmed: true` → approve the Aqua
   contract for both tokens if prompted (ERC-20 allowance; funds are pulled just-in-time when swaps
   execute) → the tx is sent.
3. Monitor via `strategy_overview` / `strategy_activity` using `strategyHash`.

**Maker (adjust a price range):** ranges cannot be edited in place. Close and reopen:

1. `close_position` with `confirmed: true` for the current strategy → send tx.
2. `create_position` with the new `priceRange` bounds → preview, then confirm.

**Taker (swap against a strategy):**

1. `list_opened` to find a strategy → 2. `quote` (eth_call, verify output) → 3. approve tokenIn
   for the AquaSwapVMRouter → 4. `build_swap` → send tx.

## WalletConnect execute

When a WalletConnect session is active (see the **walletconnect** tool), `create_position`,
`close_position`, and `build_swap` accept `execute` and default to sending the transaction through
the connected wallet (the user confirms each prompt). Set `execute: false` to get calldata only.
`quote` is never executed — it is a pure simulation payload. On the anonymous path `execute: false`
is rejected: writes there always go through the wallet, so the result never carries unsigned
calldata.

## Supported chains

Write actions are limited to chains where the Aqua contract and AquaSwapVMRouter are deployed;
an unsupported `chainId` returns an error listing the supported IDs.
