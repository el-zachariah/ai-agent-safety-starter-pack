# Preflight before OpenAI Codex CLI / PR-agent work

Customer segment: teams using **openai/codex**-style AI coding agents that can inspect, edit, test, and open PRs against real repositories.

Target evidence captured in this deadline pulse:

- Repository: [openai/codex](https://github.com/openai/codex)
- Public description: Lightweight coding agent that runs in your terminal
- Stars observed: 95599
- Last updated observed: 2026-07-05T11:50:04Z
- Topics observed: not listed

## Why this segment should care before buying

Codex-style agents feel productive because they can move quickly through a repo, but that same speed makes a cheap preflight receipt valuable when the repo has risky scripts, token-shaped environment variables, generated files, or CI commands that should not be trusted blindly.

The free repo gives a public, copyable preview. The paid **AI Agent Safety Starter Pack** is the low-friction upgrade when the scan is Yellow/Red and a buyer needs the fuller handoff bundle, richer checklists, and copy-paste review language before letting an AI coding agent continue.

## 5-minute workflow before handing a repo to Codex

1. Run the lite scanner against the target repo before the agent starts editing.
2. Paste the receipt into the Codex task as a non-negotiable guardrail.
3. Tell the agent which commands are allowed, which files are off-limits, and which findings require a human pause.
4. Require the agent to include the preflight receipt in its final PR/comment so reviewers can verify the risk posture.
5. If the scanner returns **Yellow** or **Red**, buy the $7 pack for the fuller repo handoff/checklist language before continuing.

## Copy-paste guardrail for a Codex task

```markdown
Before changing code, read this preflight receipt and obey it as part of the task contract.

- Do not run install/build/test commands that the receipt marks as risky without explicit approval.
- Do not print, exfiltrate, or transform token-shaped environment variables.
- Keep generated files, lockfiles, and vendored directories untouched unless the task explicitly requires them.
- In your final response or PR body, include a short "Preflight receipt" section with the current Green/Yellow/Red result and any skipped risky command.

If the receipt is Yellow or Red, stop after proposing the safe next command list unless the owner approves the paid handoff checklist.
```

## Example receipt snippet

```markdown
Preflight receipt for Codex CLI handoff

Decision: YELLOW — continue only with constrained commands.
Risk buckets:
- install scripts present in package metadata
- token-shaped environment variable names referenced in docs
- CI workflow can deploy on push

Allowed now:
- inspect files
- run read-only tests already documented by the maintainer
- draft patch without executing deploy/install scripts

Pause before:
- npm install / postinstall scripts
- shell scripts that touch network, credentials, or deployment
- PR comments that claim production verification without logs
```

Paid upgrade trigger: buy the $7 pack at <https://payhip.com/b/1nmxV> when the agent needs the fuller handoff language, reviewer template, and safety checklist rather than a one-off lite receipt.
