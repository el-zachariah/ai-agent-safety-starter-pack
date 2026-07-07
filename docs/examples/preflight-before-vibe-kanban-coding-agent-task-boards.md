# Preflight before Vibe Kanban coding-agent task-board teams let agents touch a real workspace

Marker: `VIBE_KANBAN_CODING_AGENT_TASK_BOARD_PROOF`

Verified public target: [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) — 27293 GitHub stars, updated 2026-07-07T03:48:21Z. Get 10X more out of Claude Code, Codex or any coding agent

This proof is for teams adopting Vibe Kanban coding-agent task-board teams who are close enough to real agent work to need a cheap, concrete preflight receipt before an autonomous workflow touches repository files, commands, local services, or credentials.

## Why this segment should care

The risk is not the public project itself. The risk is widening from a demo into task-board prompts, parallel coding-agent runs, repo checkouts, run logs, package scripts, MCP/API tools, and secret-adjacent workspace config before a maintainer has written down what the agent may do. A preflight receipt creates a small, inspectable approval artifact before the first unsafe command, tool call, browser action, or repo write lands.

## 4-minute preflight shape

1. Snapshot the exact branch, dirty files, intended agent/task-board command, and allowed tool scope.
2. Block obvious private material: `.env`, tokens, SSH keys, browser profiles, production database URLs, customer exports, and payment/admin surfaces.
3. Classify the run as Green / Yellow / Red before the agent or workflow receives write, shell, browser, MCP/API, or deploy scope.
4. Save the receipt next to the PR, issue, task-board card, or handoff note so a reviewer can approve the next step without reconstructing the whole agent session.

## Copy-paste receipt for Vibe Kanban coding-agent task-board teams

```text
VIBE_KANBAN_CODING_AGENT_TASK_BOARD_PROOF
Framework/channel: BloopAI/vibe-kanban
Agent lane: <task-board / parallel-agent / repo-writing / command-runner>
Target branch/workspace: <branch-or-path>
Planned agent command/task: <exact command or task-card link>
Files and tools the agent may touch: <paths, MCP/API tools, browser/local-app surfaces>
Secrets/payment/admin scan: <pass/fail + redacted reason>
Decision: Green / Yellow / Red
Reviewer/owner: <handle>
```

## Buy / skip trigger

- Green: keep using the free scanner and this receipt template.
- Yellow: buy the paid bundle when Vibe Kanban coding-agent task-board teams work moves from a toy/demo run into real repo writes, package scripts, MCP/API tools, browser/local-app access, CI/deploy config, or customer data handling.
- Red: do not buy yet; stop until the task no longer touches secrets, payment/KYC/admin surfaces, production data, or legal identity.

Paid upgrade: <https://payhip.com/b/1nmxV>
Free repo: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>
