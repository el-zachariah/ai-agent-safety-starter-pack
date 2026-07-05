# Claude Code marketplace proof — AI Agent Safety Starter Pack

This page is for Claude Code plugin, slash-command, and agent-directory curators who need to decide quickly whether this project is relevant to their users.

## Who this helps

- Claude Code users who run agents in real repos and want a pre-tool-access checklist.
- Plugin/skill marketplace maintainers looking for small, auditable utility commands instead of broad AI wrappers.
- Teams using MCP, Cursor rules, `AGENTS.md`, `CLAUDE.md`, package scripts, and GitHub Actions that may be touched by coding agents.

## What the free repo proves

The free `agent_preflight_lite.py` scanner checks a repo for agent-relevant risk signals before a coding agent gets tool access:

- agent instruction files: `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`
- Claude/MCP/Cursor config files
- secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, and SSH-key-looking paths
- risky shell patterns such as `rm -rf`, `curl | sh`, `chmod 777`, `docker.sock`, and force-push language
- package scripts and GitHub Actions workflows that an agent may execute or edit

## Verified sample output

The checked-in sample risky repo produces a concrete report here:

- Markdown report: [`examples/sample-report.md`](../examples/sample-report.md)
- JSON report: [`examples/sample-report.json`](../examples/sample-report.json)

Run it yourself:

```bash
python3 agent_preflight_lite.py examples/sample-risky-repo
python3 agent_preflight_lite.py examples/sample-risky-repo --json
```

## Why a curator should care

This is not positioned as a security audit or sandbox. It is a small first-pass utility that helps a Claude Code user pause before granting an agent tool access to a repo with risky scripts, hidden instructions, and secret-adjacent files.

That makes the free repo a clean directory/listing target: users can inspect the source, run the sample, and decide whether the paid $7 bundle is worth buying for the fuller checklist, destructive-command hook examples, buyer quickstart, templates, and verification scripts.

Paid bundle: <https://payhip.com/b/1nmxV>
