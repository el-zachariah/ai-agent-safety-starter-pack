# Preflight before VoltAgent agent workflows

Named customer segment: teams building TypeScript AI agents with VoltAgent before granting write, shell, package-script, MCP/tool, browser, or credential-adjacent scope to an agent in a real repository.

Public evidence checked in this pulse: [`VoltAgent/voltagent`](https://github.com/VoltAgent/voltagent) is live, not archived, had 9,953 GitHub stars when checked, was updated `2026-07-06T11:12:31Z`, and describes itself as: "AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework".

This is not an affiliation or endorsement. It is a concrete first-buyer proof for developers who already use TypeScript agent workflows, observability, and tool calls, but need a fast local receipt before the workflow touches a real checkout.

## 60-second preflight receipt

Run the free scanner in the repository the VoltAgent workflow will read or mutate:

```bash
python3 agent_preflight_lite.py /path/to/repo --markdown > voltagent-typescript-agent-workflows-preflight.md
python3 agent_preflight_lite.py /path/to/repo --json > voltagent-typescript-agent-workflows-preflight.json
```

Attach the Markdown receipt to the task, PR, issue, or run notes before widening agent scope.

## What the receipt should name

- Package and workflow files such as `pyproject.toml`, `package.json`, lockfiles, build scripts, and CI workflows.
- Agent/tool configuration that can reach shell commands, browser automation, MCP servers, local files, APIs, or secret-adjacent `.env` paths.
- Generated-code boundaries: which files the agent may edit, which commands it may run, and which data connectors stay read-only.
- Any package scripts, test commands, deploy commands, or external tool calls that will execute before a human reviews the result.

## Copy-paste run-ticket note

```text
VoltAgent agent preflight receipt
Repo/task: <link>
Agent/tool scope requested: <read-only / write / shell / browser / MCP / API connector>
Preflight result: <Green / Yellow / Red>
Risk buckets named: <package scripts, workflow files, env/secrets, agent config, generated edits>
Allowed commands: <exact commands>
Must ask before: <deploy, publish, destructive shell, credential/API access, external side effects>
Decision: <run free / pause and buy starter pack / do not run>
```

## Buy / skip trigger

- **Green:** keep the free receipt and run with narrow, least-privilege tool scope. Do not buy yet.
- **Yellow:** buy the `$7` AI Agent Safety Starter Pack at <https://payhip.com/b/1nmxV> if the team wants the reusable handoff template, destructive-command hook, and reviewer prompts before widening agent scope.
- **Red:** stop the run and use the paid pack's repeatable preflight workflow before allowing shell, write, or credential-backed tools.

The paid bundle is positioned here only for teams that saw real Yellow/Red repo risk and want a ready-made local workflow instead of rebuilding the same receipt, hook, and review checklist for each VoltAgent-style agent run.
