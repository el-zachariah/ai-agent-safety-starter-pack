# LangChain tool-agent preflight proof

**Named buyer segment:** teams using [`langchain-ai/langchain`](https://github.com/langchain-ai/langchain) or LangChain-style tool/retriever/function-calling agents before repository context, generated commands, package scripts, workflow files, MCP/API connectors, callbacks, or secret-adjacent configuration enter an AI-assisted run.

**Public target evidence captured 2026-07-06T05:16:39-05:00:** `langchain-ai/langchain` is public and not archived, with 141,075 GitHub stars observed, updated `2026-07-06T09:55:27Z`, and description: "The agent engineering platform.".

## Why this reduces checkout-start friction

LangChain buyers do not need to trust a seller with private code before seeing value. They can run the free local scanner first, attach a receipt to the agent task, and only buy the $7 starter pack when the receipt is Yellow/Red and the team needs repeatable hooks, reviewer prompts, and handoff receipts.

LangChain-style projects often combine tools, retrievers, agents, callbacks, notebooks, environment files, CI workflows, package scripts, and API keys. The risky moment is not "using LangChain"; it is letting a tool-enabled agent inherit repo/shell/API scope without a visible preflight receipt.

## 60-second proof path

```bash
python3 agent_preflight_lite.py /path/to/repo --markdown > langchain-tool-agent-preflight-receipt.md
```

Attach the receipt to the issue, PR, or agent task before widening scope from read/search to edits, package commands, tool/API connectors, workflow changes, callbacks, or deployment-adjacent config.

## Buy / skip trigger

- **Green:** keep using the free scanner and skip the paid pack for now.
- **Yellow:** review package scripts, workflow files, notebooks, callback/tool config, retriever/index paths, generated shell commands, and secret-adjacent files before the LangChain agent continues.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack at https://payhip.com/b/1nmxV if the team needs reusable preflight hooks, review-comment templates, and handoff receipts before AI-assisted work resumes.

## Copy-paste receipt

```md
LangChain tool-agent preflight receipt
- Repo scanned before AI-assisted run: <repo/path>
- Agent/tool scope requested: <tools/retrievers/callbacks/package scripts/workflows/API connectors>
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Allowed scope after review: <read/search only / edits allowed / tests allowed / no deploy / no secrets>
- Next gate: rerun preflight before enabling shell, package, workflow, callback, or credentialed connector scope.
```

## Trust posture

This proof does not require sending private code, prompts, LangSmith traces, API keys, embeddings, or repository contents to the seller. The public source repo can be inspected first, the free scanner runs locally, and the paid bundle only adds packaging, hooks, prompts, and repeatable team receipts for buyers who already saw a Yellow/Red need.
