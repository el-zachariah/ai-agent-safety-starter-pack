# Preflight before runtime safety enforcement hooks

Customer segment: teams evaluating runtime safety layers for AI coding agents, including GenseeAI/gensee-crate-style Claude Code/Codex hook users.

This is not a formal integration or endorsement. It is a practical preflight receipt to run **before** enabling a runtime enforcement wrapper, hook daemon, or agent safety monitor in a real repo.

## Why this buyer should care

Runtime monitors help after an agent starts working. The repo still needs a quick pre-tool-access pass so the team knows what the monitor is about to inherit:

- agent instructions such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or `.cursor/rules/*`;
- MCP / Claude / Cursor config that can expose tool surfaces;
- package scripts and workflows the agent or hook may trigger;
- secret-adjacent files that should stay out of the agent run;
- shell patterns worth blocking before the wrapper ever sees them.

## Five-minute receipt

```bash
# 1. Run the free preflight from this repo.
python3 agent_preflight_lite.py /path/to/repo --json > preflight-before-runtime-safety.json
python3 agent_preflight_lite.py /path/to/repo > preflight-before-runtime-safety.md

# 2. Keep the receipt with the first protected run.
mkdir -p docs/agent-run-receipts
cp preflight-before-runtime-safety.md docs/agent-run-receipts/runtime-safety-preflight.md
```

## What to decide before enabling the runtime layer

| Finding | Decision before agent run |
| --- | --- |
| Agent instruction files | Review and summarize which instructions should bind the agent. |
| MCP / Claude / Cursor config | Confirm which tools are allowed and which need human approval. |
| Package scripts / workflows | Run only the minimal install/test commands needed for the task. |
| Secret-adjacent files | Exclude, move, or mark as must-not-read before the agent starts. |
| Risky shell patterns | Add explicit deny/ask rules to the runtime wrapper and task prompt. |

## Buy / skip trigger

- **Skip the paid bundle for now** if the scan is Green and the runtime tool already gives you a clean receipt, prompt, and destructive-command deny list.
- **Buy the `$7` bundle** when the scan is Yellow/Red and you need a reusable handoff template, destructive-command hook, report format, demo risky repo, and verifier instead of creating those artifacts during the protected run.

Payhip: <https://payhip.com/b/1nmxV>

## Copy-paste handoff

> Before enabling the runtime safety wrapper, I ran the free AI Agent Safety Starter Pack preflight. The scan result is `<Green/Yellow/Red>`. The agent may run `<allowed commands>`. It must ask before `<must-ask actions>`. It must not touch `<must-not-touch files/commands>`. If this stays Yellow/Red across more repos, use the paid starter pack to standardize the receipt, hook, and verification flow.
