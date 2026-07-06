# Langfuse observability/eval pipeline preflight proof

Target verified: https://github.com/langfuse/langfuse

This is for teams using Langfuse traces, prompts, datasets, evals, or score dashboards while letting Claude Code, Codex, Cursor, or other repo agents change instrumentation and evaluation code. The first-dollar trust problem is simple: if the agent edits observability or eval wiring without a preflight receipt, reviewers cannot quickly tell whether the change touched secrets, CI, deployment hooks, or prompt/eval fixtures.

## One-minute buyer receipt

1. Run the free scanner before the agent edits the Langfuse instrumentation/eval repo:

   ```bash
   python3 agent_preflight_lite.py /path/to/langfuse-or-eval-repo --json > langfuse-agent-preflight.json
   python3 agent_preflight_lite.py /path/to/langfuse-or-eval-repo > langfuse-agent-preflight.md
   ```

2. Paste the Green / Yellow / Red result into the PR or handoff note.
3. If the scan is Yellow or Red, require a human answer before the agent can mutate `.env*`, CI, deployment config, eval datasets, scoring scripts, prompt registries, or webhook/API-token handling.
4. Keep the receipt beside the Langfuse trace/eval change so a maintainer can review the risk before reading the full diff.

## Why this is relevant to Langfuse teams

Langfuse users often centralize LLM traces, prompt versions, datasets, eval scoring, and production observability. That means an autonomous coding agent can create costly mistakes even when the app still builds: exposed API keys, changed dataset baselines, broken eval thresholds, or prompt/deployment drift. A tiny preflight receipt gives the reviewer a concrete yes/no checkpoint before the agent work becomes expensive to unwind.

## When to buy the $7 starter pack

Buy the $7 starter pack only if you want the ready-to-use review templates, copy/paste handoff language, maintainer receipts, and escalation checklists instead of building your own from this free proof: https://payhip.com/b/1nmxV

Skip it if you only need this single free scanner example.
