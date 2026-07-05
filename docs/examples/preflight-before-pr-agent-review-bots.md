# Preflight before PR-Agent review bots

Target buyer segment: maintainers and small teams using [`The-PR-Agent/pr-agent`](https://github.com/The-PR-Agent/pr-agent) or similar PR review agents before giving an AI bot repository context, issue/PR permissions, workflow secrets, package scripts, or comment-triggered automation scope.

Public fit evidence captured 2026-07-05: `The-PR-Agent/pr-agent` was public/non-archived, had 11,969 GitHub stars, was updated `2026-07-05T18:04:49Z`, and described itself as “🚀 PR Agent: The Original Open-Source PR Reviewer.  This project It is not the Qodo free tier.”.

## 60-second PR-Agent preflight receipt

Paste this into the pull request or run ticket before enabling the review bot on a real repository:

```text
PR-Agent review bot preflight — <repo / PR / task>
Scan command: python3 agent_preflight_lite.py <repo> --json
Decision: Green / Yellow / Red
Findings:
- Repo instructions reviewed: <yes/no + files>
- Workflow/CI permissions reviewed: <yes/no + workflows>
- Package/install/test scripts reviewed: <yes/no + scripts>
- Comment-triggered actions reviewed: <yes/no + labels/commands>
- Secret-adjacent files excluded or scoped: <yes/no + files>
May run without asking: read-only review, summary, local tests already approved
Must ask first: package install, workflow dispatch, external API mutation, file deletion, repo setting changes
Must not touch: secrets, deployment keys, billing/payment/admin settings, destructive shell, private data
Owner checkpoint: <person or issue link>
```

## Why this matters for this buyer

PR-agent-style automation usually feels safer than a shell agent because it appears as a review assistant, but it can still inherit sensitive repo context and automation edges:

- pull request comments, labels, or slash commands can trigger agent behavior,
- CI/workflow files can reveal what the bot may run or suggest changing,
- package scripts and generated code paths can turn a simple review into execution risk,
- maintainers need a visible receipt before widening permissions or trusting bot-generated patches.

The free scanner does not replace branch protection, CI permissions, code review, sandboxing, or secret scanning. It gives maintainers a cheap visible handoff before PR automation gets trusted.

## Buy / skip trigger

Skip the paid bundle if the scan is Green: zero or one low-risk signal, no workflow secrets, no unreviewed package/deploy scripts, and no comment-triggered automation that can mutate the repo.

Buy the [$7 starter pack](https://payhip.com/b/1nmxV) if the scan is Yellow or Red: two or more risk buckets, workflow files, package scripts, secret-adjacent files, agent instructions, or risky shell commands. The paid pack saves the setup work of turning this one-off PR receipt into a reusable repo preflight workflow, destructive-command hook, report template, demo risky repo, and verifier.

## Copy-paste maintainer note

```text
Before enabling PR-Agent on this repo or asking it to act beyond read-only review, run the free preflight and attach the Green / Yellow / Red receipt. If the result is Yellow/Red, review workflow permissions, package scripts, secret-adjacent files, and comment-triggered actions before widening bot scope.
```
