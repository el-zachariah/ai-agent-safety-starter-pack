# Preflight before LangGraph stateful agent workflows

Public target verified for this proof: [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) — archived=`False`, stars=`36640`, updated=`2026-07-06T22:58:54Z`.

This page is for teams building stateful agent graphs with tool calls, persistence, and deployment steps that need a buy/skip risk receipt.

## 60-second use case

Before a developer gives an agent SDK workflow access to a repo, terminal, CI token, deployment script, or integration secret, run the free scanner and paste the receipt into the PR or handoff note.

```bash
python tools/agent_preflight_lite.py --path . --format markdown > preflight-receipt.md
```

## What the receipt should prove for LangGraph stateful agent workflows

- Tool boundaries are visible before agent code runs shell, file-write, browser, or API actions.
- Repo automation paths are visible: `.github/workflows`, shell scripts, package hooks, deployment configs, and local env files.
- Secret-handling paths are visible before agent tooling touches `.env`, API tokens, webhooks, or hosted tool credentials.
- Reviewer can classify the run as Green / Yellow / Red before approving the next agent action.

## Buy / skip trigger

- **Green:** keep using the free scanner and do not buy yet.
- **Yellow:** buy the $7 pack if you need the full templates, stronger handoff language, and copy-paste command hook before a teammate or agent proceeds.
- **Red:** buy the $7 pack before running the agent workflow in a real repo; use the paid checklist to turn the risky receipt into concrete fix tasks.

Paid pack: https://payhip.com/b/1nmxV

## Why this is a real buyer segment

`langchain-ai/langgraph` is a live public repo with 36640 GitHub stars. The relevant signals for this offer are: LangGraph, stateful, tool calls, persistence, deployment. This proof does not claim affiliation; it shows exactly how the Agent Safety Starter Pack fits teams already adopting this kind of agent workflow.
