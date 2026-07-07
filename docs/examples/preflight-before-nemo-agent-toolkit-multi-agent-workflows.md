# Preflight before NVIDIA NeMo Agent Toolkit multi-agent workflows

Unique marker: `NEMO_AGENT_TOOLKIT_MULTI_AGENT_WORKFLOW_PROOF`

This customer proof is for teams evaluating or using [`NVIDIA/NeMo-Agent-Toolkit`](https://github.com/NVIDIA/NeMo-Agent-Toolkit) to connect and optimize teams of AI agents before those agents touch a production repository, package scripts, MCP/API tools, deployment config, vector/database settings, or secret-adjacent environment values.

Target verification captured for this proof:

- Repository: `NVIDIA/NeMo-Agent-Toolkit`
- Public URL: https://github.com/NVIDIA/NeMo-Agent-Toolkit
- GitHub description: The NVIDIA NeMo Agent toolkit is an open-source library for efficiently connecting and optimizing teams of AI agents.
- Stars observed: `2478`
- Updated at: `2026-07-07T02:46:10Z`
- Archived: `False`

## 60-second buyer check

Run the free scanner before handing a NeMo Agent Toolkit workflow a real repo or deployment surface:

```bash
python3 scripts/lite_preflight.py /path/to/repo --format markdown --output nemo-preflight.md
```

Treat the result as a go/no-go receipt for the first agent run:

- **Green:** keep the free scanner receipt and run a narrow, read-only pilot.
- **Yellow:** buy the $7 AI Agent Safety Starter Pack before the agent gets write access, because the paid bundle adds handoff checklists, review-comment templates, red-flag actions, and reusable receipts for agent teams.
- **Red:** buy the $7 pack before continuing and require a maintainer sign-off receipt before any repo write, shell command, deployment hook, or credential-adjacent config enters the run.

## What this catches for NeMo Agent Toolkit teams

- Multi-agent orchestration files that call local tools, package scripts, or generated shell commands.
- MCP/API connector configs that can expand an agent from chat-only into repo, network, or deployment control.
- Environment and secret-adjacent files that should be excluded or acknowledged before an agent run.
- CI/deployment/workflow files that can be changed by an agent and then executed later by humans or automation.
- Vector/database/retrieval config that can leak sensitive corpus paths or make an agent look safer than it is.

## Copy/paste preflight receipt

```text
NVIDIA NeMo Agent Toolkit preflight receipt
Target repo: <repo/path>
Agent workflow: <workflow or team-of-agents entrypoint>
Free scanner result: Green / Yellow / Red
Top risk bucket: <package-scripts | workflow-files | env-secrets | MCP/API-tools | deployment-config>
Decision: <run read-only | buy/use paid checklist first | stop until maintainer approves>
Reviewer: <name/handle>
Timestamp: <UTC>
```

## Paid upgrade trigger

If the free scan is Yellow or Red, the paid pack is the fastest next step because it gives the team a repeatable handoff checklist, review-comment template, and red-flag action matrix instead of another generic AI-safety article.

Paid bundle: https://payhip.com/b/1nmxV
