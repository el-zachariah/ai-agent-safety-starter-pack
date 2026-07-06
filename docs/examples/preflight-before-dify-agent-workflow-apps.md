# Preflight before Dify agent/workflow apps

**Dify agent/workflow app preflight proof.** Use this when a team using [`langgenius/dify`](https://github.com/langgenius/dify) or a Dify-style visual AI app builder is about to connect a workflow, agent, tool, dataset, API credential, webhook, or deployment script to a real repository or production workspace.

**Public target evidence captured this pulse:** `langgenius/dify` is live and non-archived at https://github.com/langgenius/dify; GitHub stars observed: `147917`; last updated: `2026-07-06T20:33:51Z`. Description observed: "Production-ready platform for agentic workflow development.".

## Why this matters before the first paid run

Dify makes the builder feel visual, but the risky parts are still concrete: provider keys, tool/function calls, HTTP nodes, datasets, workflow exports, deployment settings, package scripts, Docker files, and secret-adjacent environment values. A short local preflight receipt helps a developer decide whether the run is safe enough with the free scanner or needs the paid starter pack's repeatable checklist, hook examples, and reviewer prompts.

## 60-second receipt for Dify teams

1. Run the free lite scanner on the repo or deployment folder before giving a Dify workflow access to code, env values, webhooks, or tool endpoints.
2. Attach the receipt to the issue/PR/runbook that explains the workflow change.
3. Mark each flagged path as **run**, **ask first**, or **avoid** before the Dify app is allowed to call tools or deploy.
4. Keep the receipt with the workflow export so the next maintainer can repeat the check.

## Buy / skip trigger

- **Green:** keep using the free scanner and paste the receipt into the Dify runbook.
- **Yellow:** buy the $7 pack if the workflow touches provider keys, API connectors, package/Docker scripts, workflow files, or deployment config and you need a reusable approval note.
- **Red:** stop before connecting live credentials or deployment hooks; use the paid checklist/hook examples to turn the findings into explicit allow/deny rules.

```text
DIFY_AGENT_WORKFLOW_PROOF
Target workflow: Dify app / agent / workflow touching repo, connectors, or deployment scope
Free scan result: Green / Yellow / Red
Reviewed before launch: provider keys, tool endpoints, HTTP/webhook nodes, package scripts, Docker/deploy files, workflow exports, and secret-adjacent paths
Decision: run / ask first / avoid
Paid pack trigger: Yellow/Red when the team needs repeatable hooks, reviewer prompts, and handoff templates before the next run
```

Paid upgrade when the receipt is Yellow/Red: https://payhip.com/b/1nmxV
