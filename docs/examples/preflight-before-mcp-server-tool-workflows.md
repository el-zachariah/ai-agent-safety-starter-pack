# Model Context Protocol server preflight proof

**Named buyer segment:** teams using [`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) or MCP-style server/tool workflows before agent clients receive repository context, filesystem access, browser/API tools, package scripts, workflow edits, credentialed connectors, or secret-adjacent configuration.

**Public target evidence captured 2026-07-06T05:02:40-05:00:** `modelcontextprotocol/servers` is public and not archived, with 88,102 GitHub stars observed, updated `2026-07-06T09:43:47Z`, and description: "Model Context Protocol Servers".

## Why this reduces checkout-start friction

MCP adoption moves quickly because it lets assistants call real tools. That also makes the early buyer nervous: before they buy anything, they need proof the seller understands the trust boundary between a harmless local scan and a tool-enabled agent session. The free scanner creates a local receipt before MCP servers, package scripts, workflow files, API connectors, or `.env`-adjacent paths are authorized. The paid $7 starter pack is only positioned for Yellow/Red teams that need repeatable hooks, reviewer prompts, and handoff receipts.

## 60-second proof path

```bash
python3 agent_preflight_lite.py /path/to/repo --markdown > mcp-server-tool-preflight-receipt.md
```

Attach the receipt to the issue, PR, or agent-run handoff before widening an MCP client/server workflow from read-only discovery to filesystem, shell, browser, package, workflow, or deployment tools.

## Buy / skip trigger

- **Green:** keep using the free scanner and skip the paid pack for now.
- **Yellow:** review package scripts, workflow files, MCP server config, generated commands, API connectors, or secret-adjacent paths before enabling tools.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack at https://payhip.com/b/1nmxV if the team needs repeatable preflight hooks, review-comment templates, and handoff receipts before MCP-backed agent work continues.

## Copy-paste receipt

```md
MCP server/tool workflow preflight receipt
- Repo scanned before tool-enabled agent run: <repo/path>
- Assistant/task: MCP client/server + tools / filesystem / shell / package scripts
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Allowed scope after review: <read-only / filesystem read / edits allowed / tests allowed / no deploy / no secrets>
- Next gate: rerun preflight before enabling shell, package, browser, workflow, or deployment tools.
```

## Trust posture

This proof does not require sending private code, MCP server configs, tool tokens, logs, secrets, or repository contents to the seller. The public source repo can be inspected first, the free scanner runs locally, and the paid bundle only adds packaging, hooks, prompts, and repeatable team receipts for buyers who already saw a Yellow/Red need.
