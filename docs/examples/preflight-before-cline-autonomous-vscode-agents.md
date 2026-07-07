# Preflight before Cline autonomous VS Code agents

Named buyer segment: small teams and solo builders who let Cline edit files, run terminal commands, call MCP tools, or modify repo state from VS Code.

Public segment evidence: GitHub API check during this pulse showed 64,317 stars for `https://github.com/cline/cline`. Cline's public repo describes it as: "Autonomous coding agent as an SDK, IDE extension, or CLI assistant.".

## Why this matters before checkout

A Cline user is already close to the paid pain: they are giving an AI agent repo-write and command-execution reach. The missing trust step is not another generic landing-page promise; it is a concrete receipt that says what the agent was allowed to touch before it touched it.

Use the free `/agent-preflight` command before a Cline task when:

- Cline is about to edit production-adjacent code, repo config, scripts, CI, or deployment files.
- You are using MCP servers or custom tools whose filesystem/network reach is not obvious.
- You need a quick artifact to paste into a PR, issue, or handoff before an autonomous patch lands.

Buy the $7 starter pack when you want the same preflight habit packaged as reusable checklists, buyer-facing receipts, and copy-paste policy language for real team workflows.

## One-minute Cline preflight example

```bash
/agent-preflight "Cline will update CI config and run tests in this repo; list the files, commands, network calls, secrets, and rollback checks that must be explicit before it starts."
```

Expected receipt shape:

```text
Agent task: Cline CI/config patch
Allowed files: .github/workflows/*, package/test config, docs linked to this change
Commands: test/lint only unless maintainer approves deploy/publish
Secrets: no token printing; no .env reads; no credential file edits
Network: package install only if lockfile diff is reviewed
Rollback: git diff + test output + one-line revert path before handoff
```

## Buy/skip trigger for Cline users

- **Buy** if Cline will touch CI, deployment, package-manager, MCP, or multi-file refactor paths and you want a reusable receipt template before the task starts.
- **Skip** if you only need a one-off prompt for a toy repo; use the free command and keep moving.

Paid bundle: <https://payhip.com/b/1nmxV>
Free repo/funnel: <https://el-zachariah.github.io/ai-agent-safety-starter-pack/>
