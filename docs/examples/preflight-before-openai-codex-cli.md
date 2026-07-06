# OpenAI Codex CLI preflight proof

Buyer segment: teams using [`openai/codex`](https://github.com/openai/codex) or a similar terminal/editor AI coding agent before it gets repository write access, shell commands, package scripts, CI workflows, MCP/tool config, or secret-adjacent files.

Target evidence captured 2026-07-06T03:35:50.168536-05:00: `openai/codex` is public, not archived, observed stars `95769`, updated `2026-07-06T08:34:59Z`, description: "Lightweight coding agent that runs in your terminal".

## Why this matters for OpenAI Codex CLI runs

OpenAI Codex CLI is valuable because it can operate directly against real source trees. That same convenience makes the first run trust-sensitive: package scripts, workflow files, local agent rules, MCP/tool configuration, and `.env`-adjacent paths should be reviewed before an agent edits files or executes commands.

Use the free preflight before the first OpenAI Codex CLI task, before widening from read/planning to edit/apply mode, and before enabling package/test/deploy commands.

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > openai-codex-cli-preflight-receipt.md
```

## Green / Yellow / Red decision gate

- **Green:** share the free receipt with the team and skip the paid pack for now.
- **Yellow:** review the flagged package scripts, workflow files, agent rules, MCP/tool config, or secret-adjacent paths before giving OpenAI Codex CLI broader scope.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need the full hook bundle, reviewer checklist, and repeatable receipts before letting the agent edit or execute in the repo.

## Copy-paste maintainer receipt

```md
OpenAI Codex CLI preflight receipt
- Repo scanned before agent execution: <repo/path>
- Agent/task: OpenAI Codex CLI coding task
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <files only / tests only / package scripts / no deploy / no secrets>
- Next gate: rerun preflight before applying changes or enabling shell/package commands.
```

## What the paid bundle adds for Yellow/Red scans

The public scanner proves the use case without requiring a purchase. The $7 pack is for teams that hit Yellow/Red and want ready-to-drop reviewer prompts, preflight command hooks, and handoff receipts so every OpenAI Codex CLI run starts with the same safety gate.
