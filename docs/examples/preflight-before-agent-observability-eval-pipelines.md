# Agent observability and eval pipeline preflight proof

Buyer segment: teams wiring Langfuse, Phoenix, or similar agent observability and eval pipelines into AI coding agents before those agents touch real repositories, tool calls, API backed actions, package scripts, or deployment paths.

## Public target evidence

- Primary target: [langfuse/langfuse](https://github.com/langfuse/langfuse) observed with 30479 stars, archived=False, updated 2026-07-06T01:05:36Z.
- Description captured from GitHub API: 🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 .
- Adjacent target: [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) observed with 10408 stars, archived=False, updated 2026-07-06T00:55:52Z.

## Why this buyer cares before checkout

Agent observability buyers already believe agent runs need traces, evals, and accountability. The missing step is a repo-scope preflight receipt before a monitored agent run gets write, shell, package-script, MCP, browser, or credential-adjacent access.

A lightweight preflight receipt gives them a before-run artifact they can attach to an eval, PR, or runbook:

1. Which repo instructions, workflow files, MCP configs, package scripts, and secret-adjacent files were visible before the agent run.
2. Whether the run is Green, Yellow, or Red before tool access expands.
3. What reviewer should approve or isolate before the agent proceeds.

## Free proof path

Use the public lite scanner first:

```bash
python3 tools/repo_lite_preflight.py /path/to/repo --markdown preflight-receipt.md --json preflight-receipt.json
```

Attach `preflight-receipt.md` beside the Langfuse, Phoenix, CI, or eval run record before a coding agent starts editing.

## Buy or skip trigger

- Buy the $7 pack when the free receipt is Yellow or Red and the team needs copy-paste reviewer prompts, a stronger Claude Code command, and repeatable handoff wording before allowing the next agent run.
- Skip it for now when the receipt is Green, no repo/write/API scope is being granted, and the agent run is purely local experimentation.

Product checkout: https://payhip.com/b/1nmxV
