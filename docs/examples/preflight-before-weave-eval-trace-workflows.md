# Weave eval/trace workflow preflight proof

**Named buyer segment:** teams using [`wandb/weave`](https://github.com/wandb/weave) or similar eval/observability workflows before exposing repository context, prompt/eval datasets, scoring scripts, trace exports, API-token config, deployment hooks, or agent-run receipts.

**Public target evidence captured 2026-07-06T20:34:37.833083-05:00:** `wandb/weave` is public and not archived, with 1105 GitHub stars observed, updated `2026-07-07T00:04:53Z`, description: "Weave is a toolkit for developing AI-powered applications, built by Weights & Biases.".

Marker: `WEAVE_EVAL_TRACE_PROOF`.

## Why this matters before Weights & Biases Weave eval/trace workflows

Eval and observability stacks are often the first place a team centralizes prompts, traces, test datasets, scoring scripts, and production-like run metadata. That is exactly the moment to require a local preflight receipt before an AI coding agent, evaluator, or CI job receives broader repo or credential scope.

Run the free scanner against the application repo or eval harness before widening access:

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > weave-eval-trace-workflows-preflight-receipt.md
```

## Green / Yellow / Red buy trigger

- **Green:** attach the free receipt to the eval/trace task and skip the paid pack for now.
- **Yellow:** review package scripts, prompt/eval datasets, workflow files, webhook config, tool/MCP/API connectors, and secret-adjacent paths before the next run.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need repeatable hooks, reviewer prompts, and handoff receipts before letting eval/observability automation touch real repo or credential scope.

## Copy-paste run ticket

```md
Weights & Biases Weave eval/trace workflows preflight receipt
- Target repo/eval harness: <repo/path>
- Eval or trace task: <Braintrust/Weave/Phoenix-style run>
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <read-only traces / tests only / no deploy / no secrets / no package scripts>
- Next gate: rerun preflight before enabling agent edits, webhooks, package scripts, or production credentials.
```

## What the paid bundle adds for Yellow/Red scans

The free proof keeps the funnel honest. The paid pack is for teams that hit Yellow/Red and want the repeatable command hook, reviewer checklist, and copy-paste receipts that make every eval/observability run start with the same safety gate.
