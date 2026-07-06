# AgentOps observability/eval preflight proof

Named customer segment: teams using [`AgentOps-AI/agentops`](https://github.com/AgentOps-AI/agentops) or similar agent observability / visual-agent / RAG-agent workflows before real repositories, shell tools, package scripts, workflow files, MCP/API connectors, or secret-adjacent config enter scope.

Target evidence captured 2026-07-06T11:36:26.933488-05:00: `AgentOps-AI/agentops` is public, not archived, observed stars `5681`, updated `2026-07-06T13:19:22Z`, description: "Python SDK for AI agent monitoring, LLM cost tracking, benchmarking, and more. Integrates with most LLMs and agent frameworks including CrewAI, Agno, OpenAI Agents SDK, Langchain, Autogen, AG2, and CamelAI".

## Why this proof matters

AgentOps users already care about traces, evals, costs, and replay. The missing first-run trust step is a local repo preflight before an instrumented agent receives shell tools, workflow files, package scripts, or secret-adjacent config.

Run the free scanner before the first `AgentOps-instrumented agent run`, before widening from design/review to edit/apply mode, and before allowing generated commands, package scripts, deploy workflows, browser tools, or credential-adjacent files.

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > agentops-observability-eval-workflows-preflight-receipt.md
```

## Green / Yellow / Red buy trigger

- **Green:** share the free receipt and skip the paid pack for now.
- **Yellow:** review the flagged package scripts, workflow files, agent rules, MCP/API/tool config, or secret-adjacent paths before giving the agent broader scope.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need the full hook bundle, reviewer checklist, and repeatable handoff receipts before the agent edits or executes in the repo.

## Copy-paste receipt for a first run

```md
AgentOps observability/eval workflow teams preflight receipt
- Repo scanned before agent execution: <repo/path>
- Agent/task: AgentOps-instrumented agent run
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <read-only / files only / tests only / no deploy / no secrets>
- Next gate: rerun before enabling shell/package commands, deploy workflows, or credentialed tools.
```

## What the paid bundle adds for Yellow/Red scans

The public scanner proves the workflow without requiring a purchase. The $7 pack is for teams that hit Yellow/Red and want ready-to-drop command hooks, reviewer prompts, and handoff receipts so every AgentOps observability/eval workflow teams run starts with the same safety gate.
