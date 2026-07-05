# Preflight before E2B code-interpreter agents

Buyer segment: teams using E2B sandboxes, code-interpreter SDKs, or agent runtimes that execute code against a real repository, template, API key, or project environment.

Named public target evidence:

- `e2b-dev/E2B` is live at https://github.com/e2b-dev/E2B.
- GitHub API snapshot captured 12,844 stars, updated `2026-07-05T13:31:07Z`.
- Description: Open-source, secure environment with real-world tools for enterprise-grade agents.
- Existing free-repo distribution route: https://github.com/e2b-dev/awesome-ai-sdks/pull/261

## Why this matters before an E2B-backed agent run

A sandbox makes execution cleaner, but it does not decide what repo files, environment variables, mounted paths, package scripts, CI workflows, or project tokens the agent should receive. A five-minute local preflight gives the human owner a receipt before the agent gets code execution scope.

Run the free lite check before handing an E2B-backed agent a repo:

```bash
python3 agent_preflight_lite.py /path/to/repo
```

If your team uses the free Claude Code bridge, run `/agent-preflight` as the same pre-agent receipt before the E2B-backed run.

Look especially for:

- `.env`, `.env.local`, API key templates, or files mentioning `E2B_API_KEY`;
- Dockerfiles, sandbox templates, startup scripts, or package scripts that the agent may execute;
- MCP, Claude Code, Codex, Cursor, OpenCode, or browser-agent config files that can widen tool scope;
- GitHub Actions or deploy scripts that can turn a sandbox test into a production-side effect.

## Green / Yellow / Red decision

- **Green:** no secret-adjacent files, no deploy scripts, no broad mounted paths, and only narrow test commands. Proceed with a limited sandbox run and keep the free receipt.
- **Yellow:** repo has env templates, Docker or package scripts, agent config files, or workflow files. Use the paid starter pack to turn the one-off check into a reusable preflight report and command-allowance note.
- **Red:** real API keys, destructive shell commands, production deploy hooks, broad mounts, or unclear checkout state. Stop before the E2B agent runs, remove secrets, narrow scope, then use the full pack before retrying.

## Pasteable handoff note

```text
E2B agent preflight receipt: <link or paste scan result>
Allowed first run: inspect files, install dependencies only if listed, run tests already in package scripts.
Do not: read unneeded env files, modify workflow/deploy files, run destructive shell commands, or touch payment/admin surfaces.
Escalate if the scan is Yellow or Red before widening sandbox access.
```

## When the $7 pack is worth buying

Buy the full AI Agent Safety Starter Pack when the scan is Yellow or Red, or when this preflight will become a repeated handoff step for several repositories or team members. The paid bundle adds report templates, a destructive-command hook, a buyer quickstart, a demo risky repo, and local verification scripts so the E2B preflight is repeatable instead of ad hoc.

Payhip: https://payhip.com/b/1nmxV
