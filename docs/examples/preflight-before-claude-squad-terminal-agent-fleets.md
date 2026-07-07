# Preflight before Claude Squad terminal-agent fleets

Customer segment: teams using [`smtg-ai/claude-squad`](https://github.com/smtg-ai/claude-squad) to manage multiple AI terminal agents such as Claude Code, Codex, OpenCode, and Amp before those agents edit a real repository, run shell/package commands, or fan out across task branches.

Public target evidence checked in this pulse: `smtg-ai/claude-squad` is public and not archived, showed 8,048 GitHub stars, was last updated `2026-07-07T03:48:17Z`, and describes itself as: "Manage multiple AI terminal agents like Claude Code, Codex, OpenCode, and Amp.".

Why this proof exists: Claude Squad-style workflows multiply the exact trust problem that blocks a first purchase. A buyer may be about to let several terminal agents inherit repo instructions, package scripts, workflow files, MCP/tool config, and secret-adjacent paths. The free scanner gives them a local receipt first; the paid $7 pack is the fast upgrade when that receipt turns Yellow/Red and they need reusable run rules, hook examples, and review-comment templates.

## 60-second Claude Squad preflight

Run the free scanner before starting the terminal-agent fleet:

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-claude-squad.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-claude-squad.md
```

Attach the Markdown receipt to the Claude Squad session notes before assigning parallel tasks.

## Pasteable fleet receipt

```text
CLAUDE_SQUAD_TERMINAL_AGENT_FLEET_PROOF
Target repo: <repo URL or local path>
Agent fleet: Claude Code / Codex / OpenCode / Amp workers via Claude Squad
Planned tasks: <one line per worker>
Allowed commands: <tests/builds only, no deploy/secrets/network unless named>
Must ask before: package-manager lifecycle scripts, workflow/deploy edits, MCP/tool config, secret-adjacent files
Must not touch: .env, credentials, signing keys, payment/KYC/tax files, production deploy controls
Rollback: <branch/worktree reset command or PR revert plan>
Preflight decision: Green / Yellow / Red
```

## Buy / skip trigger

- **Green:** keep the free receipt and run the fleet with normal code review.
- **Yellow:** buy the [$7 AI Agent Safety Starter Pack](https://payhip.com/b/1nmxV) if package scripts, agent instructions, workflow files, MCP/tool config, or secret-adjacent paths are present and the team wants reusable handoff/review templates before multiple agents start.
- **Red:** pause the fleet, remove or isolate the risky paths, then use the paid pack's command-hook and review-comment templates before any agent gets write or shell scope.

This page is intentionally narrow: it makes the product feel real for a Claude Squad user at the exact moment multiple terminal agents are about to touch a repo.
