# Preflight before Dev Containers / Codespaces agent runs

Named segment: teams using Dev Containers or GitHub Codespaces workspaces before letting Claude Code, Codex, Cursor, Copilot coding agent, or another AI coding agent run inside the container.

Public target evidence checked during this deadline pulse: [`devcontainers/spec`](https://github.com/devcontainers/spec) is live, describes Development Containers as full-featured development environments, and was observed with 5,566 stars / updated `2026-07-05T06:03:53Z` via the GitHub API.

## Why this buyer should care

A devcontainer can quietly change what the agent inherits before the first edit:

- `.devcontainer/devcontainer.json` can run `postCreateCommand`, `postStartCommand`, install scripts, forwarded ports, features, mounts, and environment wiring.
- Codespaces or containerized agents often receive repo write access plus package-manager commands immediately.
- A team may assume the container is safe while still exposing `.env` examples, package scripts, workflow files, MCP config, or broad Docker/socket mounts.

## 60-second preflight receipt

Paste this before the first agent run:

```text
Agent preflight: Dev Container / Codespaces workspace
Repo: <repo URL or path>
Scan command: python3 agent_preflight_lite.py . --json
Decision: Green / Yellow / Red
Devcontainer config reviewed: .devcontainer/devcontainer.json <present/absent>
Container lifecycle commands: <postCreate/postStart/updateContent commands or none>
Agent may run: <install/test commands allowed>
Agent must ask before: <postCreateCommand changes, Docker/socket mounts, port exposure, deploy/migration scripts, credential reads>
Agent must not touch: <.env, auth files, production config, package publish/deploy paths>
```

## Buy/skip trigger

- **Skip the paid pack for now** if the free scan is Green and the devcontainer has no lifecycle commands, broad mounts, token wiring, or deploy scripts.
- **Buy the $7 pack** at <https://payhip.com/b/1nmxV> if the scan is Yellow/Red, `.devcontainer/devcontainer.json` contains lifecycle commands, or the agent will run inside Codespaces with repo write access and package scripts. The paid bundle gives the reusable report template, destructive-command hook, demo risky repo, and verifier instead of rebuilding the handoff during the task.

## First safe commands

```bash
python3 agent_preflight_lite.py . --json
python3 agent_preflight_lite.py . > agent-preflight-devcontainer.md
```

Keep `agent-preflight-devcontainer.md` beside the task ticket before the agent gets shell access.
