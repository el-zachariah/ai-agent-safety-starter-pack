# Preflight before Pipecat voice agent workflows

Marker: `PIPECAT_VOICE_AGENT_PROOF`

Public target verified for this buyer proof:

- Repository: [`pipecat-ai/pipecat`](https://github.com/pipecat-ai/pipecat)
- GitHub stars when verified: `13229`
- Last updated when verified: `2026-07-06T20:57:45Z`
- Verified at: `2026-07-06T16:08:41-05:00`
- Why it fits: teams building voice/multimodal agents are about to connect LLM, STT, TTS, transport, and deployment keys before autonomous edits. That is exactly the checkout-start friction this funnel must answer: prove the seller understands the buyer's live workflow before asking them to buy the paid templates.

## Who this is for

Use this receipt before a Pipecat voice/multimodal agent workflow lets Claude Code, Codex, Cursor, or another coding agent edit agent code, run package scripts, touch deployment config, or inspect secret-adjacent files.

This is not a security audit of `pipecat-ai/pipecat`. It is a short pre-run workflow for the team about to run agents in its own repo.

## 60-second receipt

Run the free scanner first:

```bash
python3 agent_preflight_lite.py /path/to/your/repo --json
python3 agent_preflight_lite.py /path/to/your/repo > agent-preflight-pipecat-voice-agent-workflows.md
```

Paste the short decision into the task handoff:

```text
PIPECAT_VOICE_AGENT_PROOF
Target agent workflow: Pipecat voice/multimodal agent workflow
Repo scanned: <repo/path or commit>
Decision: Green / Yellow / Red
Risk buckets present: <LLM/STT/TTS keys, transport adapters, deployment scripts, .env-adjacent files, and package scripts>
Allowed before agent run: <read-only / tests only / no shell / no secrets / specific commands>
Must ask first: <deploy, destructive commands, credential use, external network calls>
Reviewer: <person/team>
```

## Buy / skip trigger for the $7 pack

- **Green:** keep the free scanner output with the run notes. Do not buy just because `pipecat-ai/pipecat` is popular.
- **Yellow:** buy the `https://payhip.com/b/1nmxV` pack if the scan shows two or more buckets, package scripts, workflow files, agent/tool config, or secret-adjacent paths and you need a reusable handoff template.
- **Red:** buy the pack before the agent run if destructive shell, credential-adjacent files, deploy scripts, or broad tool/API access are in scope; use the included destructive-command hook and report template before granting shell access.

## What the paid pack saves

The paid pack gives the repeatable report template, destructive-command hook, risky demo repo, buyer quickstart, and verifier so a Pipecat voice/multimodal agents team does not rebuild the handoff and guardrail after the scan already found Yellow/Red risk.
