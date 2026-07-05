# Preflight before OpenHands-style autonomous repo agents

Customer segment: teams evaluating or running OpenHands / Devin-style autonomous coding agents against real repositories before a human has reviewed blast radius.

Why this matters now: `All-Hands-AI/OpenHands` is a live autonomous software-engineering-agent project (79473 GitHub stars; updated 2026-07-05T11:07:21Z). Its audience is exactly the kind of buyer who wants a fast, pasteable safety receipt before letting an agent plan, edit, run tests, or open a PR.

Use this free preflight as the **before agent starts** receipt. It does not replace OpenHands. It gives a maintainer or team lead one visible go/no-go note to decide whether the repo is safe enough for autonomous work.

## 60-second free receipt

From a clean checkout of the target repo:

```bash
python3 tools/lite_repo_preflight.py --path . --markdown preflight-openhands.md --json preflight-openhands.json
```

Paste the Markdown summary into the issue/PR/run ticket before starting the autonomous agent.

## What to look for in an OpenHands-style repo

| Signal | Why it matters before autonomous edits | Fast action |
|---|---|---|
| Missing tests or no obvious test command | The agent can make plausible edits with no executable proof | Add the exact test command to the run ticket |
| Broad write surface (`scripts/`, infra, CI, generated files) | One agent task can touch high-blast-radius files | Restrict the first run to docs/tests/small module paths |
| Secret-looking config (`.env`, tokens, private endpoints) | Agent context can accidentally expose sensitive setup | Replace secrets with `.env.example` before the run |
| Existing CI or policy checks | Lets the agent produce evidence instead of a vague completion claim | Require CI/test output in the final PR comment |
| Large lockfiles or vendored assets | Diffs become noisy and hard to review quickly | Tell the agent not to rewrite generated dependencies |

## Buy / skip rule for this segment

- **Green receipt:** skip the paid pack for now; keep the Markdown note in the ticket and proceed with a small scoped agent task.
- **Yellow receipt:** use the $7 pack if the repo has unclear tests, risky scripts, or broad agent permissions. The paid pack adds the handoff checklist, review-comment templates, and stricter buyer-side acceptance notes.
- **Red receipt:** do not hand the repo to an autonomous agent yet. Fix secrets, missing tests, or broad write permissions first; then rerun the preflight.

## Pasteable run-ticket note

```text
Before OpenHands-style autonomous work starts, I ran the free repo preflight.
Decision: <Green / Yellow / Red>
High-risk files or settings: <list>
Allowed first-run scope: <paths or tasks>
Required proof before merge: <test command, CI link, review comment>
If this is Yellow/Red, use the full AI Agent Safety Starter Pack before widening the agent scope.
```

Paid upgrade when the receipt is Yellow/Red: https://payhip.com/b/1nmxV

Related free proof pages:

- [Claude Code hook/TDD proof](./claude-code-hook-preflight-proof.md)
- [Continuous agent preflight example](./preflight-before-continuous-claude.md)
- [Multi-harness marketplace proof](./preflight-for-multi-harness-agent-marketplaces.md)
