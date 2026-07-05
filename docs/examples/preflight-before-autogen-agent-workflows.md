# Preflight before AutoGen multi-agent workflows

Customer segment: teams using [`microsoft/autogen`](https://github.com/microsoft/autogen) or similar multi-agent orchestration before giving function-calling agents repo, shell, package-script, MCP, browser, or API-backed tool access.

Public target evidence captured 2026-07-05T10:50:47-05:00: `microsoft/autogen` is live with 59,505 GitHub stars, updated `2026-07-05T14:29:59Z`, and describes itself as `A programming framework for agentic AI`.

## Why this buyer should care before checkout

AutoGen-style workflows can combine planner agents, executor agents, tool/function calls, group chat routing, code execution, and long-lived task context. A bad repo instruction, unsafe package script, or over-broad `.env`/tool mount can propagate through multiple agents before a human sees the damage. This free receipt is the quick proof; the paid $7 pack turns the same checklist into reusable hooks, templates, and a team handoff workflow.

## Five-minute preflight receipt

Run this before the first tool-enabled AutoGen session in a real repository:

1. **Scope the run** — name the task, repo path, allowed files, blocked paths, and whether agents may execute shell/package commands.
2. **Inventory tool surfaces** — list function-calling tools, code executors, browser/API clients, MCP servers, Docker mounts, and any `.env` or token-bearing config reachable by the agents.
3. **Scan repo instructions** — run the free preflight scanner and paste the Markdown receipt into the task issue/PR before the crew starts.
4. **Pin human approval points** — require a human before dependency install scripts, workflow changes, credential use, destructive shell commands, or cross-repo writes.
5. **Keep the receipt with the PR** — attach the risk level, flagged files, allowed command list, and the exact AutoGen config used for the run.

## Yellow/red flags for AutoGen-style crews

- Agents can run shell commands or package scripts without an allowlist.
- A code executor sees the whole checkout plus `.env`, `.npmrc`, cloud config, or browser profile files.
- Planner/executor agents inherit repo instructions that have not been reviewed by a human.
- Tool calls can write to GitHub, cloud dashboards, payment/admin surfaces, or production APIs.
- The team cannot reconstruct which agent saw which instruction/config after the run.

## Copy-paste receipt stub

```text
AutoGen preflight receipt
Repo/task:
Agents/config reviewed:
Allowed tools:
Blocked files/commands:
Preflight scan level: Green / Yellow / Red
Human approval required before:
Receipt owner:
```

## When to buy the reusable pack

Buy the $7 AI Agent Safety Starter Pack if this receipt is Yellow/Red, if multiple agents can call tools, or if the same preflight needs to become a repeatable team workflow: <https://payhip.com/b/1nmxV>.
