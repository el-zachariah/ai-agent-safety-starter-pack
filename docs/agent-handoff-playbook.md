# Agent handoff playbook for Claude Code, Codex, Cursor, and MCP-backed agents

Use this free playbook when you are about to give an AI coding agent tool access in a repository you did not just audit.

The goal is not to make the repo "secure" in one pass. The goal is to create a short, repeatable handoff note that tells the agent what it can read, what it can run, and what needs a human check first.

## 10-minute handoff flow

1. **Run the lite preflight scanner.**

   ```bash
   python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-lite.json
   python3 agent_preflight_lite.py /path/to/repo > agent-preflight-lite.md
   ```

2. **Read the instruction/config files first.**

   Open the files flagged as agent instructions or tool config: `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, `.mcp.json`, `.claude/settings.json`, and similar files.

3. **Make a run/avoid list before the agent starts.**

   - Allowed: safe read-only inspection, targeted edits, unit tests you reviewed.
   - Ask first: install scripts, deploy scripts, migrations, package manager lifecycle scripts, MCP server changes.
   - Never without a human: destructive shell commands, credential changes, force pushes, production deploys.

4. **Give the agent a short operating note.**

   Paste something like:

   > Before changing files, read `agent-preflight-lite.md`. Do not run install, deploy, migration, cleanup, force-push, credential, or Docker socket commands without asking. If a command includes `rm -rf`, `curl | sh`, `chmod 777`, `docker.sock`, or production credentials, stop and explain the risk first.

5. **Save the handoff with the repo/task.**

   Keep the preflight output next to the ticket, issue, or worktree notes so the next agent run starts with context instead of guessing.

## When to upgrade to the $7 starter pack

The free scanner is enough for a quick first look. Upgrade when you want the repeatable workflow pieces instead of rebuilding them every time:

- full repo preflight mini with richer report structure,
- destructive-command hook examples,
- report templates for agent task handoff,
- buyer quickstart and verification scripts,
- demo risky repo and expected outputs.

Paid bundle: https://payhip.com/b/1nmxV

## Limits

This is not a sandbox, malware scanner, secret scanner, or security audit. Treat it as a practical pre-agent checklist that helps you slow down before giving tool access to automation.
