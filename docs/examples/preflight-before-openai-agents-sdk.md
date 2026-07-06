# Preflight before OpenAI Agents SDK tool agents

**OpenAI Agents SDK tool-agent preflight proof.** Use this when a team is about to let an OpenAI Agents SDK workflow call tools, MCP servers, local scripts, package commands, deployment helpers, or API-backed actions from a real repository.

Target evidence checked during this pulse: [`openai/openai-agents-python`](https://github.com/openai/openai-agents-python) was public on GitHub with 27667 stars and updated at `2026-07-06T00:11:04Z`. Description observed: 'A lightweight, powerful framework for multi-agent workflows'.

## Why this buyer should care

OpenAI Agents SDK projects often cross the exact boundary where a small mistake becomes expensive: tool calls, handoffs, MCP servers, hosted/local execution, environment variables, package scripts, and repo-specific instructions. Before granting that scope, a maintainer needs a receipt that says what the agent can touch and whether the run is Green, Yellow, or Red.

## Five-minute free preflight

1. Run the free scanner against the repo or branch before connecting the agent runtime:

   ```bash
   python3 agent_preflight_lite.py --repo /path/to/repo --output-md preflight-openai-agents.md --output-json preflight-openai-agents.json
   ```

2. In the generated receipt, look for:
   - repo-level agent instructions or workflow config;
   - MCP/tool config, local package scripts, and shell-capable helpers;
   - `.env` examples, deployment files, webhook/API surfaces, or credential-adjacent files;
   - generated risk decision: **Green**, **Yellow**, or **Red**.
3. Paste the Markdown receipt into the PR, issue, or internal approval note before the OpenAI Agents SDK workflow receives repo or tool scope.

## When to buy the $7 pack

Buy the paid pack if the receipt is **Yellow/Red**, if the OpenAI Agents SDK workflow will run package scripts or MCP/tool calls, or if you need the copy-paste hooks, review templates, and remediation checklists that turn the receipt into a repeatable team gate: https://payhip.com/b/1nmxV

Skip it for now if the receipt is **Green**, the agent has no repo write/shell/API scope, and a one-off free scan is enough.

## Copy-paste approval note

> I ran the agent preflight before granting OpenAI Agents SDK tool scope. Current decision: `<Green|Yellow|Red>`. If Yellow/Red, I will either reduce tool scope, sandbox execution, or use the paid starter pack checklist before enabling repo/package-script/API access.

Related free repo assets: [`/agent-preflight`](../../commands/agent-preflight.md), [review-comment template](../preflight-review-comment-template.md), and [trust/support notes](../trust-and-support.md).
