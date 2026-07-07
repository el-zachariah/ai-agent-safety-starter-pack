# Braintrust eval/observability workflow preflight proof

**Named buyer segment:** Braintrust eval/observability workflow teams using [`braintrustdata/braintrust-sdk-javascript`](https://github.com/braintrustdata/braintrust-sdk-javascript) or adjacent eval/observability workflows before eval prompts, experiment logs, datasets, scorer code, trace exports, provider keys, CI workflows, package scripts, or deployment config enter an AI-assisted run.

**Public target evidence captured 2026-07-06T21:46:05-05:00:** `braintrustdata/braintrust-sdk-javascript` is public and not archived, with 25 GitHub stars observed, updated `2026-07-06T20:18:24Z`, description: 'JavaScript Tracing & Evals library for Braintrust'.

Marker: `BRAINTRUST_EVAL_OBSERVABILITY_WORKFLOW_PROOF`.

## Why this matters before Braintrust eval/observability workflow teams handoffs

Braintrust eval/observability workflow work sits close to prompts, traces, datasets, eval/scoring code, provider credentials, package scripts, and deployment surfaces. A local preflight receipt lets a team decide what an agent may read, edit, test, or deploy before automation gets broad repo access.

Run the free scanner against the application repo, eval harness, dataset workspace, gateway wrapper, notebook repo, or deployment repo before widening agent scope:

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > braintrust-eval-observability-workflows-preflight-receipt.md
```

## Green / Yellow / Red buy trigger

- **Green:** attach the free receipt to the eval/observability change and skip the paid pack for now.
- **Yellow:** review eval prompts, experiment logs, datasets, scorer code, trace exports, provider keys, CI workflows, package scripts, or deployment config before the next run.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need repeatable hooks, reviewer prompts, and handoff receipts before letting automation touch real repo, eval, trace, dataset, deployment, or credential scope.

## Copy-paste run ticket

```md
Braintrust eval/observability workflow preflight receipt
- Target repo/app/eval harness: <repo/path>
- Agent/eval task: <what automation will read or edit>
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <tests only / no deploy / no secrets / no package scripts / no dataset writes>
- Next gate: rerun preflight before enabling agent edits, package scripts, workflow changes, dataset writes, provider-key access, or deployment changes.
```

## What the paid bundle adds for Yellow/Red scans

The free proof keeps the funnel honest. The paid pack is for teams that hit Yellow/Red and want the repeatable command hook, reviewer checklist, and copy-paste receipts that make every eval, observability, agent, gateway, or dataset run start with the same safety gate.

No affiliation with `braintrustdata/braintrust-sdk-javascript` is implied; this is a buyer-specific proof showing how the public free scanner and paid starter pack map to a real public workflow.
