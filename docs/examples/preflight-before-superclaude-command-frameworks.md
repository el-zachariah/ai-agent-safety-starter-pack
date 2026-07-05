# SuperClaude command framework preflight proof

Named buyer segment: teams installing or maintaining [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)-style Claude Code command packs, personas, MCP links, and project-level instructions before letting an AI coding assistant work inside a real repository.

Public target evidence captured in this pulse:

- Repository: `SuperClaude-Org/SuperClaude_Framework`
- Stars observed: `23490`
- Last updated: `2026-07-05T20:52:09Z`
- Public description: A configuration framework that enhances Claude Code with specialized commands, cognitive personas, and development methodologies.

## Why this buyer should care before checkout

SuperClaude-style installs can make Claude Code feel production-ready fast: commands, cognitive personas, orchestration patterns, MCP/tooling, and repeatable workflows. The missing step is a small preflight receipt before those instructions inherit a real repository with package scripts, `.env` files, CI secrets, or write-capable agent loops.

Use the free scanner first:

```bash
python3 tools/agent_repo_lite_scan.py . --markdown
```

Then read the result as a buy/skip decision:

- **Green:** keep using the free scanner and do not buy yet.
- **Yellow:** buy the $7 pack if the repo has SuperClaude commands/personas plus package scripts, MCP config, devcontainer lifecycle hooks, Cursor/Copilot rules, or CI automation that an agent can trigger.
- **Red:** buy before granting the assistant broad scope; generate a repo-specific handoff receipt and paste it into the task/PR so maintainers know what was checked.

## Preflight receipt template for SuperClaude-style setups

Copy this into the issue, PR, or internal task before a SuperClaude-enhanced agent edits code:

```markdown
### Agent preflight receipt — SuperClaude command framework

- Repo checked: <owner/repo or local path>
- Assistant/framework: Claude Code with SuperClaude-style commands/personas
- Agent scope requested: <read-only / edit / shell / tests / browser / MCP / deploy>
- Scan command run: `python3 tools/agent_repo_lite_scan.py . --markdown`
- Decision level: <Green / Yellow / Red>
- Why it is not Green: <package scripts, env files, MCP config, devcontainer lifecycle commands, repo rules, CI secrets, etc.>
- Guardrail before run: <branch, no-secrets, limited commands, reviewer, backup, dry-run>
- Handoff owner: <person reviewing the agent's output>
```

## What the paid pack adds

The paid bundle is not another generic checklist. It adds a repeatable preflight/handoff workflow for the moment a Claude Code framework stops being a toy install and starts touching a real repo:

1. a structured repo-risk worksheet,
2. a stronger command-hook workflow,
3. copy/paste maintainer receipts,
4. buyer-facing Yellow/Red triage language,
5. examples for MCP, hooks, commands, marketplaces, coding agents, and multi-agent harnesses.

Product: <https://payhip.com/b/1nmxV>
