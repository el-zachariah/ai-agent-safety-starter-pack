# Preflight before Continue.dev IDE agents

Customer segment: teams using Continue.dev or similar IDE coding agents before granting workspace context, terminal commands, MCP/context providers, repo secrets, or package-script execution.

Public evidence checked in this pulse: [`continuedev/continue`](https://github.com/continuedev/continue) — 34,692 GitHub stars, updated `2026-07-05T13:11:34Z`, description: "open-source coding agent".

## Why this buyer should care

Continue-style IDE agents often sit close to the developer's real repo, local shell, model config, context providers, and token-bearing files. A cheap preflight receipt gives the team a visible checkpoint before the agent inherits `.continue/` config, package scripts, workflow files, or secret-adjacent files.

The free scanner now treats `.continue/` as agent/workflow config, so a Continue user can prove the tool is relevant before deciding whether the paid `$7` bundle saves setup time.

## 5-minute receipt

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-continue.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-continue.md
```

Paste the decision into the first Continue task note:

```text
agent-preflight-continue
Decision: GREEN / YELLOW / RED
Risk buckets: agent/workflow config, package scripts, secret-adjacent files, risky shell commands
Allowed: read scoped files, propose diffs, run listed tests only
Must ask first: install scripts, package manager changes, MCP/provider config edits, secret-bearing files, deploy commands
Must not touch: .env, token stores, production config, credential files, payment/admin surfaces
```

## Buy or skip trigger

- **Skip for now** when the scan is Green and the IDE agent only reads a small, low-risk repo.
- **Buy the `$7` starter pack** when the scan is Yellow or Red and the agent will edit files, run tests, change `.continue/` or MCP/provider config, or execute package scripts. The paid bundle saves the repeated setup work: full handoff template, destructive-command hook, demo risky repo, and verifier.

## What to review before widening scope

1. `.continue/` config and any model/context-provider rules.
2. MCP, Cursor, Claude, or other agent config in the same repo.
3. Package scripts and workflow files the IDE agent may invoke.
4. Secret-adjacent files that should stay excluded.
5. Destructive shell patterns that should be blocked before task execution.

Source product: <https://payhip.com/b/1nmxV>
