# Preflight before Agentic Radar security scans

Named buyer segment: teams evaluating [`splx-ai/agentic-radar`](https://github.com/splx-ai/agentic-radar) or a similar LLM / agentic-workflow security scanner before an AI coding agent receives repo, package-script, MCP, API, browser, or secret-adjacent scope.

Public target evidence captured for this pulse: `splx-ai/agentic-radar` is live/non-archived, observed at 992 GitHub stars, updated `2025-11-27T15:28:44Z`, and describes itself as: A security scanner for your LLM agentic workflows

Why this is a checkout-start proof: Agentic Radar-style users already believe agentic workflows can fail dangerously, but a broad scanner does not automatically create the small repo handoff receipt a maintainer needs before starting Claude Code, Codex, Cursor, MCP tools, or a CI-backed agent run. This free proof shows the exact lightweight receipt; the paid bundle is only for teams that want the reusable report template, destructive-command hook examples, buyer quickstart, verifier, and demo risky repo.

## 60-second preflight before the security scan or agent run

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agentic-radar-preflight.json
python3 agent_preflight_lite.py /path/to/repo > agentic-radar-preflight.md
```

Record these before widening scope:

1. Agentic workflow being evaluated: Agentic Radar / security scanner / Claude Code / Codex / Cursor / MCP runner.
2. Repo scope: read-only, branch-only edits, allowed package scripts, allowed CI jobs, and whether browser/API tools are enabled.
3. Free preflight decision: Green, Yellow, or Red.
4. Must-ask-before actions: package install hooks, deploy scripts, migrations, secret-adjacent files, MCP credentials, API-backed tools, browser automation, and shell commands that write outside the repo.
5. Receipt owner: the maintainer or teammate who can say the agent run is safe enough to start.

## Buy / skip trigger for this segment

- **Green:** keep the free receipt next to the Agentic Radar/security-scan result; do not buy yet.
- **Yellow:** buy the $7 pack if the same repo has package scripts, MCP/API connectors, repo instructions, workflow secrets, browser tools, or deployment config that a coding agent may touch.
- **Red:** buy before granting write/tool access. Use the paid templates and local hook examples to standardize the reviewer note instead of inventing a one-off policy under pressure.

Paid upgrade when Yellow/Red: https://payhip.com/b/1nmxV

## Pasteable handoff receipt

```text
Agentic workflow/security scan: <Agentic Radar / Claude Code / Codex / Cursor / MCP runner>
Repo: <owner/repo or local path>
Free preflight artifact: agentic-radar-preflight.md and agentic-radar-preflight.json
Decision level: <Green / Yellow / Red>
Why it is not Green: <package scripts, repo instructions, MCP/API connectors, browser tools, workflow secrets, deploy config, secret-adjacent files>
Allowed for this run: <read-only / branch edits / specific tests / specific tools>
Must ask before: <install hooks, deploy, migration, destructive shell, credentialed API, browser action, external writes>
Paid pack needed now? <No if Green; Yes if Yellow/Red repeats across real repos or the reviewer wants reusable hooks/templates>
```
