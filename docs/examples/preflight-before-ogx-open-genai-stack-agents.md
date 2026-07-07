# Preflight before OGX / Llama Stack-style Open GenAI Stack agent runs

Marker: `OGX_OPEN_GENAI_STACK_AGENT_PROOF`

Target segment: teams evaluating [`ogx-ai/ogx`](https://github.com/ogx-ai/ogx) / Open GenAI Stack-style apps before they let an AI agent touch repo context, tool wiring, provider credentials, eval scripts, notebook data, package scripts, or deployment files.

This is a free buyer-specific proof page for the AI Agent Safety Starter Pack. It makes the checkout decision concrete for a named segment instead of asking an OGX maintainer or adopter to trust a generic safety claim.

## Why this segment should care

OGX / Llama Stack-style projects tend to combine model/provider routing, RAG or memory components, tool calls, eval harnesses, notebooks, and deployment scripts. That is exactly where a coding agent can accidentally cross from "read a few files" into "run a package script, expose a token, or mutate a workflow".

Before starting the agent, capture a 60-second Green / Yellow / Red receipt:

1. List the agent's planned task and repo path.
2. Check for `.env`, provider key references, workflow files, package scripts, notebook data, MCP/tool configs, and deployment commands.
3. Mark the run **Green** only when it is read-only and away from secret-adjacent files.
4. Mark the run **Yellow** when the agent may inspect repo context, package scripts, tool configs, eval datasets, notebooks, or deployment files.
5. Mark the run **Red** when the agent can write files, run shell/package/deploy commands, or touch provider credentials and production routing.

## Copy-paste handoff receipt

```text
OGX_OPEN_GENAI_STACK_AGENT_PROOF
Repo/workflow: ogx-ai/ogx-style Open GenAI Stack app
Agent task: <what the agent will change or inspect>
Scope checked: repo files, package scripts, workflow files, notebooks, tool/RAG configs, provider credentials, deployment commands
Decision: Green / Yellow / Red
Reason: <one sentence>
Next safe action: <read-only inspect / run the paid checklist / stop for owner approval>
```

## Buy trigger

Use the free receipt when the run is obviously **Green**.

Buy the paid starter pack at https://payhip.com/b/1nmxV when the result is **Yellow** or **Red** because the bundle gives the fuller checklist, copy-paste prompts, and handoff templates for agent runs near provider keys, package/deploy commands, notebooks, eval datasets, RAG/tool configs, or production routing.

Seller/support identity: Zachariah / Signal Loom Works via el-zachariah.
