# Promptfoo LLM eval/red-team workflow preflight proof

Named customer segment: teams using [`promptfoo/promptfoo`](https://github.com/promptfoo/promptfoo) or promptfoo-style LLM eval, guardrail, and agent test workflows before real repository files, package scripts, CI workflows, MCP/API tools, browser actions, or secret-adjacent configuration enter scope.

Target evidence captured 2026-07-06T11:50:03-05:00: `promptfoo/promptfoo` is public, not archived, observed stars `22972`, updated `2026-07-06T16:33:44Z`, description: "Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, DeepSeek, and more. Simple declarative configs with command line and CI/CD integration.  Used by OpenAI and Anthropic.".

## Why this proof matters

Promptfoo users already think in test cases, eval reports, assertions, and repeatable checks. The missing buyer-trust bridge is a local repo preflight receipt before an eval or red-team harness is allowed to execute agent tools, touch package scripts, read `.env`-adjacent config, mutate fixtures, or run in CI against a real product repo.

Run the free scanner before the first promptfoo-backed agent/eval run that can see real repo context or secrets-adjacent files:

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > promptfoo-agent-eval-preflight-receipt.md
```

## Green / Yellow / Red buy trigger

- **Green:** keep the free receipt with the promptfoo report and skip the paid pack for now.
- **Yellow:** review package scripts, workflow files, MCP/API/tool config, prompt fixtures, and `.env`-adjacent paths before widening eval or agent scope.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if the team needs the full hook bundle, reviewer checklist, and reusable handoff receipts before eval tooling or agents execute in the repo.

## Copy-paste receipt for the first eval run

```md
Promptfoo eval workflow preflight receipt
- Repo scanned before promptfoo/agent execution: <repo/path>
- Eval or red-team suite: <suite name>
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <read-only / fixtures only / tests only / no deploy / no secrets>
- Next gate: rerun before adding shell-capable agents, CI credentials, browser tools, deploy scripts, or production-like secrets.
```

## What the paid bundle adds for Yellow/Red scans

The public scanner proves the workflow without requiring a purchase. The $7 pack is for promptfoo teams that hit Yellow/Red and want ready-to-drop command hooks, reviewer prompts, and handoff receipts so every LLM eval, guardrail, or agent red-team run starts with the same safety gate instead of an improvised warning.
