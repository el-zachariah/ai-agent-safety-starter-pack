# Preflight before smolagents tool-running agent workflows

Customer segment: teams using [huggingface/smolagents](https://github.com/huggingface/smolagents) or similar Python tool-running agents before granting repo files, package scripts, environment variables, local command execution, browser tools, or API-backed tools.

Target evidence captured 2026-07-05T12:05:55-05:00:

- Public repo: `huggingface/smolagents`
- Stars observed: `28193`
- Updated at: `2026-07-05T15:55:46Z`
- Public description: 🤗 smolagents: a barebones library for agents that think in code.

## Why this proof exists

A smolagents-style workflow can move fast from prompt to tool call: a `CodeAgent` or tool-calling agent may inspect files, call Python functions, run package scripts, touch local caches, or receive API-backed tool credentials. The sale friction for the $7 pack is trust: buyers need to see the exact handoff they would keep before widening that agent scope.

The free scanner does not audit the model or sandbox the runtime. It gives the buyer a visible preflight receipt so the team can decide what the agent may read, what it may execute, and when the paid starter pack saves setup time.

## 60-second preflight receipt

Run this before the first smolagents task that touches a real repo:

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-smolagents.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-smolagents.md
```

Write the receipt next to the task ticket:

| Field | Fill before tool access |
| --- | --- |
| Agent entrypoint | `CodeAgent`, custom tool-calling agent, or hosted runner name |
| Repo scope | exact path/branch and files the agent may inspect |
| Tool scope | allowed tools/functions, shell access, browser/API tools, MCP connectors |
| Risk decision | Green / Yellow / Red from the lite scan |
| Must ask first | installs, migrations, deploys, destructive writes, credential reads, network calls |
| Must not touch | `.env`, token stores, prod configs, payment/admin surfaces, private keys |
| Human reviewer | person who approves widening tool scope or running package scripts |

## Pasteable task handoff

```text
Before running the smolagents workflow, read agent-preflight-smolagents.md.
Allowed: inspect source files and run read-only analysis commands.
Ask first: package installs, tests that start services, migrations, browser/API actions, external network calls, or editing config files.
Never touch: .env files, token stores, private keys, payment/admin settings, or deployment credentials.
If the preflight decision is Yellow/Red, keep this receipt with the task and use the full workflow bundle before widening shell/tool scope.
```

## Buy / skip trigger

Skip the paid pack if the scan is Green and the agent only receives read-only local context.

Buy the [$7 starter pack](https://payhip.com/b/1nmxV) when the scan is Yellow/Red **and** the smolagents workflow will run package scripts, call repo-local tools, use browser/API connectors, load `.env`-adjacent values, or hand work between multiple agents. The paid pack gives the reusable report template, destructive-command hook, buyer quickstart, demo risky repo, and verifier so the team does not rebuild the guardrail process for each agent run.
