# Preflight before CopilotKit in-app AI copilot proof

Target buyer segment: teams using CopilotKit to wire in-app AI copilots, frontend actions, API-backed tools, and agentic product workflows.

Public target evidence checked during this pulse: [`CopilotKit/CopilotKit`](https://github.com/CopilotKit/CopilotKit) is public and not archived, with 35804 GitHub stars and latest update timestamp `2026-07-06T15:35:33Z`. Description observed: 'The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more.  Makers of the AG-UI Protocol'.

## Why this is a checkout-start trust proof

A CopilotKit in-app AI copilot proof can look like ordinary product UI work until it receives tool/action scope. At that point the repo may expose frontend action handlers, API routes, auth/session scope, vector/knowledge connectors, deployment env, package scripts, and secret-adjacent config. This page gives that exact buyer a public, copy-paste receipt before buying anything, so the paid bundle feels like a concrete workflow upgrade rather than a cold checkout page.

## 60-second free scan

```bash
python3 agent_preflight_lite.py /path/to/repo
python3 agent_preflight_lite.py /path/to/repo --json
```

Look for these before the assistant/copilot gets real action scope:

- agent or assistant instruction files that steer tool behavior,
- package scripts, workflow files, or deploy commands the assistant may trigger,
- API/tool config, MCP-like connectors, webhook handlers, or backend action routes,
- `.env`, provider keys, auth/session config, database URLs, or other secret-adjacent paths,
- browser, CI, or production actions that need a human approval line.

## Copy-paste handoff receipt

```text
COPILOTKIT_IN_APP_AI_COPILOT_PROOF
Target: CopilotKit/CopilotKit
Free scan result: Green / Yellow / Red
Copilot/assistant scope requested: <repo paths, action handlers, API routes, tools, CI, deployment, data connectors>
Allowed without asking: <read-only files, safe tests, docs, local scan commands>
Must ask before: <package install/deploy, credentialed APIs, database writes, auth/session changes, destructive shell, production webhooks>
Yellow/Red reason: <2+ risk buckets, secret-adjacent config, package scripts, workflow edits, tool/API scope>
Decision: if Yellow/Red, use the paid starter-pack templates + destructive-command hook before granting tool access; if Green, keep using the free scanner and normal review.
Paid workflow link if Yellow/Red: https://payhip.com/b/1nmxV
```

## Buy / skip trigger for this segment

- **Buy the $7 pack** when the scan is Yellow/Red because frontend action handlers, API routes, auth/session scope, vector/knowledge connectors, deployment env, package scripts, and secret-adjacent config are in scope and the team needs a repeatable handoff, report template, and destructive-command guardrail before the assistant/copilot acts.
- **Skip buying for now** when the scan is Green and the assistant has no write-capable tools, no secret-adjacent config, no risky scripts, and no production-facing actions.

CopilotKit teams should run the free scan before an in-app copilot receives action/tool scope, then buy the $7 pack only when the receipt is Yellow/Red.
