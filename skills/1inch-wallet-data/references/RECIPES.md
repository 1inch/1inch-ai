# Wallet & Data — product_api recipes

Use the authenticated MCP tool `product_api`. If a path 404s, fetch the live `api-index` resource (`file://1inch-mcp/guides/api-index`) or call `search`, then retry.

Source of truth in the monorepo: `apps/mcp-service/src/mcp/resources/product-api-recipes.ts`.

## Portfolio

- **Path prefix:** `/portfolio/portfolio/v5.0/...`
- **Example:** `product_api({ method: "GET", path: "/portfolio/portfolio/v5.0/overview/current_value", query: { addresses: "0x...", chain_id: "1" } })`
- **Gotcha:** Gateway strips the first `/portfolio`; backend OpenAPI paths are `/portfolio/v5.0/...`. Full host: https://api.1inch.com

## Balance

- **Path prefix:** `/balance/v1.2/{chainId}/...`
- **Example:** `product_api({ method: "GET", path: "/balance/v1.2/1/balances/0xYourWallet" })`
- **Gotcha:** Response includes zero balances; filter client-side

## Token

- **Path prefix:** `/token/v1.2/{chainId}/...`
- **Example:** `product_api({ method: "GET", path: "/token/v1.2/1/search", query: { query: "USDC" } })`
- **Gotcha:** Full list is huge; prefer `/search?query=...`

## Token Details

- **Path prefix:** `/token-details/v1.0/...`
- **Example:** `product_api({ method: "GET", path: "/token-details/v1.0/1/details/0xTokenAddress" })`
- **Gotcha:** Native ETH pseudo-address (`0xeeee...eeee`) NOT supported; use WETH

## History

- **Path prefix:** `/history/v2.0/...`
- **Example:** `product_api({ method: "GET", path: "/history/v2.0/history/0xYourWallet/events", query: { chainId: "1" } })`
- **Gotcha:** Prefer `search` if unsure of exact History path version; check live api-index / llms.txt

## NFT

- **Path prefix:** `/nft/v1/...`
- **Example:** `product_api({ method: "GET", path: "/nft/v1/byaddress", query: { address: "0xYourWallet", chainIds: "1" } })`
- **Gotcha:** Prefer `search` if unsure of exact NFT path; check live api-index / llms.txt
