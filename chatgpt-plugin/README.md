# 1inch Analytics — read-only ChatGPT plugin

A ChatGPT plugin over the **read-only** 1inch MCP endpoint. It answers questions about 1inch APIs and
reads 1inch Aqua shared-liquidity analytics. It cannot prepare or send a transaction.

| | |
| --- | --- |
| Endpoint | `https://api.1inch.com/mcp/read-only` |
| Authentication | none — every tool on this endpoint is public |
| Tools | `search`, `list_examples`, `get_example`, `aqua` |

## Why a separate plugin

The route registers four tools and nothing else. `swap`, `orderbook`, `product_api`, `walletconnect`,
`authenticate`, `debug` and the Aqua write actions do not exist on it, so no host-side toggle can
expose them. That restriction lives on the server (`apps/mcp-service` in
[dev-portal](https://github.com/1inch/dev-portal)), not in this package — `mcp.json` cannot filter
tools, which is exactly why the endpoint does.

Keeping this separate from the main `1inch-mcp` plugin matters for the skills as much as the tools:
the main plugin's skills teach `swap`, `orderbook` and `product_api` recipes, and bundling those with
this endpoint would instruct the assistant to call tools that are not there.

## Layout

```
chatgpt-plugin/
  plugin.json                          manifest, OpenAI metadata under extensions.com.openai
  mcp.json                             the read-only server connection
  assets/logo.svg
  skills/
    1inch-mcp-server/SKILL.md          hub: endpoint, the four tools, what is not available
    1inch-mcp-server/references/TOOLS.md
    1inch-aqua/SKILL.md                Aqua analytics, read actions only
    1inch-aqua/references/WORKFLOW.md  exact argument shapes and how to read the results
```

## Installing (workspace / custom connector)

The package is not published to the plugin directory. Connect it directly:

1. OpenAI requires a ZIP for a plug-in upload. From the repository root:
   `cd chatgpt-plugin && zip -r ../1inch-read-only.zip .`
2. In ChatGPT, open **Plugins**, then **Upload new or existing plugin**, and select the ZIP.
3. Complete domain verification for `api.1inch.com` if prompted.

For a personal or workspace custom connector, add `https://api.1inch.com/mcp/read-only` as the server
URL with authentication set to none.

## Updating the tool surface

`mcp.json` declares the server; it cannot add or remove tools. Adding a tool here means changing the
endpoint, which is a `dev-portal` change. Adding a *skill* is a change to this directory only.

After any change, refresh the app in ChatGPT so it re-reads the tool list and instructions — a
conversation already open keeps the list it started with.
