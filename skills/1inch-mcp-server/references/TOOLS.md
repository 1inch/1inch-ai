# 1inch MCP tools -- reference

Production endpoint: `https://api.1inch.com/mcp/protocol`.

Tools expose **safety hints** to clients: read-only tools use `readOnlyHint`; tools that can change on-chain or remote state use `destructiveHint`.

## Public tools

### `search`

Search documentation, API references, and SDK guides.

| Parameter      | Type    | Required | Notes                      |
| -------------- | ------- | -------- | -------------------------- |
| `query`        | string  | Yes      | Search string              |
| `limit`        | number  | No       | 1-100, page size           |
| `page`         | number  | No       | 1-based pagination         |
| `include_body` | boolean | No       | Include full document body |

### `list_examples`

No parameters. Returns available SDK example identifiers.

### `get_example`

| Parameter | Type   | Required | Notes                                 |
| --------- | ------ | -------- | ------------------------------------- |
| `name`    | string | Yes      | Example id from `list_examples`       |
| `file`    | string | No       | Specific file path inside the example |

## Authenticated tools

Require API key or OAuth session. See [AUTH.md](AUTH.md).

### `swap`

Token swaps (classic, Fusion, cross-chain). Supports quote-only mode (`quoteOnly: true`), execution (returns txs or typed data to sign), and submission (`signedOrder` / `orderHash` for Fusion/cross-chain).

Key parameters: `src`, `dst`, `amount`, `chain`, `from`, optional `quoteOnly`, `preferredType`, `dstChain`, `slippage`, `signedOrder`, `orderHash`.

Prefer the product docs for the full parameter matrix and flows.

### `orderbook`

Limit orders via Orderbook API v4.1. **action** is required: `build` | `create` | `list` | `cancel`.

Typical flow: `build` -> user signs typed data -> `create` with signature.

### `product_api`

Proxy to 1inch product REST APIs.

| Parameter | Type              | Required | Notes                                 |
| --------- | ----------------- | -------- | ------------------------------------- |
| `method`  | `"GET"` or `"POST"` | No     | Default `GET`                         |
| `path`    | string            | Yes      | API path (e.g. portfolio, price, gas) |
| `query`   | object            | No       | Query string map                      |
| `body`    | object            | No       | JSON body for POST                    |

Because the tool can perform writes via POST, it is marked **destructive** at the MCP layer even when `method` is GET.

## Machine-readable API index

For discovering `product_api` paths: `https://business.1inch.com/portal/llms.txt`.
