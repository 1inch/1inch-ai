#!/usr/bin/env python3
"""Validate the ChatGPT plugin manifests against the published Agent Plugins schemas.

Run before packaging:  python3 chatgpt-plugin/validate-manifests.py

Both manifests are validated against the JSON Schemas they declare in their own `$schema`
field, which is the same document a host reads. `mcp.json` is strict about its server
objects — `additionalProperties: false` on every variant — so a single unrecognised key
there silently invalidates the whole file, and a host that rejects the file lists no tools
while the skills still load. That is the failure this check exists to catch.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

try:
    import jsonschema
except ImportError:  # pragma: no cover - dependency guidance, not a validation path
    sys.exit("jsonschema is required: pip install jsonschema")

ROOT = Path(__file__).resolve().parent
MANIFESTS = ("plugin.json", "mcp.json")


def load_schema(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as response:
        return json.load(response)


def main() -> int:
    schemas: dict[str, dict] = {}
    failed = False

    for name in MANIFESTS:
        path = ROOT / name
        if not path.is_file():
            print(f"FAIL {name}: missing")
            failed = True
            continue

        document = json.loads(path.read_text())
        url = document.get("$schema")
        if not isinstance(url, str):
            print(f"FAIL {name}: no $schema declared")
            failed = True
            continue

        if url not in schemas:
            try:
                schemas[url] = load_schema(url)
            except Exception as exc:  # network failure is a real failure, not a skip
                print(f"FAIL {name}: could not fetch {url} ({exc})")
                failed = True
                continue

        errors = sorted(
            jsonschema.Draft202012Validator(schemas[url]).iter_errors(document),
            key=lambda error: list(error.path),
        )
        if errors:
            failed = True
            print(f"FAIL {name}: {len(errors)} schema error(s)")
            for error in errors:
                location = "/".join(str(part) for part in error.path) or "(root)"
                print(f"  {location}: {error.message}")
        else:
            print(f"OK   {name}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
