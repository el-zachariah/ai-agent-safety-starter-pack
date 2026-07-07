# Ragas eval/dataset workflow preflight proof

**Named buyer segment:** Ragas eval/dataset workflow teams using [`vibrantlabsai/ragas`](https://github.com/vibrantlabsai/ragas) or adjacent eval/observability workflows before repo context, eval datasets, scoring scripts, judge/model provider keys, notebooks, CI workflows, trace exports, package scripts, or deployment config enter an AI-assisted run.

**Public target evidence captured 2026-07-06T21:19:28-0500:** `vibrantlabsai/ragas` is public and not archived, with 14,689 GitHub stars observed, updated `2026-07-07T00:08:06Z`, description: 'Supercharge Your LLM Application Evaluations 🚀'.

Marker: `RAGAS_EVAL_DATASET_WORKFLOW_PROOF`.

## Why this matters before Ragas eval/dataset workflow teams handoffs

Ragas-style eval pipelines sit next to datasets, judge prompts, model-provider keys, scoring scripts, CI, trace exports, and notebooks. That is exactly where a cheap local preflight receipt can stop a Yellow/Red handoff before an AI agent or eval runner widens access.

Run the free scanner against the application repo, eval harness, dataset repo, notebook workspace, gateway wrapper, or deployment repo before widening agent access:

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > ragas-eval-dataset-workflows-preflight-receipt.md
```

## Green / Yellow / Red buy trigger

- **Green:** attach the free receipt to the eval/observability change and skip the paid pack for now.
- **Yellow:** review package scripts, workflow files, prompt/eval artifacts, notebooks, API connectors, deploy files, and secret-adjacent paths before the next run.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need repeatable hooks, reviewer prompts, and handoff receipts before letting automation touch real repo, eval, trace, dataset, deployment, or credential scope.

## Copy-paste run ticket

```md
Ragas eval/dataset preflight receipt
- Target repo/app/eval harness: <repo/path>
- Agent/eval task: <what the automation will read or edit>
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <tests only / no deploy / no secrets / no package scripts / no dataset writes>
- Next gate: rerun preflight before enabling agent edits, package scripts, workflow changes, dataset writes, provider-key access, or deployment changes.
```

## What the paid bundle adds for Yellow/Red scans

The free proof keeps the funnel honest. The paid pack is for teams that hit Yellow/Red and want the repeatable command hook, reviewer checklist, and copy-paste receipts that make every eval, observability, agent, gateway, or dataset run start with the same safety gate.

No affiliation with `vibrantlabsai/ragas` is implied; this is a buyer-specific proof showing how the public free scanner and paid starter pack map to a real public workflow.
