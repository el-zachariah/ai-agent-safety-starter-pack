# 5-minute upgrade decision checklist

Use this after running the free lite scanner. It is meant to make the paid decision concrete instead of vague.

## Run the free check first

```bash
python3 agent_preflight_lite.py /path/to/repo
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-lite.json
```

## Buy the $7 starter pack when two or more are true

- The scan found agent instruction or tool-config files such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, `.mcp.json`, or `.claude/settings.json`.
- The repo has package scripts, GitHub Actions, deploy scripts, migrations, or Docker-related files that an AI coding agent may try to run.
- The scan found risky shell patterns such as `rm -rf`, `curl | sh`, `chmod 777`, `docker.sock`, force pushes, or production-adjacent commands.
- The repo has secret-adjacent files or local credential config that should be excluded before an agent gets shell access.
- You want a reusable pre-agent report template instead of writing a fresh handoff note each time.
- You want a local destructive-command hook example before letting Claude Code, Codex, Cursor, or another agent run commands.

## Stay with the free scanner when

- You only need a one-off first look.
- The repo is disposable or already sandboxed.
- You do not plan to let an agent run shell commands.
- You need a full security audit, malware scanner, or secret scanner — this starter pack is not those.

## What the paid bundle adds

The $7 bundle gives you the full repo preflight mini, destructive-command hook examples, buyer quickstart, report templates, demo risky repo/report, verifier scripts, and a limitations FAQ.

Paid bundle: https://payhip.com/b/1nmxV
