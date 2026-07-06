# Open SWE async coding-agent preflight proof

`OPEN_SWE_ASYNC_CODING_AGENT_PROOF`

Public target verified: [`langchain-ai/open-swe`](https://github.com/langchain-ai/open-swe), an open-source asynchronous coding agent. This proof is for teams evaluating Open SWE or similar task-branch coding agents before they let the agent read repo context, create branches, run package scripts, edit workflow files, call MCP/API tools, or work near secret-adjacent config.

## 60-second free receipt before the agent runs

```text
Target: Open SWE / async coding-agent run
Repo: <repo or branch under review>
Preflight command: python3 agent_preflight_lite.py . --json
Decision: Green / Yellow / Red
Allowed before first agent action: read issue, inspect files, propose plan
Must ask before: package install, shell command, workflow edit, deploy, token/env access, force push
```

## What the free scanner is checking

- agent instruction files such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, or repository-specific coding-agent rules;
- package scripts, CI workflows, Docker/devcontainer files, and generated task branches that an async coding agent may execute or modify;
- MCP/API connector config, browser/tool automation hooks, and secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, or SSH keys;
- destructive or high-blast-radius shell patterns that should be blocked before autonomous patch generation.

## Buy / skip trigger

- **Green:** no meaningful repo/tooling risk signals. Keep the free receipt and skip the paid pack for now.
- **Yellow/Red:** two or more buckets light up, or the agent can touch package scripts, workflows, MCP/API connectors, deployment config, or secret-adjacent files. That is the point to buy the $7 AI Agent Safety Starter Pack: https://payhip.com/b/1nmxV

## Copy-paste handoff

```text
Before Open SWE starts the task branch, attach the free preflight receipt.
If the scan is Yellow/Red, use the paid starter pack to turn the receipt into: allowed commands, blocked destructive commands, files the agent must not read, and the human approval points for package/deploy/workflow changes.
```
