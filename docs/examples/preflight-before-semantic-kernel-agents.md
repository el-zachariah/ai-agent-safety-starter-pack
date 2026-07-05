# Preflight before Semantic Kernel agent framework runs

Customer segment: teams building with [`microsoft/semantic-kernel`](https://github.com/microsoft/semantic-kernel), Semantic Kernel agents, planners, plugins/functions, memory connectors, or tool-calling workflows before the agent receives repo, shell, API, or package-script scope.

Public target evidence captured 2026-07-05: `microsoft/semantic-kernel` was live, non-archived, recently updated, and publicly visible with 28k+ stars. The point of this proof is not to audit that upstream repo. It gives Semantic Kernel users a concrete receipt to run against their own application repo before widening agent scope.

## Why this buyer should care

Semantic Kernel projects often combine:

- Kernel plugins/functions that can call local code or external services.
- Planners or agents that choose tools from natural-language instructions.
- Memory/vector-store connectors and API clients.
- `.env`, `appsettings.json`, notebook, container, package, or CI files that may contain secret-adjacent configuration.
- Test/build/deploy scripts an AI coding agent may try to run while wiring the agent workflow.

That is exactly when a 5-minute preflight receipt is cheaper than cleaning up a confused agent run.

## Free 5-minute receipt

Run the free scanner from this repo before the Semantic Kernel agent gets broad context:

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/semantic-kernel-app --json > agent-preflight-semantic-kernel.json
python3 agent_preflight_lite.py /path/to/semantic-kernel-app > agent-preflight-semantic-kernel.md
```

Attach the Markdown receipt to the task, PR, or run ticket.

## Example Yellow handoff

```text
Repo: semantic-kernel-customer-support-agent
Agent surface: Semantic Kernel planner + plugins + memory connector
Decision: Yellow
Risk buckets: agent/workflow config, package scripts, secret-adjacent config, workflow files
May run: unit tests, focused lint, local sample prompts with fake keys
Must ask first: changing plugin permissions, reading real .env values, migrations, deploy scripts, paid API calls
Must not touch: production keys, customer data, cloud credentials, billing/admin surfaces
Next step: use the full $7 workflow if the agent will edit plugin/tool code or run package/deploy scripts repeatedly.
```

## Buy / skip trigger

Skip the paid pack if the free scan is Green and the agent only reads code. Buy the [$7 starter pack](https://payhip.com/b/1nmxV) when the scan is Yellow/Red and you need a reusable report template, destructive-command hook, and verifier before Semantic Kernel agents, planners, plugins, or connectors run against a real repo.
