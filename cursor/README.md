# 1inch Business MCP — Cursor Plugin

Swap, order & query 1inch APIs from your AI assistant. Search docs, get SDK examples, execute swaps, manage limit orders, and call product APIs — all through natural language in Cursor.

## Features

| Tool            | Auth     | Description                                            |
| --------------- | -------- | ------------------------------------------------------ |
| `search`        | Public   | Search 1inch documentation and API reference           |
| `list_examples` | Public   | List available SDK code examples                       |
| `get_example`   | Public   | Get full source code of an SDK example                 |
| `swap`          | Required | Token swap quotes and execution (Classic, Fusion, cross-chain) |
| `orderbook`     | Required | Build, create, list, and cancel limit orders           |
| `product_api`   | Required | Call any 1inch product API (portfolio, prices, gas, etc.) |
| `debug`         | Required | Look up recent API request logs for troubleshooting    |

## Setup

### From Cursor Marketplace

Search for **1inch Business MCP** in the Cursor Marketplace and click Install.

### Manual setup

Add to `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "1inch-mcp": {
      "url": "https://api.1inch.com/mcp/protocol"
    }
  }
}
```

For authenticated tools, add your API key:

```json
{
  "mcpServers": {
    "1inch-mcp": {
      "url": "https://api.1inch.com/mcp/protocol",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

Get an API key from the [1inch Business Portal](https://business.1inch.com/portal).

## Examples

### Example 1 — Search documentation

**Prompt:** "How do I integrate the 1inch Fusion swap API?"

The `search` tool queries the documentation index and returns matching pages with titles, URLs, and excerpts.

### Example 2 — Get a swap quote

**Prompt:** "Get me a quote to swap 1000 USDC to DAI on Ethereum"

The `swap` tool compares Classic, Fusion, and cross-chain routes and returns the recommended option with expected output, gas estimate, and price impact.

### Example 3 — Check portfolio balances

**Prompt:** "Check portfolio for wallet 0x3A766281Ac78D82449CF58d085e4fbB4A9E3a723"

The `product_api` tool calls the Portfolio endpoint and returns token balances, USD values, and chain breakdown.

### Example 4 — Build a limit order

**Prompt:** "Create a limit order to sell 500 USDC for USDT at 1:1 on Ethereum"

The `orderbook` tool builds EIP-712 typed data for signing. After the user signs, it submits the order.

## Privacy Policy

[1inch Privacy Policy](https://business.1inch.com/portal/assets/legal-docs/privacy_policy_20251001.pdf)

## Support

- [1inch Business Portal Support](https://business.1inch.com/portal/support)
- [Product Documentation](https://business.1inch.com/portal/documentation/ai-integration)

## License

MIT
