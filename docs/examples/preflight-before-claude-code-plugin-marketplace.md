# Preflight before installing a Claude Code plugin marketplace

Named buyer segment: Claude Code users, maintainers, and small teams installing or curating plugin marketplaces such as Superpowers Marketplace, Tons of Skills, and Build with Claude.

## Why this proof exists

A marketplace install can add commands, hooks, skills, agent files, or MCP/tool configuration to a real developer environment. A first buyer needs to know the seller understands that moment: the risk is not theoretical, it happens right before someone pastes `/plugin marketplace add ...` or `/plugin install ...` and lets an AI coding agent operate inside a repo.

The free lite scanner gives that buyer a public, inspectable first step before they buy the paid handoff templates.

## Five-minute proof path

1. Clone the plugin or marketplace source you are considering.
2. From this repo, run the free preflight against that checkout:

   ```bash
   python3 agent_preflight_lite.py /path/to/plugin-or-marketplace --json > agent-preflight-receipt.json
   ```

3. Review the receipt for:
   - package scripts that run shell, install hooks, or network actions;
   - MCP/tool configuration that expands what the agent can call;
   - `.env`, token, or credential-looking patterns;
   - generated-code or vendored directories that should not be trusted as authored logic;
   - command files that ask Claude Code to run destructive shell actions.
4. Attach the receipt to the PR/review thread or keep it in the repo before allowing an AI-agent session to continue.

## Yellow checkout trigger

Buy the $7 starter pack when the free scan finds any ambiguity and you need a repeatable buyer/team handoff:

- you are reviewing a plugin-marketplace PR for a real team;
- a command/hook/plugin touches package scripts, shell, MCP, secrets, or release automation;
- you need a short approval checklist instead of an ad-hoc comment;
- you want the destructive-command guardrail prompt and report template before the next Claude Code/Codex session.

Paid bundle: https://payhip.com/b/1nmxV

## Red stop trigger

Do not proceed to install or buy anything yet if the receipt shows hardcoded credentials, obfuscated shell, unexplained install scripts, private endpoint assumptions, or a maintainer cannot explain why a hook/command needs the requested power.

## Public distribution evidence

These live routes show the same free preflight being offered where Claude Code plugin buyers already look:

- Superpowers Marketplace PR: https://github.com/obra/superpowers-marketplace/pull/64
- Tons of Skills marketplace PR: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/pull/964
- Build with Claude command PR: https://github.com/davepoon/buildwithclaude/pull/218

Use this page to decide quickly: if you are about to install or review a marketplace plugin, run the free receipt first; if the receipt needs to become a team-safe handoff, buy the starter pack.
