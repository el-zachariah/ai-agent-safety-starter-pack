# Paid report sample preview

Marker: PAID_REPORT_SAMPLE_PREVIEW_2026_07_07

Use this page before checkout if the contents list is not enough and you want to see the shape of the reusable handoff report. It shows a sanitized sample of the paid pack output without requiring private repository details, order details, billing details, screenshots, or account access.

## What the paid report helps you decide

The paid pack is not for a Green scan. It is for a Yellow/Red scan where a tool-enabled AI agent is about to touch package scripts, MCP/Cursor/Claude settings, workflow files, deployment helpers, shell commands, or secret-adjacent paths.

The reusable report turns the scan into a short go / limited-go / no-go note:

```text
GO: no high findings and medium findings reviewed.
LIMITED GO: proceed only with read-only inspection or an isolated branch/sandbox.
NO-GO: high-risk configs/scripts/secrets need manual cleanup first.
```

## Sample handoff fields

A buyer can copy the paid report into an issue, PR note, local task file, or team handoff and fill these fields before the agent run:

```text
Repo/session
- Repo:
- Agent/tool planned: Claude Code / Codex / Cursor / OpenCode / other
- Reviewer:
- Date:
- Scan command:
- Scan report file:

Top findings to review before agent execution
| Priority | File/path | Finding | Why it matters | Action before agent run |
```

## Sample control points

The report prompts the reviewer to check the surfaces that most often surprise agent runs:

- agent instructions such as AGENTS.md, CLAUDE.md, Cursor rules, or Copilot instructions;
- MCP/tool configs such as .mcp.json or Claude settings files;
- package lifecycle scripts and shell scripts;
- CI/CD workflows;
- secret-adjacent files;
- destructive-command guardrails tested or intentionally skipped.

## Sample risky-repo excerpt

The demo bundled with the paid pack produces a small report that looks like this after scanning the included sample repository:

```text
Summary
- High: 5
- Medium: 3
- Low: 0

Example high findings
- pull_request_target workflow: inspect before agent edits.
- MCP configuration present: inspect commands, env vars, URLs, and local file access.
- recursive force-remove command: verify target path and backup before agent execution.
- remote download piped to shell: inspect source and pin/checksum before running.
```

## Allowed / blocked command note

The paid report includes a place to write the first commands the agent may run, plus the default blocked-command reminder:

```text
No force pushes, recursive deletes, disk formatting, cloud/prod deploys, credential edits, billing/auth changes, or CI/CD changes without manual approval.
```

## Buy / skip rule

- **Green scan:** keep the free lite scanner and normal review discipline.
- **Yellow scan:** buy the $7 pack when you need the reusable report, destructive-command hook, demo report, and verifier before the agent continues.
- **Red scan:** pause the agent run, use the paid pack only after the risky surfaces are reviewed, and keep private details out of public support.

Checkout: <https://payhip.com/b/1nmxV>

Related public proof before checkout:

- ZIP contents preview: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/paid-bundle-contents-preview.md>
- Local-only privacy note: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/privacy-before-checkout.md>
- Public-safe support path: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>
