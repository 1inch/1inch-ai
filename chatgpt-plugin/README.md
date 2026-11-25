# 1inch — ChatGPT plugin

A ChatGPT plugin for learning about 1inch and reading Aqua analytics. It answers questions about
1inch APIs and shows maker stats, strategies and activity. It is read-only by design: it cannot
prepare or send a transaction.

| | |
| --- | --- |
| Best for | Questions about 1inch APIs, and Aqua analytics |
| Not for | Swaps, limit orders, or opening and closing positions |
| Account | None required |

## What it can answer

- How a particular 1inch API or SDK works.
- SDK example code for the common flows.
- Aqua maker stats: TVL, fees, APY.
- Which Aqua strategies are open, and how they are performing.

If you ask for a swap, a limit order or a position change, it says that this plugin cannot do that
and points you to the full 1inch MCP server instead. That is deliberate, not a limitation to work
around.

## Installing

This plugin is distributed as a package in this repository. To install it in ChatGPT:

1. Validate the manifests: `python3 validate-manifests.py` (needs `jsonschema`).
2. Create the ZIP: `cd chatgpt-plugin && zip -r ../1inch-plugin.zip .`
3. In ChatGPT, open **Plugins**, choose **Upload new or existing plugin**, and select the ZIP.

`plugin.json` must sit at the ZIP root, so run `zip` from inside this directory rather than from the
repository root.

For a personal or workspace custom connector, add the read-only 1inch MCP server URL and leave
authentication off.

## Layout

```
chatgpt-plugin/
  plugin.json              plugin manifest and listing metadata
  mcp.json                 the read-only MCP server connection
  validate-manifests.py    checks both files against their published schemas
  assets/logo.svg
  skills/                  instructions the assistant follows for docs and Aqua questions
```

Skills live in `skills/`. They are self-contained rather than shared with the other plugins in this
repository, because those cover workflows this plugin cannot perform.
