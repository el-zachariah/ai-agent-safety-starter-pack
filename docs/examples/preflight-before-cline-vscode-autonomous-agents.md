# Preflight before Cline VS Code autonomous-agent runs

Target buyer: teams using [cline/cline](https://github.com/cline/cline) or Cline-style agentic coding workflows before letting an AI agent inspect a real repo, run terminal commands, call MCP/browser/API tools, or touch secret-adjacent files.

Public target evidence captured during this deadline pulse:

- Repository: `cline/cline`
- Stars observed: `64,333`
- Last updated: `2026-07-06T07:14:57Z`
- Public description: Autonomous coding agent as an SDK, IDE extension, or CLI assistant.

## Why this matters before checkout

A Cline run can inherit workspace instructions, tool allow-lists, package scripts, browser/MCP connectors, and local environment assumptions. That is exactly when a first buyer needs to know whether the free scan is Green, Yellow, or Red before buying the $7 bundle.

Run the free scanner first:

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/cline_vscode_autonomous_agents_workspace
```

Review these Cline-specific signals before the agent starts:

- agent instruction/config files such as `.clinerules`, `.cline/rules/*`, `.clineignore`;
- package scripts, workflow files, install commands, and generated runbooks the agent may execute;
- MCP/browser/API tool config and any repo-local allow/deny lists;
- secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, SSH keys, deployment tokens, or local credentials.

## 60-second handoff receipt

Paste this into the task ticket before the agent run:

```text
Cline preflight receipt
Repo:
Scan decision: Green / Yellow / Red
Risk buckets found:
Agent may run:
Agent must ask before:
Agent must not touch:
Secret-adjacent paths excluded:
Reviewer/owner:
```

## Buy / skip trigger

- Green: keep using the free lite scanner and normal review discipline.
- Yellow: buy the $7 starter pack if you need the reusable handoff template, destructive-command hook, and verifier before giving Cline terminal/tool scope.
- Red: stop the agent run until a human narrows tool scope; the $7 bundle is meant to make that handoff repeatable instead of improvised.

Paid bundle: https://payhip.com/b/1nmxV
