# Preflight before HumanLayer-style agent approval workflows

Target segment: teams using [`humanlayer/humanlayer`](https://github.com/humanlayer/humanlayer) or similar human-in-the-loop approval layers for Claude Code, Codex, OpenCode, and other coding agents.

Public evidence captured for this proof:

- Repository: `humanlayer/humanlayer`
- Description: The best way to get AI coding agents to solve hard problems in complex codebases.
- Stars observed: 11,089
- Last updated: `2026-07-05T18:16:26Z`
- Topics observed: `agents, ai, human-in-the-loop, llm, llms, humanlayer, amp, claude-code, codex, opencode`
- Archived: `False`

Why this buyer segment is high-fit: HumanLayer-style approval tooling sits exactly where an agent asks to run commands, edit files, call APIs, or escalate a task. If the repo already has agent instructions, package scripts, MCP/tool config, workflow secrets, or secret-adjacent files, the approval gate needs a short repo-risk receipt before the human approves the next action.

## 60-second pre-approval receipt

Run this before approving the first coding-agent action in a real repository:

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-humanlayer.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-humanlayer.md
```

Paste this into the HumanLayer approval thread, PR, or run ticket:

```text
Agent preflight receipt: agent-preflight-humanlayer.md
Decision: Green / Yellow / Red
Risk buckets seen: <agent instructions / MCP or tool config / package scripts / workflows / secret-adjacent files / risky shell>
Approve now: <exact command or file edit approved>
Must ask first: package install, deploy, destructive shell, credential-adjacent reads, workflow edits, external API writes
Do not touch: .env, tokens, production deploy keys, payment/admin browser profiles, unrelated repo areas
Upgrade trigger: if this receipt is Yellow/Red, use the $7 starter pack for the reusable handoff template, destructive-command hook, verifier, and demo report before approving broader scope.
```

## What the free scan catches before approval

- `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, `.claude-plugin/`, and other agent instruction files that shape what the agent will do.
- MCP / Claude / Cursor / GitHub Copilot / Dev Container config that can expand tool access.
- Package scripts, workflow files, or install commands a coding agent may run after approval.
- Secret-adjacent filenames that should be excluded or explicitly protected before the agent gets broader context.
- Risky shell patterns such as `rm -rf`, `curl | sh`, `chmod 777`, Docker socket access, or force-push instructions.

## When to buy the $7 pack

Buy the full bundle at <https://payhip.com/b/1nmxV> if the HumanLayer approval path is not a one-off toy approval:

- Yellow/Red scan result before the first broad action.
- Multiple approval steps in the same repo where rebuilding the receipt by hand wastes time.
- Agent will run package scripts, workflow edits, deploy previews, MCP/API calls, or shell commands.
- You need the reusable report template, destructive-command hook, local verifier, and demo risky repo before letting the agent continue.

Skip the paid pack for now if the scan is Green and the approved action is narrow, reversible, and already reviewed.

Buyer proof marker: `agent-preflight-humanlayer`.
