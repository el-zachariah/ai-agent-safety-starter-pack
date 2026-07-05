# Continuous Claude-style loop preflight example

Customer segment: maintainers and solo builders running persistent Claude Code / MCP / hook loops like `parcadei/Continuous-Claude-v3` or similar continuous-agent harnesses.

This is not an endorsement by that project. It is a concrete proof for the buyer question: "Will this help before I leave a long-running coding agent attached to a real repo?"

## When to run this

Run the free lite preflight before the continuous agent gets repo context, shell access, MCP tools, or a task queue:

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git /tmp/agent-preflight
python3 /tmp/agent-preflight/agent_preflight_lite.py . --json
python3 /tmp/agent-preflight/agent_preflight_lite.py .
```

## Five-minute receipt to keep with the run

Copy this into the issue, PR, or local run log before the loop starts:

```markdown
Continuous-agent preflight receipt
- Repo checked: <repo/path>
- Agent loop: Continuous Claude-style loop / MCP / hooks
- Decision: Green / Yellow / Red
- Risk buckets found: <agent instructions, MCP/Cursor/Claude config, package scripts, workflows, secret-adjacent files, risky shell>
- Agent may run: <install/test/read-only commands>
- Agent must ask first: <deploy, credential, destructive, network, write-to-prod, long-running background process>
- Files to exclude or review before tool access: <paths>
- Next check: rerun before enabling new MCP tools or persistent memory
```

## Example Yellow result for a continuous loop

A continuous-agent repo usually becomes Yellow quickly because it often combines:

- `CLAUDE.md`, `AGENTS.md`, or hook instructions that steer agent behavior;
- MCP or Claude config that can expose local tools;
- package scripts the agent may run repeatedly;
- queue/watch processes that keep acting after the first prompt.

In that case, do not treat the scan as a security audit. Treat it as a handoff boundary: what may run automatically, what must ask first, and what should be excluded before the loop becomes persistent.

## Buy / skip trigger

Use the free scanner if the decision is Green and you only need a one-off note.

Buy the $7 pack when this is Yellow or Red and you need the reusable workflow bundle: report template, destructive-command hook, buyer quickstart, demo risky repo, and verifier so every continuous-agent run starts with the same guardrail receipt instead of a custom checklist.
