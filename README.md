# AI Agent Safety Starter Pack — free lite preflight

A small public preview from **Signal Loom Works** for developers who let AI coding agents work inside local repos.

AI agents are useful, but a surprising number of repos contain agent instructions, MCP/Cursor/Claude settings, shell scripts, package hooks, workflow files, and secret-adjacent files that are worth checking **before** a coding agent gets tool access.

This repository includes a free lite scanner/checklist. The paid `$7` starter pack adds the full repo preflight mini, a destructive-command hook, buyer quickstart, demo risky repo, report templates, and verification scripts.

**Buy the full bundle:** https://payhip.com/b/1nmxV

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

Example output is in [`examples/sample-report.md`](examples/sample-report.md).

## Why this exists

Before I let an autonomous coding agent work in a repo, I want a cheap first pass that answers:

1. What instruction/config files will shape the agent's behavior?
2. Are there obvious destructive commands or risky install/deploy scripts?
3. Are there secret-adjacent files that should be excluded or protected?
4. Which files deserve a human look before agent execution?

The full starter pack turns this into a reusable preflight workflow plus a command hook that blocks obvious destructive shell commands.

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
