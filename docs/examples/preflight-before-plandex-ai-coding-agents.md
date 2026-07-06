# Plandex AI coding-agent preflight proof

Buyer segment: teams using [`plandex-ai/plandex`](https://github.com/plandex-ai/plandex) or a similar planning/editing AI coding agent before it gets repository write access, shell commands, package scripts, CI workflows, MCP/tool config, or secret-adjacent files.

Target evidence captured 2026-07-06T03:08:15.703026-05:00: `plandex-ai/plandex` is public, not archived, observed stars `15502`, updated `2026-07-06T07:29:58Z`, description: "Open source AI coding agent. Designed for large projects and real world tasks.".

## Why this matters for Plandex-style runs

Plandex-style agents are useful because they can plan changes across real projects. The same breadth makes the first run trust-sensitive: a repo may include package scripts, workflow files, local agent rules, MCP/tool configuration, and `.env`-adjacent paths that should be reviewed before the agent starts editing or executing commands.

Use the free preflight before the first Plandex task, before switching from planning to apply/edit mode, and before allowing package/test/deploy commands.

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > plandex-preflight-receipt.md
```

## Green / Yellow / Red decision gate

- **Green:** share the free receipt with the team and skip the paid pack for now.
- **Yellow:** review the flagged package scripts, workflow files, agent rules, MCP/tool config, or secret-adjacent paths before giving Plandex broader scope.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need the full hook bundle, reviewer checklist, and repeatable receipts before letting the agent edit or execute in the repo.

## Copy-paste maintainer receipt

```md
Plandex preflight receipt
- Repo scanned before agent execution: <repo/path>
- Agent/task: Plandex planning/apply run
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <files only / tests only / package scripts / no deploy / no secrets>
- Next gate: rerun preflight before applying changes or enabling shell/package commands.
```

## What the paid bundle adds for Yellow/Red scans

The public scanner proves the use case without requiring a purchase. The $7 pack is for teams that hit Yellow/Red and want ready-to-drop reviewer prompts, preflight command hooks, and handoff receipts so every Plandex-style run starts with the same safety gate.
