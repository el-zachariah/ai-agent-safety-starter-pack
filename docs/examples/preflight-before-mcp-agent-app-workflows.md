# MCP Agent app workflow preflight proof

**Named buyer segment:** teams building MCP Agent apps before connecting MCP servers, tool calls, package scripts, filesystem access, model/provider environment variables, or deployment config to an agent run.

**Public target evidence captured:** [`lastmile-ai/mcp-agent`](https://github.com/lastmile-ai/mcp-agent) is public and not archived; observed stars `8410`; updated `2026-07-06T22:01:30Z`; description: "Build effective agents using Model Context Protocol and simple workflow patterns".

**Proof marker:** `MCP_AGENT_APP_WORKFLOW_PROOF`

## Why this matters before a paid handoff

MCP Agent app workflow teams are close to the exact checkout-start friction this product solves: a developer is about to let an AI workflow read repo context, call tools, run package scripts, or work near credential-adjacent settings. The free scanner gives a local receipt first; the paid `$7` starter pack is only positioned when the scan is Yellow/Red and the team needs a reusable handoff, reviewer prompt, report template, and destructive-command guardrail.

## 60-second preflight receipt

From the repo or workspace that will be handed to the agent:

```bash
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-mcp-agent.md
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-mcp-agent.json
```

Attach `agent-preflight-mcp-agent.md` to the issue, PR, runbook, or agent task before widening tool/shell/deploy scope.

## Buy / skip decision for this segment

- **Green:** docs-only or toy workflow; no package scripts, workflow edits, MCP/API tools, filesystem writes, browser/session access, or secret-adjacent config. Keep using the free scanner.
- **Yellow:** package scripts, workflow files, tool definitions, MCP/API connector config, generated commands, or deployment files are in scope. Buy the `$7` pack if a repeatable receipt and review checklist would save setup time.
- **Red:** `.env`/token-bearing config, production deploy paths, destructive shell commands, broad filesystem tools, or credentialed connectors are in scope. Buy the `$7` pack before the next agent run so the handoff and command guardrail are written down first.

Paid upgrade when the receipt is Yellow/Red: https://payhip.com/b/1nmxV

## Copy/paste handoff note

```text
MCP Agent app workflow preflight: ran the free AI Agent Safety lite scan before granting repo/tool/shell scope.
Receipt: agent-preflight-mcp-agent.md
Decision: Green / Yellow / Red
If Yellow/Red, use the $7 AI Agent Safety Starter Pack before the next run: https://payhip.com/b/1nmxV
Marker: MCP_AGENT_APP_WORKFLOW_PROOF
```
