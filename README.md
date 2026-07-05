# AI Agent Safety Starter Pack — free lite preflight

A small public preview from **Signal Loom Works** for developers who let AI coding agents work inside local repos.

AI agents are useful, but a surprising number of repos contain agent instructions, MCP/Cursor/Claude settings, shell scripts, package hooks, workflow files, and secret-adjacent files that are worth checking **before** a coding agent gets tool access.

This repository includes a free lite scanner/checklist. The paid `$7` starter pack adds the full repo preflight mini, a destructive-command hook, buyer quickstart, demo risky repo, report templates, and verification scripts.

**Buy the full bundle:** https://payhip.com/b/1nmxV

**30-second buy/skip rule:** run the free scan first. Buy the `$7` pack only when the result is Yellow/Red: two or more risk buckets, MCP/Cursor/Claude config, package scripts, secret-adjacent files, or shell commands the agent might run. If the result is Green, keep using the free lite scanner and normal review discipline.

## What the free lite scanner catches

`agent_preflight_lite.py` looks for common AI-agent workspace risk signals:

- agent instruction files such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`
- MCP / Claude / Cursor config files
- secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, `id_rsa`
- risky shell patterns such as `rm -rf`, `curl | sh`, `chmod 777`, `docker.sock`, and `force push`
- package scripts and GitHub Actions workflow files that an agent may touch

It is intentionally lightweight. It is **not** a sandbox, malware scanner, secret scanner, or security audit.

## Quick start

```bash
python3 agent_preflight_lite.py /path/to/repo
python3 agent_preflight_lite.py /path/to/repo --json
```

Want a no-risk demo first?

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py examples/sample-risky-repo
```

Example output is in [`examples/sample-report.md`](examples/sample-report.md). It now prints the same **Green / Yellow / Red** decision used by the buy/skip rule, so you can see when the `$7` workflow bundle saves setup time instead of guessing.

One-minute scorecard: [`docs/one-minute-risk-scorecard.md`](docs/one-minute-risk-scorecard.md) turns scan findings into a Green / Yellow / Red go/no-go decision before an agent gets shell access.

Red-flag matrix: [`docs/red-flag-to-action-matrix.md`](docs/red-flag-to-action-matrix.md) maps scan findings to run / ask / avoid decisions before an agent gets shell access.

Claude Code slash-command bridge: copy [`commands/agent-preflight.md`](commands/agent-preflight.md) into `.claude/commands/agent-preflight.md`, then run `/agent-preflight .` before a tool-enabled session. Setup notes: [`docs/claude-code-slash-command.md`](docs/claude-code-slash-command.md).

Free handoff guide: [`docs/agent-handoff-playbook.md`](docs/agent-handoff-playbook.md) shows a 10-minute flow for turning the scan into Claude Code/Codex/Cursor run rules before an agent gets tool access.

Copy-paste task prompt: [`docs/copy-paste-agent-task-prompt.md`](docs/copy-paste-agent-task-prompt.md) gives a short agent instruction block to paste after the scan and before shell access.

Upgrade decision guide: [`docs/upgrade-decision-checklist.md`](docs/upgrade-decision-checklist.md) turns the scan result into a concrete buy/skip checklist for the `$7` bundle.

## Why this exists

Before I let an autonomous coding agent work in a repo, I want a cheap first pass that answers:

1. What instruction/config files will shape the agent's behavior?
2. Are there obvious destructive commands or risky install/deploy scripts?
3. Are there secret-adjacent files that should be excluded or protected?
4. Which files deserve a human look before agent execution?

The full starter pack turns this into a reusable preflight workflow plus a command hook that blocks obvious destructive shell commands.

Use the free scanner before you clone-and-run an unfamiliar repo, hand a backlog task to Claude Code/Codex/Cursor, enable a new MCP config, or let an agent run install/test/deploy commands.

## Upgrade trigger

Run the free lite check first. The `$7` bundle is meant for the moment the scan finds enough signals that you want a repeatable handoff instead of a one-off note:

1. capture the repo preflight result,
2. decide what the agent may read or run,
3. block obvious destructive commands with a local hook, and
4. keep a reusable report template with the repo before assigning Claude Code, Codex, Cursor, or another AI coding agent.

## Full bundle

The `$7` Payhip bundle includes:

- Agent Repo Preflight Mini
- AI Coding Safety Hook Kit
- destructive-command hook examples
- buyer quickstart
- report templates
- demo risky repo and generated demo report
- verification scripts
- support/limitations FAQ

Payhip: https://payhip.com/b/1nmxV

## License

The free lite files in this public repository are MIT licensed. The paid bundle is sold separately on Payhip.
