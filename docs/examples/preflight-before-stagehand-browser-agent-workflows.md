# Stagehand browser-agent workflow preflight proof

Named buyer segment: teams using [`browserbase/stagehand`](https://github.com/browserbase/stagehand) / Stagehand-style browser automation agents before giving them authenticated browser sessions, localhost apps, forms, admin surfaces, package scripts, or secret-adjacent config.

Public target verified before this proof: [`browserbase/stagehand`](https://github.com/browserbase/stagehand) is active and not archived, with **23379** GitHub stars observed, updated `2026-07-06T14:39:00Z`. Description: The SDK For Browser Agents

Marker: `STAGEHAND_BROWSER_AGENT_WORKFLOW_PROOF`

## Why this buyer hesitates before checkout

Browser-agent users can see the risk quickly: a Stagehand task that starts as a harmless web interaction can inherit logged-in state, fill forms, click destructive admin controls, run local dev servers, or touch repo scripts before anyone writes down the approval boundary. That is the exact trust gap this starter pack is meant to close.

## 60-second free preflight before a Stagehand run

Run the free scanner against the repo or workspace that contains the Stagehand task, browser credentials, MCP/tool config, app code, and package scripts:

```bash
python3 agent_preflight_lite.py /path/to/stagehand-workspace --format markdown > agent-preflight-stagehand.md
python3 agent_preflight_lite.py /path/to/stagehand-workspace --format json > agent-preflight-stagehand.json
```

Attach the Markdown receipt to the issue, PR, or task before the browser agent receives a logged-in page, localhost URL, form target, admin route, or write-enabled tool.

## Buy / skip trigger for the $7 pack

- **Green receipt:** skip the paid pack for now. Keep the free receipt with the task and rerun it when Stagehand scope changes.
- **Yellow receipt:** buy the $7 pack at https://payhip.com/b/1nmxV if the scan flags browser automation touching package scripts, workflow files, MCP/API config, localhost services, or secret-adjacent paths.
- **Red receipt:** buy the $7 pack before running the agent. Use the included hook/checklist/reviewer prompts to freeze approvals, command scope, and rollback notes before a browser session can mutate real data.

## Copy-paste handoff receipt

```text
Stagehand browser-agent preflight
Target repo/app:
Agent task:
Browser/session scope:
Localhost or production surface:
Package scripts/workflows in scope:
MCP/API/tool config in scope:
Secrets/admin/write surfaces found:
Free scan result: Green / Yellow / Red
Decision: skip paid pack / buy $7 pack before run
Receipt owner:
Next review date:
```

## What the paid bundle adds for Yellow/Red receipts

The paid bundle turns the free scan into a repeatable gate: a repo preflight hook, a reviewer prompt, an agent handoff checklist, and a purchase-backed template for recording exactly which Stagehand browser actions are allowed before the agent touches logged-in state or real customer/admin data.
