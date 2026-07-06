# Strands Agents SDK workflow preflight proof

Target evidence verified 2026-07-06T14:10:53-05:00: [`strands-agents/harness-sdk`](https://github.com/strands-agents/harness-sdk) is public, not archived, shows 6440 GitHub stars, and was updated at `2026-07-06T18:49:22Z`. Repository description: Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud.

This page is for a team evaluating Strands Agents SDK-style agent work before an AI assistant gets repo, shell, tool, or credential-adjacent scope. It makes the $7 starter pack feel concrete: run the free scan first, then buy only when the result is Yellow/Red enough to need a reusable handoff.

Marker: `STRANDS_AGENTS_SDK_WORKFLOW_PROOF`

## 60-second preflight receipt

Paste this into the issue, PR, runbook, or agent task before a Strands Agents SDK session begins:

```text
Strands Agents SDK workflow preflight receipt
Target repo: strands-agents/harness-sdk
Free scan command: python3 agent_preflight_lite.py . --json
Agent scope requested: <files/tools/shell/network/deploy scope>
Risk color: Green / Yellow / Red
Findings to review before tool access:
- agent instructions and local tool config
- agent tools, MCP/API connectors, package scripts, notebooks, deployment config, or secret-adjacent AWS/provider env values
- package, workflow, deploy, or notebook commands the agent may run
- secret-adjacent files that should be excluded or replaced with test fixtures
Allowed commands now: <list>
Must ask before: destructive shell, deploy, credential read/write, or external submission
Decision: proceed / narrow scope / stop
```

## Green / Yellow / Red buy trigger

- **Green:** zero or one low-risk signal, no secret-adjacent config, and no package/deploy scripts in the requested agent scope. Use the free scanner and normal review.
- **Yellow:** the scan finds agent/tool config plus scripts, AWS or provider credential-adjacent files, workflow YAML, notebooks that call tools, or shell commands the agent may execute. Buy the $7 pack when you need the reusable handoff template, report shape, and destructive-command guard instead of rewriting the receipt each time.
- **Red:** destructive shell, deploy credentials, production env files, writable workflow permissions, or unclear external API/tool side effects are in scope. Do not hand the agent tools until the scope is narrowed and the receipt is approved.

## Why this is relevant to Strands Agents SDK users

Strands Agents SDK work usually combines generated code, package commands, tool calls, workflow files, and env/config decisions. A cheap preflight prevents the first run from becoming an unreviewed shell/deploy/secret-adjacent session.

Start free: run the public scanner from this repo. Upgrade only when the receipt is Yellow/Red and you want the reusable workflow bundle: https://payhip.com/b/1nmxV

This is not a security audit, sandbox, malware scanner, or guarantee. It is a pre-tool-access checklist and receipt for teams deciding whether an agent run is safe enough to continue.
