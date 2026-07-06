# Preflight before Cloudflare Workers AI Agents

Customer segment: teams building or deploying Cloudflare Agents / Workers AI apps before an agent gets repo context, `wrangler` deploy scope, Durable Object state, package scripts, `.dev.vars`, or API-backed tool access.

Public target evidence verified with GitHub CLI in this pulse:

- Repository: [cloudflare/agents](https://github.com/cloudflare/agents)
- Description: Build and deploy AI Agents on Cloudflare
- Stars at verification time: 5228
- Updated at verification time: 2026-07-05T20:07:34Z
- Archived: false

## Why this buyer segment cares

Cloudflare Agents can connect an app, Durable Objects, Workers runtime config, tool calls, and deploy commands. That is a high-leverage moment to run a local preflight before an AI coding agent or hosted builder edits files, runs package scripts, reads `.dev.vars`, changes `wrangler.toml`, or triggers deploy automation.

Run the free scanner first:

```bash
python3 agent_preflight_lite.py /path/to/cloudflare-agent-repo --json
```

## 60-second Cloudflare Agent handoff receipt

Copy this into the issue, PR, or task before the agent starts:

```text
Cloudflare Agent preflight receipt
Repo: <repo URL or local path>
Agent surface: <Cloudflare Agents / Workers AI / Durable Object / tool-calling app>
Scan command: python3 agent_preflight_lite.py . --json
Risk color: Green / Yellow / Red
Reviewed before tool or deploy access:
- AGENTS.md / CLAUDE.md / .cursorrules / .cursor/rules/*
- wrangler.toml, worker config, Durable Object bindings, and deployment scripts
- package scripts, workflow files, and generated shell commands the agent may run
- .dev.vars, .env, API keys, tokens, and secret-adjacent files
Allowed commands: <tests/build only; no deploy, secret reads, or production writes>
Must ask first: <wrangler deploy, package install, network calls, credential reads, DB/state migrations>
Must not touch: <production secrets, billing/account config, live worker routes, release automation>
Upgrade trigger: buy the $7 pack if the scan is Yellow/Red and you need the reusable report template, destructive-command hook, demo risky repo, and verifier.
```

## Buy / skip rule for this segment

- **Green:** one or fewer low-risk findings; keep the free receipt with the Cloudflare Agent task and proceed with normal review.
- **Yellow:** package scripts, worker config, Durable Object bindings, MCP/tool config, or secret-adjacent local files are present; use the paid pack when you want a repeatable handoff instead of rewriting this receipt.
- **Red:** deploy scripts, destructive shell, production route changes, `.dev.vars`/`.env`, workflow automation, or unclear command scope; use the full $7 workflow before the agent gets tool/deploy access.

Paid bundle: <https://payhip.com/b/1nmxV>
