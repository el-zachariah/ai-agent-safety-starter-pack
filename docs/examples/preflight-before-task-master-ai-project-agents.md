# Preflight before Task Master AI project-agent runs

Named buyer segment: teams using [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) / Task Master AI to turn PRDs into tasks, then let Claude Code, Cursor, Codex, or another coding agent execute those tasks in a real repository.

Public target verified in this pulse: `eyaltoledano/claude-task-master`; stars observed by `gh repo view`: `27768`; latest public update: `2026-07-06T17:23:44Z`. Description: An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others.

Marker: `TASK_MASTER_AI_PROJECT_AGENT_PROOF`

## Why this proof exists

Task Master AI users are close to checkout-start intent because they already have a multi-step agent workflow: product requirements become task files, task files become implementation prompts, and the next step is usually a repo-editing coding agent. That is exactly where a cheap preflight receipt is useful before money, credentials, package scripts, or deployment settings enter scope.

Before a Task Master driven run, check the repo for:

- `.taskmaster/` task state, generated PRD/task files, and any model or provider config;
- `.cursor/rules/*`, `.cursorrules`, `CLAUDE.md`, `AGENTS.md`, or other agent instruction files that can change agent behavior;
- package scripts, GitHub Actions, Makefiles, Docker/Compose files, or deploy commands the agent may run while completing tasks;
- `.env`, `.npmrc`, `.pypirc`, API-token docs, webhook URLs, or other secret-adjacent material;
- MCP/tool configuration that lets the coding agent reach browsers, databases, shells, or external APIs.

## Free scan first

From this public repo, run:

```bash
python3 agent_preflight_lite.py /path/to/task-master-project
python3 agent_preflight_lite.py /path/to/task-master-project --json
```

Use the result as a copy-paste receipt in the Task Master task, issue, or pull request before the implementation agent starts.

## Buy / skip trigger

- **Green:** no agent config, no risky scripts, no secret-adjacent files, no MCP/tool scope. Keep using the free scanner and normal review.
- **Yellow:** Task Master generated tasks plus package scripts, agent instruction files, CI workflows, `.taskmaster/` state, or MCP/tool connectors are present. Buy the $7 starter pack for the repeatable handoff, report template, and destructive-command guardrail: https://payhip.com/b/1nmxV
- **Red:** secret-adjacent files, deploy tokens, shell commands, or destructive operations are in scope. Stop the agent run, tighten scope, then use the paid pack to create a reviewable safety receipt before resuming: https://payhip.com/b/1nmxV

## Copy-paste receipt for a Task Master task

```text
Task Master AI project-agent preflight: run agent_preflight_lite.py before executing this task.
Target repo: <repo path or URL>
Task files checked: .taskmaster/* and generated task markdown/json
Risk buckets observed: <Green/Yellow/Red + bullets>
Agent scope allowed: <read-only / specific files / no shell / no secrets>
Paid pack needed? Buy only on Yellow/Red: https://payhip.com/b/1nmxV
```

This makes the offer feel real to Task Master users: run the free receipt first; only pay when the scan shows workflow risk worth packaging into a reusable team handoff.
