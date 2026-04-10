# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the 1inch MCP server or this repository, please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, contact us at: **security@1inch.io**

We will acknowledge receipt within 48 hours and aim to provide a fix or mitigation plan within 7 business days.

## Scope

This policy covers:

- The remote MCP server at `https://api.1inch.com/mcp/protocol`
- The plugin configuration and skill files in this repository
- OAuth authentication flows

## Security Practices

- All traffic is encrypted via HTTPS/TLS.
- OAuth 2.0 authorization code flow for authenticated tools.
- API key authentication (`Authorization: Bearer`) for headless clients.
- Tool annotations (`readOnlyHint`, `destructiveHint`) inform clients of tool behavior.
- No secrets or API keys are stored in this repository.
