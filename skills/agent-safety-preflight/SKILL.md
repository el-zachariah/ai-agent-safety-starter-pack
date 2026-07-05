---
name: agent-safety-preflight
description: Run a local AI-agent repo preflight before Claude Code, Codex, Cursor, MCP tools, or hook/TDD loops get command access; use when you need a Green/Yellow/Red receipt for repo instructions, MCP/Cursor/Claude config, package scripts, workflows, secret-adjacent files, and risky shell hooks.
---

# Agent Safety Preflight

Use this skill before handing a repository to an autonomous coding agent, Claude Code hook, Codex/Cursor workflow, MCP-backed toolchain, or long-running TDD guard loop.

## What this does

- Scans the current repository locally; no hosted service and no secrets upload.
- Flags agent instruction files, MCP/Cursor/Claude configs, package scripts, GitHub Actions, secret-adjacent files, and risky shell patterns.
- Produces a short Green / Yellow / Red preflight receipt that can be pasted into a PR, issue, or run log before the agent receives tool access.
- Points users to the free lite scanner first; the paid bundle is only useful when the scan is Yellow/Red and the team wants reusable templates, hooks, and verification assets.

## Quick start

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git /tmp/agent-preflight
python3 /tmp/agent-preflight/agent_preflight_lite.py .
python3 /tmp/agent-preflight/agent_preflight_lite.py . --json
```

## Receipt template

```markdown
Agent preflight receipt
- Repo checked: <repo/path>
- Agent/tool about to run: <Claude Code / Codex / Cursor / MCP / hook loop>
- Decision: Green / Yellow / Red
- Risk buckets found: <agent instructions, MCP/Cursor/Claude config, package scripts, workflows, secret-adjacent files, risky shell>
- Commands allowed without asking: <install/test/read-only commands>
- Commands that must ask first: <deploy, destructive, credential, production, network, long-running background>
- Files/tools excluded before agent access: <paths or none>
```

## Buy / skip rule

Skip the paid bundle if the free scan is Green and a one-off note is enough. Buy the $7 workflow bundle when the scan is Yellow or Red and you want the reusable report template, destructive-command hook, buyer quickstart, demo risky repo, and verifier for repeated agent runs.
