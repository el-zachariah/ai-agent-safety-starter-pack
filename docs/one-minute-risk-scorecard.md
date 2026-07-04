# One-minute repo risk scorecard

Use this after the free lite scan and before you give Claude Code, Codex, Cursor, or another tool-enabled agent shell access.

The goal is not to prove a repo is safe. The goal is to decide whether the next agent run should be **green-lighted, slowed down, or blocked until you make a handoff note**.

## Score the repo

Give the repo **1 point** for each bucket the scan flags.

| Bucket | What to count | Why it matters before an agent run |
|---|---|---|
| Agent instructions | `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*` | These files can change the agent's behavior and priorities. |
| Agent/tool config | MCP, Claude, Cursor, automation config | Tooling config can expose commands, servers, or unexpected workflows. |
| Package/workflow hooks | `package.json` scripts, GitHub Actions, Makefiles, CI/deploy scripts | Agents often run install/test/build commands that trigger these paths. |
| Secret-adjacent files | `.env`, `.npmrc`, `.pypirc`, `id_rsa`, token-ish filenames | These should usually be excluded from agent context and logs. |
| Network/deploy shell | `curl | sh`, `wget | bash`, deploy scripts, Docker socket usage | These can pull remote code or mutate infrastructure. |
| Destructive shell | `rm -rf`, force pushes, `chmod 777`, broad deletes | These deserve explicit allow/deny rules before shell access. |

## Decision in 60 seconds

| Score | Label | Decision before tool access |
|---:|---|---|
| 0–1 | **Green** | Run the agent, but keep normal review discipline. |
| 2–3 | **Yellow** | Add a short handoff note: what the agent may run, what it must ask about, and what files to avoid. |
| 4+ | **Red** | Stop. Write a real preflight report, set command guardrails, and do not let the agent improvise shell/deploy actions. |

## Buy trigger for the $7 starter pack

Buy the full bundle when the free scan lands in **Yellow or Red** and you are about to let an agent run commands in a real repo.

The paid pack is meant to save setup time by giving you:

- a reusable preflight workflow,
- report templates,
- a destructive-command hook,
- a demo risky repo/report,
- a buyer quickstart, and
- local verification scripts.

Payhip: https://payhip.com/b/1nmxV

## Copy-paste scorecard receipt

```text
Repo:
Date:
Agent/tool planned:

Flagged buckets:
[ ] Agent instructions
[ ] Agent/tool config
[ ] Package/workflow hooks
[ ] Secret-adjacent files
[ ] Network/deploy shell
[ ] Destructive shell

Score: __ / 6
Decision: Green / Yellow / Red

Agent may run:
Agent must ask before:
Agent must not touch:
Files to exclude from context/logs:
```

Keep this receipt with the task handoff before the agent starts work.
