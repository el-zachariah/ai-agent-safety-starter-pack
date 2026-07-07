# Pre-checkout decision receipt

Use this before paying if you want a short, public-safe yes/no check instead of reading the whole proof trail. It turns the free lite scan into a decision you can keep in a team handoff note without sharing private source code.

`PRECHECKOUT_DECISION_RECEIPT_2026_07_07`

## 1. Run the free scan locally

```bash
python3 agent_preflight_lite.py /path/to/repo
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-lite.json
```

Keep the JSON local if it contains private paths, filenames, or internal workflow names.

## 2. Copy this receipt into your task note

```text
AI-agent repo preflight decision

Repo context: <public-safe description only>
Agent path: <Claude Code / Cursor / Codex / MCP tool / browser agent / other>
Planned agent powers: <read files / edit files / run shell / open PRs / deploy / other>

Free scan result:
- Agent instructions or tool config: yes/no
- Package scripts, workflows, deploy hooks, or migrations: yes/no
- Secret-adjacent files or local credential config: yes/no
- Risky shell patterns or destructive commands: yes/no
- MCP/Cursor/Claude/GitHub Copilot/Dev Container/Replit config: yes/no

Decision:
- Green: keep using the free scanner and normal review.
- Yellow: buy the $7 pack if a tool-enabled agent run is imminent and you need the reusable handoff/report template.
- Red: pause the agent run until the handoff and destructive-command guardrail exist; the paid pack is meant for this case.

Private-data rule: do not paste private code, secrets, credentials, card details, billing data, or order identifiers into public support issues.
```

## 3. What counts as Green / Yellow / Red

- **Green:** zero or one low-risk bucket, no agent/tool config, no risky install/deploy scripts, and no secret-adjacent files. Skip the paid pack for now.
- **Yellow:** two or more buckets, package scripts, CI/workflow files, agent instructions, MCP/Cursor/Claude config, or repo-specific shell commands an agent may try to run. Buy only if you need the repeatable report, hook, and verifier before the run.
- **Red:** destructive shell, secret-adjacent config, deployment/migration commands, production-like workflow files, or agent/tool settings that could touch private repo state. Pause and write the handoff before granting tool access.

## 4. If you are still unsure

Open the public-safe buyer question form and describe only the non-private symptom, operating system, and which step was confusing:

<https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>

Paid bundle: <https://payhip.com/b/1nmxV>
