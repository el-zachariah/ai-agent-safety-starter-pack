# Preflight before Claude Code GitHub Action workflows

`CLAUDE_CODE_ACTION_GITHUB_WORKFLOW_PROOF`

Target verified: [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action) is public, not archived, observed at **8,258 stars**, updated `2026-07-06T08:34:42Z`. Description from GitHub: 'Claude Code GitHub Action'.

## Who this is for

Teams using `anthropics/claude-code-action` or similar Claude Code GitHub Actions before the bot can comment on PRs, inspect repository context, propose edits, run package scripts, or use workflow-provided credentials.

A GitHub Action agent feels safer than a local terminal session, but it can still inherit repo permissions, CI secrets, workflow triggers, and generated shell commands. This proof gives a first buyer a concrete way to decide whether the free scan is enough or whether the reusable $7 handoff/guardrail pack is worth buying.

## Free preflight pass

Run the public scanner before enabling or broadening the workflow:

```bash
python3 agent_preflight_lite.py /path/to/repo --json
```

Review these before the action runs on live pull requests:

- `.github/workflows/*` files that define the Claude Code Action trigger, permissions, checkout depth, and secrets exposure.
- `CLAUDE.md`, `AGENTS.md`, `.claude/`, MCP config, or repo instructions that the action may follow.
- `package.json`, shell scripts, deploy scripts, and generated commands the bot may ask CI to run.
- `.env`, token files, cloud deploy config, and other secret-adjacent paths that should be excluded or sanitized.

## Claude Code Action handoff receipt

Copy this into the PR/issue where the action will run:

```text
Claude Code Action preflight receipt
Target: anthropics/claude-code-action workflow in this repo
Scan result: Green / Yellow / Red
Reviewed workflow files: .github/workflows/<name>.yml
Run without asking: tests, formatters, read-only checks
Ask first: dependency installs, package publish/deploy steps, workflow permission changes
Never touch: .env, production credentials, signing keys, payment/KYC files
Decision: proceed / tighten workflow / stop and add guardrails
```

## Buy / skip trigger

- **Skip buying for now** if the scan is Green and the action is limited to read-only review comments.
- **Buy the $7 pack** at https://payhip.com/b/1nmxV if the scan is Yellow/Red, the workflow can run shell/package/deploy commands, or the action is allowed to edit files in a real repo.

The paid pack adds the reusable preflight mini, destructive-command hook, report templates, demo risky repo, and verification scripts so every Claude Code Action run can leave a repeatable safety receipt instead of an improvised checklist.
