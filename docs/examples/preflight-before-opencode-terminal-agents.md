# Preflight before OpenCode terminal agents

Customer segment: teams trying **OpenCode-style terminal coding agents** in real repositories before the agent gets file-write, shell, package-manager, or MCP/tool access.

Target evidence captured for this proof:

- Repository: [anomalyco/opencode](https://github.com/anomalyco/opencode)
- Public description: The open source coding agent.
- GitHub stars observed this pulse: 182,519
- Updated at: `2026-07-05T13:23:57Z`

## Why this proof exists

OpenCode-style terminal agents are fast precisely because they sit next to a real checkout and can run commands. That also means the first run can inherit repo instructions, package scripts, workflow files, MCP/tool config, and secret-adjacent files before the team has written a safe handoff.

The free scanner in this repo gives a visible receipt first. The paid `$7` starter pack is the upgrade only when the receipt is Yellow/Red and the team wants the repeatable workflow, command hook, templates, and demo repo instead of improvising each agent run.

## 60-second receipt

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-opencode.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-opencode.md
```

Paste this into the OpenCode task before enabling broad edits or test/install commands:

```text
OpenCode preflight receipt: agent-preflight-opencode.md
Decision: Yellow until reviewed.
Allowed now: inspect files, propose patch plan, run read-only commands, run targeted tests after approval.
Must ask first: package installs, networked scripts, deploy/release commands, workflow edits, secret/config file edits, destructive cleanup.
Upgrade trigger: buy the $7 Agent Safety Starter Pack if two or more risk buckets appear, or if package scripts/workflows/MCP/tool configs are present and the agent will run shell commands.
```

## What makes the scan Yellow/Red for this segment

- `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, or similar instructions that shape agent behavior.
- `package.json`, `Makefile`, `justfile`, GitHub Actions, Docker, or release scripts the terminal agent might run.
- MCP/Claude/Cursor/OpenCode tool config, local env files, API-key-adjacent files, or package manager credentials.
- Shell snippets such as `curl | sh`, `rm -rf`, `chmod 777`, `docker.sock`, forced pushes, or deploy commands.

## Buy/skip rule

- **Skip the paid pack for now** if the scan is Green and the first OpenCode task is read-only or a tiny patch with no package/workflow/script changes.
- **Buy the `$7` pack** when the scan is Yellow/Red and the agent will edit files, run tests, touch package/workflow scripts, or operate with MCP/tool access. The pack gives the reusable handoff, blocker hook, report templates, and demo risky repo so the team can repeat the same safety receipt instead of rebuilding it each run.
