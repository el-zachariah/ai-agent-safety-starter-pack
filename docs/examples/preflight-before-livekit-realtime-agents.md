# LiveKit realtime agent preflight receipt

Customer segment: teams using [livekit/agents](https://github.com/livekit/agents) to ship realtime voice/video AI agents with tool calls, worker processes, and room/session credentials.

Public target verified: `livekit/agents` is active, not archived, has 11,246 GitHub stars, and was last updated `2026-07-06T11:54:55Z`. Description observed: A framework for building realtime voice AI agents 🤖🎙️📹 

Why this buyer should care before paying for more automation:

- Realtime agents often combine microphone/video rooms, token minting, webhooks, tool calls, and background workers; a single over-broad agent instruction or leaked `.env` can turn a demo into a production incident.
- The free scanner proves the repo can be checked locally before an agent, contractor, or coding model modifies the project.
- The paid $7 pack is justified when the scan is Yellow/Red and the team needs a copy-paste remediation checklist plus a PR-ready preflight receipt.

## 3-minute local preflight for a LiveKit agents repo

```bash
python3 scripts/agent_preflight_lite.py /path/to/livekit-agent-app --format markdown > preflight-livekit-agent.md
python3 scripts/agent_preflight_lite.py /path/to/livekit-agent-app --format json > preflight-livekit-agent.json
```

Inspect the report for:

1. `.env`, token, room, SIP, TURN, or webhook secrets committed near agent code.
2. Prompt/instruction files that let an agent run shell commands, edit deployment config, or access session credentials without a review gate.
3. Worker/process files that mix realtime room handling with unreviewed tool-call execution.
4. CI or deploy steps that would publish generated agent changes without a human preflight receipt.

## Buy / skip trigger

- **Skip the paid pack** if the free scan is Green and no realtime credentials, worker deploy scripts, or tool-call instructions are in scope.
- **Buy the $7 pack** if the free scan is Yellow/Red or if a maintainer needs a PR-ready receipt before accepting AI-agent changes.
- **Use the service upsell** only when a team wants the receipt adapted to its LiveKit deployment workflow.

## Copy-paste receipt for a LiveKit agent PR

```md
Agent preflight completed for LiveKit realtime-agent changes.

- Scope checked: room/session credential paths, worker process files, tool-call prompts, webhook/deploy config.
- Free scan output attached: preflight-livekit-agent.md / preflight-livekit-agent.json.
- Decision: Green / Yellow / Red.
- Paid-pack trigger: buy only if Yellow/Red or if a maintainer needs the remediation checklist before merge.
```

Source repo for the free scanner: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>
Paid checklist/receipt bundle: <https://payhip.com/b/1nmxV>
