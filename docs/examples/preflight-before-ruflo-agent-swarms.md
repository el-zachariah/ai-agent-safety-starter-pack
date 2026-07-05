# Preflight before Ruflo / Claude Flow-style agent swarms

Customer segment: teams evaluating [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) or a similar multi-agent meta-harness before it coordinates Claude Code, Codex, Hermes, MCP tools, browser/API calls, and shell-enabled workflows inside a real repository.

Public target evidence captured 2026-07-05: GitHub returned `ruvnet/ruflo`, non-archived, 63,132 stars, updated `2026-07-05T20:23:06Z`, with repository description mentioning multi-player swarms, autonomous workflows, and native Claude Code / Codex / Hermes integration.

## Why this buyer should care

A swarm harness multiplies the risk of a normal single-agent run. One bad repo instruction, package script, MCP server, or secret-adjacent file can be inherited by multiple workers. The free lite preflight gives the team a fast receipt before the harness fans out work.

Run it before the swarm receives:

- repo write access or a task branch,
- shell/install/test/deploy scope,
- MCP servers or browser/API tools,
- `.env`, `.npmrc`, cloud config, or other secret-adjacent files,
- persistent memory, checkpoints, or planner/executor state,
- package scripts that agents may run automatically.

## 60-second free check

```bash
python3 agent_preflight_lite.py . --json > agent-preflight-ruflo-swarm.json
python3 agent_preflight_lite.py . > agent-preflight-ruflo-swarm.md
```

Attach the Markdown receipt to the swarm run ticket before the first worker starts.

## Pasteable swarm handoff receipt

```text
Ruflo / Claude Flow-style swarm preflight
Repo: <repo>
Task: <issue / branch / goal>
Scan result: Green / Yellow / Red
Risk buckets found: <agent instructions, MCP/tool config, package scripts, workflows, secret-adjacent files, risky shell>
Allowed now: <read-only files / exact tests / exact package scripts>
Must ask first: <deploy, env reads, credential use, package install, network calls, workflow edits>
Must not touch: <secrets, production config, payment/admin surfaces, destructive shell>
Swarm fan-out limit: <single worker until receipt reviewed / planner-only / no background daemons>
Upgrade trigger: buy/use the $7 pack if Yellow or Red and this workflow will repeat.
```

## Buy / skip trigger

- **Green:** no agent config, no secret-adjacent files, no package/workflow scripts, and no risky shell. Keep the free receipt with the run ticket and proceed with normal review.
- **Yellow:** two or three risk buckets, MCP/tool config, or package scripts a swarm could run. Use the paid pack when you need the reusable report template and destructive-command hook instead of rewriting the handoff.
- **Red:** secret-adjacent files plus risky shell, deploy scripts, workflow permission changes, or production/API scope. Do not fan out the swarm until the full preflight workflow and local guardrails are in place.

Paid workflow bundle: https://payhip.com/b/1nmxV
