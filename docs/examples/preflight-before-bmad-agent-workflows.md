# Preflight before BMAD agent workflows touch a real repo

Target segment: teams using [`bmad-code-org/BMAD-METHOD`](https://github.com/bmad-code-org/BMAD-METHOD) or BMAD-style agent/persona workflows to turn product briefs, stories, and dev tasks into agent-run repo work.

Public evidence captured in this pulse:

- Repo: `bmad-code-org/BMAD-METHOD`
- Description: Breakthrough Method for Agile Ai Driven Development
- Stars observed: `50106`
- Updated: `2026-07-06T03:19:08Z`

## Why this buyer should care before checkout

BMAD-style workflows are strongest when the analyst/PM/architect/dev/QA agents move fast. That speed also means a repo can pick up instructions, generated stories, package scripts, MCP/Cursor/Claude config, and secret-adjacent files before a human has written the run boundary.

Run the free lite scan first:

```bash
python3 agent_preflight_lite.py /path/to/bmad-enabled-repo --json
```

## 60-second BMAD handoff receipt

Paste this into the story/task before a coding agent begins implementation:

```markdown
BMAD agent preflight receipt
- Repo/task: <link>
- Scan result: Green / Yellow / Red
- Agent roles entering scope: analyst / pm / architect / dev / qa / other
- Must-read before action: AGENTS.md, CLAUDE.md, .bmad-core files, .cursor/rules, package scripts, workflow files
- May run: <exact commands>
- Must ask first: dependency install, migration, deploy, network call, credential touch, destructive shell, force push
- Must not touch: .env, tokens, payment/admin settings, production deploy config, customer data
- Human owner for approval: <name/channel>
```

## Buy / skip trigger for the $7 starter pack

- **Green:** no BMAD/agent config, no risky scripts, no secret-adjacent files. Keep using the free scanner and normal review.
- **Yellow:** BMAD agent files plus package scripts, workflow config, MCP/Cursor/Claude settings, or one secret-adjacent signal. Buy the `$7` pack if you need the reusable report template and command guardrail instead of rebuilding them per story.
- **Red:** BMAD workflow plus destructive shell, deploy scripts, credential-adjacent files, or multiple automation surfaces. Buy the `$7` pack before handing repo/shell scope to an agent.

Paid bundle: <https://payhip.com/b/1nmxV>

## What the paid pack saves for BMAD-style teams

- A repeatable preflight report template for every story/task handoff.
- A destructive-command hook to catch obvious shell hazards before execution.
- A demo risky repo and verifier so the workflow can be tested before a real sprint.
- A clearer Green / Yellow / Red receipt a maintainer can attach to an agent-created PR.
