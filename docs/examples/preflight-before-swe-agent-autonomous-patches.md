# Preflight before SWE-agent-style autonomous patches

Target segment: teams using SWE-agent-style autonomous issue-to-patch agents in real repositories.

Public target evidence captured 2026-07-05T07:59:09-05:00:

- Target repo: [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent)
- Stars observed: 19,705
- Last pushed/updated: `2026-07-01T15:40:48Z`
- Description: SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] 
- Topics observed: agent, agent-based-model, ai, cybersecurity, developer-tools, llm, lms

## Why this buyer should care

SWE-agent-style workflows are close to the exact risk moment this product is built for: an autonomous coding agent reads repo instructions, edits files, runs tests, and may touch package scripts or workflow files while trying to solve an issue. The free scanner gives the team a visible receipt before widening that agent's shell/tool scope.

## 60-second free receipt

Run this before the autonomous patch attempt, not after the agent has already inherited the repo context:

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-swe-agent.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-swe-agent.md
```

Attach the Markdown receipt to the SWE-agent task, issue, or run notes.

## Pasteable SWE-agent handoff

```text
Preflight before autonomous patch run:
- Decision: Green / Yellow / Red = <paste scanner decision>
- Risk buckets: <paste scanner buckets>
- Agent may run: targeted tests, formatters, and read-only repo inspection.
- Agent must ask before: package installs, network calls, Docker/socket access, workflow/secret/env changes, deploy/publish scripts, or broad file rewrites outside the issue scope.
- Agent must not: modify secret-adjacent files, expand CI permissions, or run destructive cleanup commands.
- Human review focus: files flagged by the preflight plus any install/test/build commands the agent proposes.
```

## Buy/skip trigger for this segment

Skip the paid pack if the scan is Green and the agent will only touch a small code path with normal review.

Buy the `$7` starter pack if the scan is Yellow/Red and the team wants a reusable report template, destructive-command hook, demo risky repo, and verifier before letting SWE-agent-style automation attempt real issue patches.

## First buyer proof angle

This page exists so an autonomous-agent user can see the product is not generic safety copy. It gives a concrete pre-run receipt for the exact moment a SWE-agent-style tool is about to edit and test a real checkout.
