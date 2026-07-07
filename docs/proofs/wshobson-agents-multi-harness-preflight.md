# Buyer proof: multi-harness agent marketplace users

Named public segment: teams evaluating agents from multi-harness catalogs such as `wshobson/agents`.

Route status note: the related `wshobson/agents` marketplace PR is parked as non-fit after maintainer review. This page remains a generic multi-harness workflow example, not active distribution proof.

This is not an endorsement by that repository. It is a practical proof for buyers who already install or test reusable Claude Code, Codex, Cursor, OpenCode, Gemini, or Copilot agent workflows and want a fast preflight before letting an agent touch a real repo.

## Why this segment should care before checkout

A multi-agent catalog makes agent adoption easy, but the real risk is local workspace context:

- repo-level instructions such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, and `.cursor/rules/*`
- MCP, Claude, Cursor, Copilot, Dev Container, and package-manager config that changes what an agent can see or run
- package scripts, CI workflows, and shell snippets an agent may edit or execute
- secret-adjacent files that should be reviewed before tool access

The free scanner in this repo is enough for a first pass. The paid bundle is only worth buying when that first pass produces a Yellow or Red result.

## 3-minute preflight example

```bash
python3 agent_preflight_lite.py /path/to/repo
```

Interpret the result for a team testing third-party agents:

- Green: keep the free scanner result as the pre-agent receipt; do not buy yet.
- Yellow: buy the $7 bundle if two or more buckets are present, or if MCP, Cursor, Claude, Copilot, Dev Container, package scripts, or shell commands appear.
- Red: buy the $7 bundle before giving the agent write/tool access; use the paid templates and destructive-command hook as the review receipt.

## Why the paid bundle is relevant here

The paid pack adds the parts a multi-agent user needs after the free scan finds risk:

1. a fuller repo preflight mini for agent-specific files and command surfaces,
2. a destructive-command hook to catch dangerous shell patterns before execution,
3. buyer quickstart notes for turning the scan into a PR/issue review receipt,
4. report templates a maintainer can paste into the repo before the agent starts work,
5. a demo risky repo and verifier scripts so the buyer can inspect the pack before relying on it.

Buy only if your workspace is Yellow or Red: <https://payhip.com/b/1nmxV>

Support and trust details: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/trust-and-support.md>
