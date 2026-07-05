# CI preflight recipe for AI-agent pull requests

Use this free recipe when an AI coding agent is about to open or update a pull request and you want a fast repo-risk receipt before review. It keeps the free scanner useful for teams while reserving the full reusable hook/report workflow for the paid bundle.

## When to use it

- A Claude Code, Codex, Cursor, or MCP-backed agent will edit a real repository.
- The repo has package scripts, GitHub Actions, deployment files, agent instructions, or secret-adjacent config.
- You want the reviewer to see a Green / Yellow / Red preflight result before merging agent-written changes.

## Copy-paste GitHub Actions step

Add the free scanner to an existing CI workflow after checkout:

```yaml
- name: AI-agent repo preflight
  run: |
    python3 agent_preflight_lite.py . --json > agent-preflight-lite.json
    python3 agent_preflight_lite.py . > agent-preflight-lite.md
    cat agent-preflight-lite.md
```

If the job runs in another repository, copy `agent_preflight_lite.py` into a tooling folder first or fetch it from the public repo at a pinned commit. Keep the generated `agent-preflight-lite.md` with the PR notes when the scan is Yellow or Red.

## Reviewer decision rule

- **Green**: normal review is usually enough.
- **Yellow**: add a short run / ask / avoid note before allowing install, test, build, or deploy commands.
- **Red**: stop and add a reusable preflight report plus a command guardrail before the agent gets shell access.

## Why the paid pack exists

The free CI recipe surfaces the risk signal. The `$7` starter pack is for teams that want the repeatable handoff: full report template, destructive-command hook examples, demo risky repo/report, buyer quickstart, and local verifier so every agent run gets the same guardrails instead of a one-off note.

Payhip bundle: https://payhip.com/b/1nmxV
