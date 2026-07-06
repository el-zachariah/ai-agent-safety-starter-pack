# Preflight before Kilo Code agentic engineering runs

Customer segment: teams using [Kilo Code](https://github.com/Kilo-Org/kilocode) or similar VS Code agentic-engineering extensions before granting workspace context, terminal commands, browser/API tools, MCP servers, package scripts, or secret-adjacent files.

Public evidence checked in this pulse: `Kilo-Org/kilocode` is live at <https://github.com/Kilo-Org/kilocode>, was observed with 25,628 GitHub stars, updated `2026-07-06T06:39:10Z`, and describes itself as "the all-in-one agentic engineering platform".

`KILO_CODE_AGENTIC_ENGINEERING_PROOF`

## Why this segment should care

Kilo Code-style editor agents sit close to the same risk surface that makes the paid starter pack useful:

- repo instructions and editor rules that steer autonomous edits,
- `.kilocode/`, `.vscode/`, MCP, or extension settings that can widen tool context,
- package scripts and CI workflows the agent may ask to run,
- `.env` / token-bearing files that should be excluded before task context expands,
- terminal commands that need a run / ask / avoid decision before approval.

The free lite scanner now treats `.kilocode/` as agent/workflow config, so a Kilo Code user can verify relevance locally before deciding whether the paid `$7` bundle saves setup time.

## 60-second Kilo Code preflight receipt

Run this before a Kilo Code task gets terminal or repo-write access:

```bash
python3 agent_preflight_lite.py /path/to/repo --json
```

Paste the result into the Kilo Code task as a short run ticket:

```text
Kilo Code run-ticket receipt
Repo: <repo/path>
Decision: <GREEN | YELLOW | RED>
Risk buckets: <agent/workflow config, package scripts, secret-adjacent files, risky shell commands>
Allowed now: read files, propose patches, run listed safe tests
Must ask first: install scripts, deploys, migrations, destructive shell, secret-bearing files, new MCP/tool servers
Must not touch: .env*, credentials, production config, force-pushes, broad delete commands
```

## YELLOW_RED_BUY_TRIGGER_KILO_CODE

Buy the `$7` starter pack at <https://payhip.com/b/1nmxV> only when the free scan is Yellow/Red and the Kilo Code task will touch a real repo. The paid pack saves the work of rebuilding:

1. a reusable pre-agent report template,
2. a destructive-command hook/guardrail starter,
3. a demo risky repo and verifier,
4. the buyer quickstart for repeating the same handoff across future Kilo Code / Cline / Roo / Cursor-style runs.

If the scan is Green, keep using the free lite scanner and normal review discipline.
