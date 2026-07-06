# Playwright MCP browser-agent preflight receipt

Marker: `PLAYWRIGHT_MCP_BROWSER_AGENT_PROOF`

Public target verified for this segment: [`microsoft/playwright-mcp`](https://github.com/microsoft/playwright-mcp) — Playwright MCP server for browser automation agents.

Use this 60-second receipt before a Claude Code, Cursor, Codex, or other tool-enabled agent gets a Playwright MCP browser session against a real app, logged-in workspace, localhost service, or credential-adjacent admin surface.

## Why this buyer segment should care

Browser-agent runs cross the boundary from code suggestions into stateful UI actions. A Playwright MCP session can click destructive controls, read page content, follow links into admin panels, operate against localhost, and accidentally reuse cookies or test credentials. The free lite scanner does not replace browser isolation, but it gives the maintainer a concrete repo/task handoff before the browser tool is connected.

## Copy-paste handoff receipt

```text
PLAYWRIGHT_MCP_BROWSER_AGENT_PROOF
Target app or URL:
Browser/session scope: read-only / test account / localhost / production-like
Allowed browser actions:
Blocked actions: purchase, delete, invite, email/send, deploy, payment, real-account mutation
Repo scan result: Green / Yellow / Red
Files reviewed before browser access:
- package scripts and test/dev server commands
- .mcp.json / MCP config / Claude or Cursor config
- .env.example and secret-adjacent paths
- auth, payment, admin, email, or destructive-flow code paths
Human approval required before:
- submitting forms to real services
- changing billing/account/admin settings
- using stored cookies against production
- running install/deploy/database reset commands
```

## Green / Yellow / Red buy trigger

- **Green:** demo app, disposable test account, no MCP config, no secret-adjacent files, and browser actions are read-only. Use the free scan and normal review.
- **Yellow:** localhost app with package scripts, `.mcp.json`, browser state, auth flows, or form submissions. Write a handoff and use the reusable workflow before giving the agent browser control.
- **Red:** production-like app, logged-in admin/customer account, payment/order/email flows, database mutations, or secret-adjacent config in scope. Stop until a human narrows browser actions and command permissions.

## Buy / skip rule

Run the free scanner first. **Buy the $7 pack** when the result is Yellow/Red and you need the reusable report template, destructive-command hook, demo risky repo, and verification workflow instead of rebuilding the handoff under deadline pressure: <https://payhip.com/b/1nmxV>

Skip the paid pack for now if the Playwright MCP run is isolated to a disposable demo with no repo scripts, credentials, admin controls, or real accounts.
