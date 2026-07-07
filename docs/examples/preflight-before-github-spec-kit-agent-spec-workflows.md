# GitHub Spec Kit agent spec workflow preflight proof

Unique marker: `GITHUB_SPEC_KIT_AGENT_SPEC_WORKFLOW_PROOF`

Verified public target: [github/spec-kit](https://github.com/github/spec-kit) — 💫 Toolkit to help you get started with Spec-Driven Development, 118483 GitHub stars, updated 2026-07-07T08:00:02Z.

## Why this buyer segment should care

Spec Kit teams turning specs into AI-agent implementation tasks are a tight first-buyer fit because spec-first repos still hand agents generated plans, scripts, CI, and secret-adjacent app config; buyers need a visible go/no-go receipt before the coding agent executes the spec. The public free repo now shows the exact workflow, and the paid pack is the small checkout when the receipt turns Yellow or Red.

## 60-second pre-agent receipt

```text
Buyer workflow: github/spec-kit
Before automation: run the free preflight over the repo branch that will receive the spec/agent change.
Green: docs-only or fixture-only edits; skip the paid pack.
Yellow: package scripts, CI, tool config, generated task files, dependency changes, deployment config, or customer-data paths; use the paid checklist before the agent run.
Red: credential writes, destructive commands, payment/KYC/tax/legal identity changes, or unsafe security work; stop and require owner review.
Seller proof: GITHUB_SPEC_KIT_AGENT_SPEC_WORKFLOW_PROOF
Paid pack: https://payhip.com/b/1nmxV
```

## Buy / skip trigger

- **Buy**: Buy when a Spec Kit implementation plan is about to be handed to Claude Code, Codex, Cursor, or a GitHub Action that can edit files, run package scripts, or touch deployment/API config.
- **Skip**: if the spec/agent run is documentation-only and has no write, shell, dependency, deployment, or secret-adjacent scope.

No affiliation with `github/spec-kit` is implied; this proof is a public buyer-specific mapping from the free scanner to a real AI-agent workflow.
