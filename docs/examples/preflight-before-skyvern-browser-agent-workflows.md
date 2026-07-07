# Preflight before Skyvern browser-agent workflows

Unique marker: `SKYVERN_BROWSER_AGENT_WORKFLOW_PROOF`

This customer proof is for teams evaluating or using [`Skyvern-AI/skyvern`](https://github.com/Skyvern-AI/skyvern) before browser tasks, credentials, forms, admin surfaces, package scripts, webhooks, deployment config, and secret-adjacent runtime settings enter an AI-agent run.

Target verification captured for this proof:

- Repository: `Skyvern-AI/skyvern`
- Public URL: https://github.com/Skyvern-AI/skyvern
- GitHub description: Automate browser based workflows with AI
- Stars observed: `22140`
- Updated at: `2026-07-07T10:23:19Z`
- Archived: `False`

## 60-second buyer check

Run the free scanner before handing this workflow a real repo, workspace, tool connector, or deployment surface:

```bash
python3 scripts/lite_preflight.py /path/to/repo --format markdown --output skyvern-browser-agent-workflows-preflight.md
```

Treat the result as a go/no-go receipt for the first agent run:

- **Green:** keep the free scanner receipt and run a narrow, read-only pilot.
- **Yellow:** buy the $7 AI Agent Safety Starter Pack before the agent gets write access, because the paid bundle adds handoff checklists, review-comment templates, red-flag actions, and reusable receipts for agent teams.
- **Red:** buy the $7 pack before continuing and require a maintainer sign-off receipt before any repo write, shell command, deployment hook, or credential-adjacent config enters the run.

## What this catches for Skyvern browser-agent workflow teams

- Browser tasks that can mutate external systems, submit forms, or touch money-adjacent pages.
- Credential/session handling that must stay out of agent-generated logs and receipts.
- Webhook/API integrations that turn browser observation into backend action.
- Package scripts and deployment config near automation code.
- Repo instructions that need a maintainer-approved stop/go receipt before unattended runs.

## Copy/paste preflight receipt

```text
Skyvern browser-agent workflow preflight receipt
Target repo: <repo/path>
Agent/workflow entrypoint: <agent, workspace, task, or tool entrypoint>
Free scanner result: Green / Yellow / Red
Top risk bucket: <package-scripts | workflow-files | env-secrets | MCP/API-tools | deployment-config>
Decision: <run read-only | buy/use paid checklist first | stop until maintainer approves>
Reviewer: <name/handle>
Timestamp: <UTC>
```

## Paid upgrade trigger

If the free scan is Yellow or Red, the paid pack is the fastest next step because it gives the team a repeatable handoff checklist, review-comment template, and red-flag action matrix instead of another generic AI-safety article.

Paid bundle: https://payhip.com/b/1nmxV
