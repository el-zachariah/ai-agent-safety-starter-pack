# Preflight before LangGraph stateful agent workflows

**Named buyer segment:** teams using [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) or a similar stateful agent workflow framework before giving an agent repo, tool, shell, MCP, package-script, or deployment context.

Public target evidence captured during the deadline pulse: `langchain-ai/langgraph` is live at <https://github.com/langchain-ai/langgraph>, description `Build resilient agents.`, 36,528 GitHub stars observed, and updated `2026-07-05T14:27:57Z`.

## Why this proof matters before checkout

LangGraph-style teams are not buying a generic "AI safety" PDF. Their first-dollar question is practical:

> "Before a stateful graph agent edits code or calls tools in this repo, what do we check, what do we block, and what receipt do we leave for review?"

Run the free scanner first. Buy the $7 pack only when the scan is Yellow/Red and you need the reusable report template, destructive-command hook, demo risky repo, and verifier instead of rebuilding that workflow during the agent run.

## 5-minute LangGraph preflight receipt

Copy this before the agent starts:

```text
agent-preflight-langgraph
Repo:
Branch / PR:
Agent framework: LangGraph / stateful graph agent
Planned tools: repo read/write, package install/test, API calls, MCP/tool connectors, deployment target
Free scan command: python3 agent_preflight_lite.py . --json
Decision: Green / Yellow / Red
Risk buckets found:
- Agent instructions: AGENTS.md / CLAUDE.md / custom graph runbooks
- Agent configs: langgraph.json, langchain.json, .continue/, .cursor/, .mcp.json
- Secret-adjacent files: .env, API key examples, deployment credentials
- Package/workflow scripts: npm/pip/uv/poetry install, build, test, deploy hooks
- Tool execution: shell tools, browser tools, repo write tools, database/API tools
- Persistence: checkpoint stores, vector stores, traces, run artifacts
Allowed without asking:
- read docs/tests/config names
- run safe lint/unit tests listed here:
Must ask first:
- install new packages
- call paid/external APIs
- modify deployment, auth, database, MCP, or checkpoint/store config
Blocked:
- destructive deletes / broad chmod / pipe-to-shell installers / force push / secret printing
Paid-pack trigger:
- Buy/use the $7 workflow if decision is Yellow/Red and the agent will run commands or touch config/secrets.
```

## LangGraph-specific review checklist

1. **Graph entrypoints:** identify the compiled graph, nodes, tool call edges, and any human-in-the-loop interrupts before the agent edits them.
2. **State and persistence:** list checkpoint stores, vector stores, trace sinks, and local artifacts that could retain prompts, repo snippets, customer data, or secrets.
3. **Tool scope:** write what the graph agent may call: shell, browser, GitHub, database, SaaS APIs, MCP tools, local files, and package managers.
4. **Package and workflow scripts:** review `package.json`, `pyproject.toml`, `uv.lock`, `.github/workflows/`, Docker files, and deploy scripts before an agent runs install/test/build.
5. **Secret boundaries:** exclude `.env`, tokens, cloud credentials, PayPal/Stripe/admin surfaces, production data, and private traces from agent context.
6. **Stop rules:** require human confirmation before migration, deploy, billing, email/send, wallet/payment, data deletion, credential rotation, or irreversible repository operations.

## Pasteable handoff for a LangGraph agent task

```text
Before editing, run the repo preflight and summarize the Green/Yellow/Red result.
You may read source/docs/tests and run the safe tests listed by the maintainer.
You must ask before package installs, external API calls, workflow/deploy changes, MCP/tool config changes, checkpoint/vector-store changes, or anything touching .env/secrets.
You must not run destructive shell commands, print secrets, force-push, delete data, or modify billing/payment/admin surfaces.
If the scan is Yellow/Red, use the full preflight workflow/hook before continuing.
```

## Buy / skip rule

- **Skip for now** if the scan is Green and the graph agent only reads docs or makes a tiny reviewed patch.
- **Buy the $7 starter pack** at <https://payhip.com/b/1nmxV> if the scan is Yellow/Red and the LangGraph run will use shell tools, package scripts, MCP/API tools, checkpoint/vector stores, deployment config, or secret-adjacent files.

This is an independent preflight example for LangGraph-style workflows; it is not affiliated with or endorsed by LangChain/LangGraph.
