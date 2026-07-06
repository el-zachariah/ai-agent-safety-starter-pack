# Haystack agent workflow preflight proof

**Named buyer segment:** teams using [`deepset-ai/haystack`](https://github.com/deepset-ai/haystack) or Haystack-style agent/RAG workflows before repository context, tool functions, retrieval pipelines, package scripts, workflow files, API connectors, or secret-adjacent paths enter an AI-assisted run.

**Public target evidence captured 2026-07-06T04:34:38-05:00:** `deepset-ai/haystack` is public and not archived, with 25,836 GitHub stars observed, updated `2026-07-06T09:28:14Z`, and description: "Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Built for scalable agents, RAG, multimodal applications, semantic search, and conversational systems.".

## Why this reduces checkout-start friction

Haystack-style workflows are strongest when they connect retrieval, routing, tools, memory, and production app code. That also means buyers need a low-friction trust check before agents or pipeline jobs touch install scripts, tests, CI workflows, generated commands, local config, API connectors, or `.env`-adjacent files. The free scanner gives a shareable receipt first; the paid $7 starter pack is only positioned for Yellow/Red teams that need repeatable hooks, reviewer prompts, and handoff receipts.

## 60-second proof path

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > haystack-agent-preflight-receipt.md
```

Attach the receipt to the issue, PR, or task before widening a Haystack agent workflow from prototype retrieval/routing to tool execution, package-script, API connector, or deploy scope.

## Buy / skip trigger

- **Green:** keep using the free scanner and skip the paid pack for now.
- **Yellow:** review flagged package scripts, workflow files, agent/pipeline config, generated commands, API connectors, or secret-adjacent paths before letting the Haystack workflow run tools or deploy.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack at https://payhip.com/b/1nmxV if the team needs repeatable preflight hooks, review-comment templates, and handoff receipts before AI-assisted edits continue.

## Copy-paste receipt

```md
Haystack agent workflow preflight receipt
- Repo scanned before AI-assisted edit/run: <repo/path>
- Assistant/task: Haystack retrieval/agent workflow + tools / tests / package scripts
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Allowed scope after review: <read-only / edits only / tests allowed / no deploy / no secrets>
- Next gate: rerun preflight before enabling shell, package, workflow, or deployment commands.
```

## Trust posture

This proof does not require sending private code to the seller. The public source repo can be inspected first, the free scanner runs locally, and the paid bundle only adds packaging, hooks, prompts, and repeatable team receipts for buyers who already saw a Yellow/Red need.
