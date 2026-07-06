# Preflight before Replit Agent workspaces

Use this 60-second receipt before a Replit Agent or similar hosted workspace agent edits a real repo, runs package scripts, reads `.env` values, or changes deployment/run commands.

## Why this buyer should care

A Replit workspace feels contained, but the agent can still inherit project run commands, package-manager scripts, secrets-adjacent files, database URLs, deploy settings, and repo instructions. That is exactly the moment where a small preflight receipt is easier than recovering from a bad agent run.

## Free preflight command

```bash
python3 agent_preflight_lite.py /path/to/replit-workspace
python3 agent_preflight_lite.py /path/to/replit-workspace --json
```

The lite scanner now flags `.replit` and `replit.nix` as agent/workflow config, alongside package scripts, workflow files, and secret-adjacent files.

## Pasteable run ticket

```markdown
Agent preflight receipt: Replit workspace
- Workspace/repo: <name>
- Agent about to run: Replit Agent or hosted IDE agent
- Decision: Green / Yellow / Red
- Config reviewed before agent access: `.replit`, `replit.nix`, package scripts, workflow files, agent instructions
- Secrets excluded or confirmed absent: `.env`, database URLs, deploy tokens, API keys
- Commands the agent may run without asking: <tests, lint, read-only checks>
- Commands requiring approval: deploy, database migration, destructive shell, force push, credential changes
```

## Buy or skip

Skip the paid bundle if the free scan is Green and the agent only performs a one-off edit. Buy the $7 workflow pack when the scan is Yellow/Red, the workspace contains `.replit` or `replit.nix` plus package scripts or secrets, or the agent will touch deploy/run commands repeatedly.

Tracking phrase for this proof: `agent-preflight-replit`.
