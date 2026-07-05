# Preflight before OpenHands task branches

**Customer segment:** teams using [OpenHands](https://github.com/OpenHands/OpenHands) or similar autonomous software-engineering agents to open task branches, run shell commands, and change real repositories.

**Public evidence checked:** `OpenHands/OpenHands` is active (`updated_at=2026-07-05T14:48:56Z`) with `79487` GitHub stars. Repository description at check time: "🙌 OpenHands: AI-Driven Development".

## Why this proof exists

OpenHands-style agents are useful because they can investigate, edit, run tests, and produce a branch or pull request with little manual steering. That also means the first bad run can spend time on a stale branch, hit unsafe package scripts, leak unnecessary context, or create a noisy PR before anyone has a clean receipt of what was checked.

Run the free lite preflight **before** giving the agent a task branch. If the result is Yellow or Red, use the paid $7 workflow bundle to standardize the handoff, patch request, and review comment before the agent gets broad repo scope.

## 60-second command

From the repository the OpenHands agent will work on:

```bash
python3 agent_preflight_lite.py --repo . --format markdown --output preflight-openhands.md
python3 agent_preflight_lite.py --repo . --format json --output preflight-openhands.json
```

If you are running OpenHands in a container or remote workspace, copy this repo preflight into the same checkout that the agent will mutate, then attach `preflight-openhands.md` to the task issue, branch note, or PR description.

## What to inspect before the agent starts

| Surface | What the lite preflight catches | Why OpenHands users care |
|---|---|---|
| Git cleanliness | dirty worktree, untracked files, detached HEAD | prevents agents from mixing human edits with generated patches |
| Package scripts | install/test/build hooks and risky package-script names | identifies package-script command surfaces before autonomous shell execution |
| CI/workflows | GitHub Actions and automation config | keeps agent PRs from surprising maintainers with workflow changes |
| Secret-looking files | `.env`, key/cert names, credential-like paths | reduces accidental context exposure in task logs or patches |
| Agent config | MCP/tooling/config files when present | scopes what the agent can call before it starts editing |

## Paste-ready task note

```markdown
Before OpenHands starts this task branch, I ran the repo preflight.

- Decision: Yellow / Red / Green
- Risk buckets: <paste from preflight-openhands.md>
- Files/scripts to avoid or review first: <paste>
- Human guardrail: OpenHands may edit code and run tests, but package/workflow/security-sensitive changes need review before merge.

If Yellow/Red, use the paid Agent Safety Starter Pack workflow to turn this into a repeatable task prompt + review receipt.
```

## Buy trigger

Buy the [$7 AI Agent Safety Starter Pack](https://payhip.com/b/1nmxV) when:

- OpenHands is about to touch a production repo, CI workflow, package manager, auth, deploy, or MCP/tooling config.
- The lite scan reports Yellow/Red and you need a reusable handoff, review-comment, and escalation template.
- You want the same receipt style across Claude Code, Cursor/Continue, Goose, LangGraph, SWE-agent, and OpenHands runs.

Skip buying for now if the repo is a disposable toy project, the lite scan is Green, and no one else needs a review receipt.
