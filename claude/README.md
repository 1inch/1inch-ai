# 1inch Business MCP — Claude Connectors Directory

Assets and submission tracking for the [Anthropic Connectors Directory](https://claude.com/connectors/directory).

## Server details

- **Name:** 1inch Business MCP
- **URL:** `https://api.1inch.com/mcp/protocol`
- **Transport:** Streamable HTTP
- **Auth:** OAuth 2.0 (authorization code flow) for authenticated tools; public tools require no auth
- **Tool annotations:** All 7 tools have `readOnlyHint` or `destructiveHint`

## Tools

| Tool            | Auth     | Annotation         | Description                                |
| --------------- | -------- | ------------------ | ------------------------------------------ |
| `search`        | Public   | `readOnlyHint`     | Search documentation and API reference     |
| `list_examples` | Public   | `readOnlyHint`     | List SDK code examples                     |
| `get_example`   | Public   | `readOnlyHint`     | Get example source code                    |
| `swap`          | Required | `destructiveHint`  | Swap quotes and execution                  |
| `orderbook`     | Required | `destructiveHint`  | Limit order management                     |
| `product_api`   | Required | `destructiveHint`  | Product API proxy (portfolio, prices, etc.) |
| `debug`         | Required | `readOnlyHint`     | Request log lookup                         |

## Links

- [Submission form](http://clau.de/mcp-directory-submission)
- [Submission guide](https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide)
- [Directory policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)
- [FAQ](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)
- [Product documentation](https://business.1inch.com/portal/documentation/ai-integration)

## Legal

- [Privacy Policy](https://business.1inch.com/portal/assets/legal-docs/privacy_policy_20251001.pdf)
- [API Terms of Service](https://business.1inch.com/portal/assets/legal-docs/terms_of_service_public_api_20260218.pdf)
- [Commercial API Terms](https://business.1inch.com/portal/assets/legal-docs/terms_of-service_commercial_api_20251107.pdf)

## Icon

Custom icon URL for the directory (api.1inch.com has no Google-indexed favicon):

`https://business.1inch.com/portal/favicon/favicon-128x128.png`

## Submission status

See [`MARKETPLACE-SUBMISSIONS.md`](../../apps/mcp-service/MARKETPLACE-SUBMISSIONS.md) in the dev-portal repo for the full prefilled form fields and submission checklist.
