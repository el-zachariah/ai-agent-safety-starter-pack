# Preflight before n8n AI workflow automation

Named buyer proof for teams using **n8n**, self-hosted workflow automation, or low-code AI workflows before they connect credentials, webhooks, APIs, databases, local repos, package scripts, or deployment environments to an agentic workflow.

## Public target evidence

- Target: [`n8n-io/n8n`](https://github.com/n8n-io/n8n)
- Observed stars at proof build: `195308`
- Observed updated_at: `2026-07-05T23:23:20Z`
- Description observed: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

## Why this buyer should care

n8n-style workflows often become the place where API credentials, webhook triggers, database writes, browser/API calls, and custom code nodes meet. The risky moment is not after a workflow is already live; it is when a team lets an AI agent or automation builder inspect a repo, suggest package-script changes, edit workflow JSON, wire MCP/API tools, or touch `.env`-adjacent configuration.

The free lite scanner in this repo gives a quick Green / Yellow / Red receipt before that handoff. The paid **AI Agent Safety Starter Pack** turns that receipt into a repeatable review artifact with checklist, hook, and copy-paste handoff language.

## 60-second n8n workflow preflight

Use this before giving an AI assistant or workflow automation builder broad context:

1. Run the free scanner against the repo or workflow-support folder before the agent sees secrets or gets write scope.
2. Treat these as **Yellow/Red** triggers for buying the $7 pack: `.env` examples with real-looking tokens, workflow exports with credential IDs, webhook URLs, custom code nodes, Docker/compose files, package scripts, MCP/server config, or deploy scripts.
3. Paste the receipt into the PR/issue/task before letting the agent continue.
4. If the scan is Green, skip the paid pack for now; if Yellow/Red, use the paid checklist + hook to make the handoff repeatable.

## Buy / skip decision for n8n teams

- **Buy the $7 pack** if an n8n or low-code agent workflow touches repo files, package scripts, `.env` values, webhook/API credentials, MCP/tool config, browser profiles, or deployment paths.
- **Skip it** if the workflow is a toy demo with no repo access, no real credentials, and no persistent automation.

Paid pack: [https://payhip.com/b/1nmxV](https://payhip.com/b/1nmxV)
