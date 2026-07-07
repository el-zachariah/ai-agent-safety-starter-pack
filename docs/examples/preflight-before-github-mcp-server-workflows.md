# GitHub MCP Server workflow preflight proof

**Verified public target:** `github/github-mcp-server` — https://github.com/github/github-mcp-server  
**Public evidence captured:** 2026-07-07T06:34:15-05:00. The repository is public, not archived, showed 31,259 GitHub stars, last updated `2026-07-07T11:18:29Z`, and describes itself as: "GitHub's official MCP Server".

This proof is for teams wiring the GitHub MCP Server into Claude Code, Cursor, Codex, or another agent harness before the agent can read issues, inspect pull requests, open branches, or trigger repository automation.

## Why this buyer segment should care before checkout

A GitHub MCP Server workflow turns repository metadata and write-capable actions into agent tools. Before a local or hosted agent receives those tools, the team needs a repeatable receipt for:

- repository/organization scopes granted to the MCP server;
- issue, PR, branch, workflow, and release actions an agent may call;
- package scripts, CI jobs, and deployment files the agent might trigger indirectly;
- token, app, and webhook boundaries that are secret-adjacent even when the repo is public;
- a visible human handoff that says what the agent can change, what it must not touch, and when to stop.

## Copy-paste preflight receipt

```text
GITHUB_MCP_SERVER_WORKFLOW_PROOF
Target workflow: github/github-mcp-server connected to an AI coding agent.
Green: read-only repo inspection, no secrets/tokens exposed, no write tools enabled, no workflow/deploy trigger access.
Yellow: agent can draft issues/PRs/branches or run local package scripts; use the $7 starter pack for a repeatable handoff receipt and destructive-action checklist.
Red: agent can merge, push protected branches, edit workflows, cut releases, alter secrets, or invoke deployment/payment/customer-impacting automation; stop and run the full preflight before granting access.
```

## What to inspect in the free repo before buying

- Free scanner and examples: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>
- Landing page: <https://el-zachariah.github.io/ai-agent-safety-starter-pack/>
- Paid reusable workflow bundle: <https://payhip.com/b/1nmxV>

Buy the paid pack only when your GitHub MCP Server setup lands in Yellow/Red and you need the reusable checklist, hook template, and handoff language. Skip it if your setup is read-only and already has a clear internal approval receipt.

**Not affiliated with `github/github-mcp-server` or GitHub.** This is a buyer-specific safety proof from Zachariah / Signal Loom Works for teams using that workflow style.
