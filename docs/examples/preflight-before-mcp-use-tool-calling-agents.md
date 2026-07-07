# Preflight before MCP-use tool-calling agents

Marker: `mcp-use-tool-calling-agents-proof`

Public target verified: [`mcp-use/mcp-use`](https://github.com/mcp-use/mcp-use)  
Stars observed during this deadline pulse: `10263`  
Updated at verification: `2026-07-06T23:40:01Z`  
Description: The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.

## Buyer this is for

This proof is for teams using MCP-use to connect LLM agents to MCP servers, repo tools, browser tools, local files, package scripts, or credential-adjacent connectors.

MCP-use turns “just ask the model” into real tool calls. A buyer needs proof that the preflight pack catches the repo/tool boundary before those calls touch private code, workflows, or credentials.

## Free preflight receipt

Before an agent gets tool access, run the free lite scanner and keep the receipt with the task handoff:

```bash
python3 scripts/agent_safety_lite.py --path . --format markdown > preflight-receipt.md
python3 scripts/agent_safety_lite.py --path . --format json > preflight-receipt.json
```

Look first at:

- `mcp.json, .mcp.json, server configs, tool allowlists, package scripts, workflow files, and .env-adjacent connector settings`
- tool permissions that can read or mutate a repo;
- package/install/test commands an agent may run automatically;
- API keys, OAuth tokens, workspace credentials, browser profiles, or webhook URLs near the workflow;
- deployment or CI config that could turn a local agent action into production side effects.

## Green / Yellow / Red buy trigger

- **Green:** no sensitive configs, no package-script/tool boundary, no credential-adjacent files, and the agent is only reading a toy repo. Use the free scanner and skip the paid pack for now.
- **Yellow:** the MCP server/tool scan is Yellow or Red before an agent can call repo, browser, shell, database, or API-backed tools. Buy the $7 pack for the filled review checklist, command hook, JSON receipt template, and copy-paste handoff wording.
- **Red:** secrets, production connectors, write-capable tools, deployment workflows, browser/admin sessions, or payment/customer data are in scope. Stop the agent run, buy the pack, and require a signed-off preflight receipt before continuing.

## Copy-paste handoff check

> I am about to run `mcp-use/mcp-use`-style tool-calling agent work in this repo. I need a Green/Yellow/Red preflight receipt before granting tool scope. If the receipt is Yellow or Red, use the paid Agent Safety Starter Pack checklist and command hook before continuing.

## Why this makes the paid product concrete

A generic safety product feels optional. This proof turns it into a specific buying moment: when a MCP-use tool-calling agent teams owner sees Yellow/Red before granting tool scope, the $7 pack is the fastest way to get a reusable receipt, hook, and reviewer language without inventing a process.
