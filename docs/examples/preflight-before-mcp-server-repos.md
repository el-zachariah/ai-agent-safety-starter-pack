# MCP server repo preflight proof

Named segment: teams using or publishing MCP server repositories like [`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) before connecting those servers to Claude Code, Cursor, Codex, or another local agent harness.

Public evidence checked in this pulse: `modelcontextprotocol/servers` is a live GitHub repository with 88073 stars, updated `2026-07-05T11:10:04Z`, and it sits in the Model Context Protocol ecosystem.

## Why this matters before checkout

MCP server repos are exactly where a "quick agent experiment" can quietly become production-risky: server launch commands, package scripts, Dockerfiles, environment variables, OAuth/API token notes, and broad filesystem/network capabilities can all be inherited by an agent once the server is wired into a local client.

Run the free `/agent-preflight` check before enabling or publishing the server. It gives the maintainer or buyer a receipt they can paste into a PR, release checklist, or handoff note.

## Free receipt example

```text
Agent preflight: YELLOW
Segment: MCP server repository
Risk buckets:
- mcp-config: server launch command + client config present
- secrets: API/token/env-var setup documented
- shell: package scripts or Docker entrypoints execute local commands
- handoff: no copy-paste reviewer receipt found yet
Next: add an explicit preflight receipt before connecting this server to an agent client.
```

## Buy trigger

Buy the $7 AI Agent Safety Starter Pack only when the free receipt is Yellow/Red or when the MCP server will be used by a real repo agent. The paid pack gives the owner-facing checklist, handoff prompt, command hook pattern, and reviewer receipt template that turn the scan into a repeatable approval gate.

Product: https://payhip.com/b/1nmxV

Skip buying for Green toy repos with no secrets, no filesystem/network access, and no real agent handoff.
