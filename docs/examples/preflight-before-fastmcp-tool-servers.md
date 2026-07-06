# Preflight before FastMCP tool-server agent sessions

Customer segment: teams using [`PrefectHQ/fastmcp`](https://github.com/PrefectHQ/fastmcp) or FastMCP-style Python MCP servers before a Claude Code, Cursor, Codex, or other coding agent can read the repo, call MCP tools, run package commands, or work near API credentials.

Public evidence checked in this pulse: `gh repo view jlowin/fastmcp` redirected to canonical `PrefectHQ/fastmcp`; GitHub reported `isArchived=false`, 25,992 stars, updated `2026-07-06T10:05:42Z`, URL https://github.com/PrefectHQ/fastmcp, description `🚀 The fast, Pythonic way to build MCP servers and clients.`

## Why this is a buyer-fit proof

FastMCP is exactly where the paid pack should feel real: a developer is turning local Python functions, API calls, files, and service clients into tools that an agent can invoke. Before that MCP server is connected to Claude Desktop, Claude Code, Cursor, Codex, or another tool-running client, the team needs a small handoff receipt: what the agent may call, what needs approval, what files stay out of scope, and which shell/package commands are blocked.

The free lite scanner now flags `fastmcp` in `pyproject.toml` as an agent-framework dependency and still flags `.mcp.json` / MCP config as agent workflow config. That gives a FastMCP team a local proof before deciding whether the paid `$7` bundle saves setup time.

## 60-second FastMCP tool-server handoff receipt

```bash
python3 agent_preflight_lite.py /path/to/fastmcp-server --json > agent-preflight-fastmcp.json
python3 agent_preflight_lite.py /path/to/fastmcp-server > agent-preflight-fastmcp.md
```

Paste this into the agent task or PR before authorizing MCP tool use:

```text
FASTMCP_TOOL_SERVER_PROOF
Repo preflight: agent-preflight-fastmcp.md
Decision: <Green / Yellow / Red>
Agent may call: <read-only FastMCP tools, test fixtures, local docs>
Agent must ask first: <write tools, external API calls, deploy/publish commands, package installs>
Agent must not touch: <.env, tokens, production credentials, customer data, destructive shell>
Buy trigger: if the scan is Yellow or Red, use the paid $7 workflow bundle for the reusable handoff template, destructive-command hook, demo risky repo, and verifier before wiring this MCP server into a tool-enabled agent session.
```

## What to review first

- `pyproject.toml`, `requirements.txt`, lockfiles, or package scripts that install or run the FastMCP server.
- `.mcp.json`, Claude/Cursor/MCP client config, and any server command that starts local tools.
- FastMCP tools that write files, call external APIs, mutate databases, deploy services, or read customer/private data.
- Secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, cloud credentials, OAuth tokens, or local service config.
- Risky shell patterns such as `curl | sh`, `rm -rf`, `chmod 777`, Docker socket access, or force pushes.

## Buy / skip rule

Skip the paid pack for a Green demo server with no credentials, no write tools, no package/deploy scripts, and no MCP client config. Buy the `$7` starter pack at https://payhip.com/b/1nmxV when the scan is Yellow/Red and a FastMCP server will expose repo files, shell commands, API calls, credentials, or persistent services to a coding agent. That is when the paid report template and destructive-command hook save setup time immediately.

## Trust signal for first buyers

This is customer-specific proof, not generic funnel copy: it names the canonical FastMCP repo, shows public GitHub evidence, gives a pasteable MCP handoff receipt, and ties the paid ask to a concrete Yellow/Red risk trigger.
