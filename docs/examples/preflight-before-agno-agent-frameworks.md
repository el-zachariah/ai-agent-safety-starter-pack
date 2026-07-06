# Preflight before Agno agent-framework runs

Marker: `AGNO_AGENT_FRAMEWORK_PROOF`

Target evidence checked 2026-07-06T01:56:03-05:00: [`agno-agi/agno`](https://github.com/agno-agi/agno) is public/non-archived, observed stars `41010`, updated `2026-07-06T06:37:38Z`. Description: Build, run, and manage agent platforms.

## Who this is for

Teams using Agno-style agent frameworks before a local or CI-backed agent receives repo files, tool calls, MCP/API connectors, package scripts, vector/database config, or secret-adjacent environment values.

## 60-second free preflight

Run the public lite scanner before the first agent run:

```bash
python3 agent_preflight_lite.py /path/to/agno-project --json
```

Paste this run-ticket into the task handoff:

```text
Agno run-ticket receipt
- Repo/workspace checked:
- Agent/task being delegated:
- Scan level: GREEN / YELLOW / RED
- Agent/workflow files reviewed:
- Package/install/test/deploy commands allowed:
- MCP/API/tool connectors allowed:
- Secret-adjacent files excluded:
- Human approval required before:
```

## Buy / skip trigger

`YELLOW_RED_BUY_TRIGGER_AGNO`: buy the $7 starter pack only when the free scan is Yellow/Red and an Agno-style agent will run commands, call tools, read config, or touch real repo files. The paid bundle adds the reusable report template, destructive-command hook examples, demo risky repo, and verification scripts so this receipt becomes repeatable instead of improvised.

Payhip bundle: https://payhip.com/b/1nmxV

If the scan is Green and the task is read-only, keep using the free lite scanner and normal code review discipline.
