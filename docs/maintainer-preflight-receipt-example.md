# Maintainer preflight receipt example for AI-agent PRs

This is a concrete proof-of-work example for maintainers, plugin directory curators, and small teams who let Claude Code, Codex, Cursor, or MCP-backed agents touch real repositories.

Use it when a contributor says an AI coding agent will open a PR, run tests, edit package scripts, or follow repo-local instructions. The goal is not to block the work; it is to get a visible receipt before the agent gets shell access.

## The maintainer ask

Paste this before the agent run or in the PR description template:

```markdown
Before the AI agent gets shell access, please attach a repo preflight receipt:

1. Run the free scanner:
   `python3 agent_preflight_lite.py . --json > agent-preflight.json`
2. Summarize the Green / Yellow / Red decision and risk buckets.
3. List what the agent may run, what needs maintainer approval, and what it must not touch.

If the result is Yellow/Red, include the handoff rules before continuing.
```

## Sample receipt from the included risky demo repo

```markdown
### AI-agent preflight receipt

Repo: examples/sample-risky-repo
Decision: Red — set guardrails before tool access

Risk buckets found:
- Agent instructions: AGENTS.md may steer the agent.
- Secret-adjacent files: .env-style material should be excluded.
- Package scripts/workflows: install/test scripts deserve review before execution.
- Risky shell patterns: curl-piped install and destructive delete examples must not run unattended.

Allowed before approval:
- Read source files and documentation.
- Run the lite scanner and non-mutating inspection commands.
- Draft the change plan and test plan.

Must ask first:
- package install, build, test, deploy, migration, or networked commands.
- changes to MCP/Cursor/Claude config, CI workflows, or package scripts.

Must not do:
- delete files, rewrite history, force push, print secrets, or run curl-piped shell commands.
```

## Why this lowers checkout friction

A buyer does not need another abstract checklist. They need confidence that the pack turns into an immediate maintainer-facing workflow.

The free repo gives the public scanner and this receipt shape. The paid `$7` bundle is for maintainers or teams who want the same handoff to be repeatable instead of rebuilding it every time:

- full repo preflight mini,
- destructive-command hook examples,
- buyer quickstart,
- report templates,
- demo risky repo and generated report,
- local verifier scripts.

Buy only when the scan is Yellow/Red and you want the reusable hook/report workflow now: <https://payhip.com/b/1nmxV>
