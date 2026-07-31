# Market Data — product_api recipes

Use the authenticated MCP tool `product_api`. If a path 404s, fetch the live `api-index` resource (`file://1inch-mcp/guides/api-index`) or call `search`, then retry.

Source of truth in the monorepo: `apps/mcp-service/src/mcp/resources/product-api-recipes.ts`.

## Spot Price

- **Path prefix:** `/price/v1.1/{chainId}/...`
- **Example:** `product_api({ method: "GET", path: "/price/v1.1/1/0xTokenAddress", query: { currency: "USD" } })`
- **Gotcha:** Prices in native token WEI unless `currency` param set (e.g. `currency=USD`)

## Gas Price

- **Path prefix:** `/gas-price/v1.6/{chainId}`
- **Example:** `product_api({ method: "GET", path: "/gas-price/v1.6/1" })`
- **Gotcha:** Compact response, ready for agent use

## Charts

- **Path prefix:** `/charts/...`
- **Example:** `product_api({ method: "GET", path: "/charts/v1.0/chart/aggregated/candle/0xToken/1", query: { range: "1d" } })`
- **Gotcha:** Prefer `search` for exact Charts paths and candle params; check live api-index / llms.txt
