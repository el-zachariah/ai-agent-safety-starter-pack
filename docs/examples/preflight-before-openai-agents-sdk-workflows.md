# Preflight before OpenAI Agents SDK workflows

Target buyer segment: teams evaluating or running [`openai/openai-agents-python`](https://github.com/openai/openai-agents-python) or similar OpenAI Agents SDK workflows before giving agents repo files, function tools, MCP/tool connectors, package scripts, API keys, or hosted runner permissions.

Public fit evidence captured 2026-07-05: `openai/openai-agents-python` describes itself as “A lightweight, powerful framework for multi-agent workflows,” was public/non-archived, had 27,660 GitHub stars, and was updated 2026-07-05T15:01:20Z.

## 60-second preflight receipt

Paste this into the run ticket before the agent run starts:

```text
OpenAI Agents SDK preflight — <repo or task>
Scan command: python3 agent_preflight_lite.py <repo> --json
Decision: Green / Yellow / Red
Findings:
- Agent instructions/config reviewed: <yes/no + files>
- Tool/function access reviewed: <yes/no + tools>
- MCP/API connectors reviewed: <yes/no + configs>
- Package/install/test scripts reviewed: <yes/no + scripts>
- Secret-adjacent files excluded or scoped: <yes/no + files>
May run without asking: <commands>
Must ask first: package install, deploy, external API mutation, file deletion, credential/env changes
Must not touch: secrets, production data, billing/payment, destructive shell, private keys
Owner checkpoint: <person or issue link>
```

## Why this matters for this buyer

OpenAI Agents SDK-style projects often combine:

- planner/worker or handoff patterns where one agent can trigger another,
- Python package scripts and local test commands,
- function tools with external side effects,
- model/API credentials in `.env` or runner configuration,
- hosted or local execution that can make risky shell mistakes feel automated.

The free scanner does not replace review, sandboxing, or secret scanning. It gives the team a visible handoff receipt before the first tool-enabled run.

## Buy / skip trigger

Skip the paid bundle if the scan is Green: zero or one low-risk signal, no secret-adjacent files, no unreviewed tool config, and no package/deploy scripts the agent might run.

Buy the [$7 starter pack](https://payhip.com/b/1nmxV) if the scan is Yellow or Red: two or more risk buckets, `.env` or API credentials, MCP/tool connectors, package scripts, workflow files, or shell commands the agent may execute. The paid pack saves the setup work of turning this one-off receipt into a reusable preflight workflow, destructive-command hook, report template, demo risky repo, and verifier.

## Copy-paste handoff note

```text
Before using OpenAI Agents SDK tools in this repo, run the free preflight and attach the receipt. If the result is Yellow/Red, do not widen tool scope until the repo owner has reviewed package scripts, MCP/API config, secret-adjacent files, and destructive shell patterns. Use the paid workflow only when that review needs to be repeated across tasks or teammates.
```
