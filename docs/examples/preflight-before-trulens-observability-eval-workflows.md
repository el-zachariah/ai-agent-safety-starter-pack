# TruLens observability/eval workflow preflight proof

**Named buyer segment:** TruLens observability/eval workflow teams using [`truera/trulens`](https://github.com/truera/trulens) or adjacent eval/observability workflows before repo context, feedback functions, eval datasets, app traces, provider keys, notebooks, CI workflows, package scripts, or deployment config enter an AI-assisted run.

**Public target evidence captured 2026-07-06T21:31:00-0500:** `truera/trulens` is public and not archived, with 3,423 GitHub stars observed, updated `2026-07-06T17:05:12Z`, description: 'Evaluation and Tracking for LLM Experiments and AI Agents'.

Marker: `TRULENS_OBSERVABILITY_EVAL_WORKFLOW_PROOF`.

## Why this matters before TruLens observability/eval workflow teams handoffs

TruLens-style eval and observability workflows sit close to app traces, feedback functions, provider keys, notebooks, and CI. A local preflight receipt makes the repo handoff safe before agent automation touches that surface.

Run the free scanner against the application repo, eval harness, dataset repo, notebook workspace, gateway wrapper, or deployment repo before widening agent access:

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > trulens-observability-eval-workflows-preflight-receipt.md
```

## Green / Yellow / Red buy trigger

- **Green:** attach the free receipt to the eval/observability change and skip the paid pack for now.
- **Yellow:** review package scripts, workflow files, prompt/eval artifacts, notebooks, API connectors, deploy files, and secret-adjacent paths before the next run.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need repeatable hooks, reviewer prompts, and handoff receipts before letting automation touch real repo, eval, trace, dataset, deployment, or credential scope.

## Copy-paste run ticket

```md
TruLens observability/eval preflight receipt
- Target repo/app/eval harness: <repo/path>
- Agent/eval task: <what the automation will read or edit>
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <tests only / no deploy / no secrets / no package scripts / no dataset writes>
- Next gate: rerun preflight before enabling agent edits, package scripts, workflow changes, dataset writes, provider-key access, or deployment changes.
```

## What the paid bundle adds for Yellow/Red scans

The free proof keeps the funnel honest. The paid pack is for teams that hit Yellow/Red and want the repeatable command hook, reviewer checklist, and copy-paste receipts that make every eval, observability, agent, gateway, or dataset run start with the same safety gate.

No affiliation with `truera/trulens` is implied; this is a buyer-specific proof showing how the public free scanner and paid starter pack map to a real public workflow.
