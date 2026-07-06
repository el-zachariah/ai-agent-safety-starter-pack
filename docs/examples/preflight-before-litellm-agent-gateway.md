# Preflight before LiteLLM agent gateway runs

Target segment: teams using `BerriAI/litellm` as an LLM gateway/proxy for Claude Code, Cursor, Codex, LangGraph, CrewAI, browser agents, MCP-backed agents, or internal evaluation runners.

Public target evidence verified during this pulse:

- Repository: `BerriAI/litellm`
- URL: <https://github.com/BerriAI/litellm>
- Stars observed: `52762`
- Last updated: `2026-07-06T15:20:06Z`
- Why it matters: a LiteLLM proxy often centralizes API keys, provider routing, budget limits, logging, and model access for many downstream agents. A bad agent task can turn one repo-scoped change into gateway-wide leakage or spend.

## The checkout-start friction this proof answers

A buyer looking at the paid pack may ask: "Is this just generic AI safety copy, or does it fit my real agent stack?"

For LiteLLM gateway users, the fit is concrete:

- `config.yaml`, `litellm_config.yaml`, Docker compose files, provider env vars, and proxy routing are sensitive enough to preflight before an agent edits or summarizes them.
- Gateway-backed agents can multiply one prompt mistake across every connected provider, workspace, and token budget.
- The free scanner receipt gives a low-friction before/after artifact that a maintainer can paste into an issue or PR review before buying the deeper checklist bundle.

## Five-minute receipt for a LiteLLM-backed agent task

1. Run the free scanner from this repo before granting the agent write, shell, package-script, or gateway-config access.
2. Capture the Markdown receipt and look for Yellow/Red signals around `.env`, proxy config, Docker compose, workflow files, package scripts, MCP/tool config, or generated command execution.
3. Add this line to the agent handoff:

   > Do not edit LiteLLM gateway/provider config, budget/routing rules, workflow files, Docker compose, or secret-adjacent values until this preflight receipt is Green or the Yellow/Red items are explicitly acknowledged.

4. If the receipt is Green, skip the paid bundle for now.
5. If the receipt is Yellow/Red, buy the `${7}` pack here: <https://payhip.com/b/1nmxV> and use the paid checklist before the gateway-backed agent run proceeds.

## Quick example

```text
Agent task: "Wire our repo's test helper into the LiteLLM proxy and update provider fallback config."
Preflight result: Yellow
Reason: touched litellm_config.yaml, docker-compose.yml, .env.example, and package scripts in one run.
Action: pause, paste the receipt into the PR, then use the paid checklist to split config, secrets, and script changes before the agent continues.
```

## Buy / skip rule

- **Skip** if the scan is Green and the task only reads public docs or generated examples.
- **Buy the `$7` pack** if the scan is Yellow/Red because LiteLLM proxy config, provider credentials, budget/routing controls, Docker/workflow files, or package scripts are in scope.
