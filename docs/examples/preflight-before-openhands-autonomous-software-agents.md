# Preflight before OpenHands autonomous software-agent runs

Named customer segment: teams evaluating or running [`OpenHands/OpenHands`](https://github.com/OpenHands/OpenHands) for autonomous software-engineering work.

Public target evidence checked during this deadline pulse:

- Repository: `OpenHands/OpenHands`
- URL: https://github.com/OpenHands/OpenHands
- Stars observed: `79591`
- Last updated: `2026-07-06T11:03:57Z`
- Description: 🙌 OpenHands: AI-Driven Development

## Why this matters before a first run

OpenHands is a high-fit autonomous software-engineering agent surface: it can inspect repos, propose edits, run commands, and touch CI/package paths, so a fast preflight receipt answers the trust question before a first agent run.

Use the free lite scanner first when an OpenHands run is about to include repository context, generated file edits, shell commands, package scripts, workflow files, MCP/tool connectors, or secret-adjacent config.

## Copy-paste preflight receipt

```text
OpenHands preflight receipt
Repo:
Branch/PR:
Agent scope:
Commands/tools allowed:
Sensitive paths excluded:
Lite scanner result: Green / Yellow / Red
Decision: proceed / narrow scope / buy the full $7 checklist bundle before running
Owner:
Timestamp:
```

## Files/config to inspect before allowing agent work

- `.openhands/`
- `openhands.yaml`
- `openhands.toml`
- `.github/workflows/*`
- package scripts such as `package.json`, `pyproject.toml`, `uv.lock`, `requirements*.txt`, `Makefile`
- secret-adjacent files such as `.env*`, credential configs, deployment manifests, and cloud/API connector settings

## Buy / skip trigger

- **Green:** keep using the free scanner and this receipt.
- **Yellow/Red:** buy the $7 pack if the run will edit files, execute package scripts, touch CI/tool config, or expose secret-adjacent paths.
- **Red:** stop the run and use the paid checklist before handing repository context or command execution to OpenHands.

Paid bundle: https://payhip.com/b/1nmxV
