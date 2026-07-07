# Graphiti agent-memory workflow preflight proof

Unique marker: `GRAPHITI_AGENT_MEMORY_WORKFLOW_PROOF`

Buyer segment: Graphiti agent-memory teams using [`getzep/graphiti`](https://github.com/getzep/graphiti) or a similar agent framework before memory graph writes, tool calls, repo writes, shell commands, workflow files, database config, and secret-adjacent paths enter scope.

Target evidence captured 2026-07-07T03:40:06.661882-05:00: `getzep/graphiti` is public, not archived, observed stars `28446`, updated `2026-07-07T08:31:59Z`, description: "Build Real-Time Knowledge Graphs for AI Agents".

## Why this matters before the first Graphiti-backed agent-memory run

Graphiti agent-memory teams can move faster than a manual reviewer because the agent stack can chain planning, tool use, and code changes. The trust break happens at checkout when a buyer cannot see how the safety pack fits their actual workflow. This proof makes the use case concrete: run the free preflight before the agent stack gets edit or execution authority, then only buy when the scan turns Yellow or Red.

## One-command public preflight

```bash
python3 scripts/agent_preflight_lite.py /path/to/repo --markdown > graphiti-agent-memory-workflows-preflight-receipt.md
```

## Green / Yellow / Red buy trigger

- **Green:** attach the free receipt to the agent task and skip the paid pack for now.
- **Yellow:** review the flagged package scripts, workflow files, agent/tool permission surfaces, MCP/tool config, and secret-adjacent paths before widening agent scope.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need the full hooks, reviewer prompts, and repeatable handoff receipts before allowing the agent workflow to edit or execute.

## Copy-paste maintainer receipt

```md
Graphiti agent-memory teams preflight receipt
- Target workflow: Graphiti-backed agent-memory run
- Repo scanned before agent authority: <repo/path>
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <files only / tests only / no package scripts / no deploy / no secrets>
- Next gate: rerun before applying changes or enabling shell/package/deploy commands.
```

## What the paid bundle adds for Yellow/Red scans

The public scanner proves fit without requiring a purchase. The $7 pack is for teams that hit Yellow/Red and want ready-to-drop command hooks, reviewer checklists, and handoff receipts so every Graphiti-backed agent-memory run starts with the same safety gate.
