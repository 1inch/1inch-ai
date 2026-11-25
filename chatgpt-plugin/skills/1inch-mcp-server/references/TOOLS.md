# 1inch MCP tools — read-only reference

Production endpoint: `https://api.1inch.com/mcp/read-only`.

This endpoint registers four tools. The `aqua` tool is annotated `readOnlyHint`, so a host does not
prompt for confirmation before each call.

## `search`

Search documentation, API references and SDK guides.

| Parameter      | Type    | Required | Notes                      |
| -------------- | ------- | -------- | -------------------------- |
| `query`        | string  | Yes      | Search string              |
| `limit`        | number  | No       | 1-100, page size           |
| `page`         | number  | No       | 1-based pagination         |
| `include_body` | boolean | No       | Include full document body |

## `list_examples`

No parameters. Returns available SDK example identifiers.

## `get_example`

| Parameter | Type   | Required | Notes                            |
| --------- | ------ | -------- | -------------------------------- |
| `name`    | string | Yes      | Example id from `list_examples`  |
| `file`    | string | No       | Specific file path in the example |

## `aqua`

Aqua shared-liquidity analytics. Six read actions, no authentication:

| Action                   | Purpose                                                     |
| ------------------------ | ----------------------------------------------------------- |
| `maker_stats`            | Aggregated TVL, fees, APY and strategy counts for a maker    |
| `list_maker_strategies`  | Paginated strategy list for a maker                          |
| `strategy_overview`      | State, performance and token balances of one strategy        |
| `strategy_activity`      | On-chain events: opens, closes, swaps                        |
| `strategy_volume`        | Time-bucketed volume for one strategy                        |
| `list_opened`            | System-wide feed of currently open strategies                |

See the `1inch-aqua` skill for exact argument shapes.

## Not available on this endpoint

`swap`, `orderbook`, `product_api`, `walletconnect`, `authenticate`, `debug`, and the Aqua write
actions (`create_position`, `close_position`, `quote`, `build_swap`). They exist only on
`https://api.1inch.com/mcp/protocol`.
