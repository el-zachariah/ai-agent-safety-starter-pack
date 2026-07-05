# Qwen Code CLI preflight proof

**Named buyer segment:** teams evaluating `QwenLM/qwen-code` / Qwen-style coding agents before letting a terminal AI assistant edit repos, run package scripts, use MCP or tool connectors, or touch API-backed `.env` values.

**Public target evidence checked 2026-07-05T17:30:26-0500:** `QwenLM/qwen-code` is live at https://github.com/QwenLM/qwen-code; GitHub API observed `25794` stars and `updated_at=2026-07-05T18:20:06Z`. Description captured: "An open-source AI coding agent that lives in your terminal.".

## Why this matters before a Qwen-style agent run

Qwen Code / Qwen-Agent-style workflows are attractive because they can sit close to the terminal, repo tree, tests, tool calls, MCP/context providers, and deployment scripts. That is exactly the moment a small team needs a visible preflight receipt before giving the agent broad scope.

The free scanner in this repo gives the first-pass proof:

```bash
python3 tools/agent_preflight_lite.py --repo /path/to/your/repo --format markdown
```

Look for:

- `.env`, token, or credential-adjacent files the agent could read;
- package scripts that can run arbitrary shell commands;
- repo-level agent instructions or workflow config that can redirect the assistant;
- MCP/tool connector files that may expose external actions;
- CI or deployment files that can turn a local agent change into a production side effect.

## Checkout-start trigger

- **Green scan:** use the free README and scanner; skip the paid pack for now.
- **Yellow scan:** buy the $7 pack if you need the copy-paste issue comment, review checklist, and handoff wording before assigning Qwen-style agent work.
- **Red scan:** buy before running the agent against the repo; use the paid checklist as the minimum receipt for secrets, package scripts, MCP/tool connectors, and deployment scope.

Paid pack: <https://payhip.com/b/1nmxV>

## Example maintainer receipt

> I ran the preflight before letting a Qwen-style coding agent work in this repo. Current result: Yellow/Red because the repo has package scripts, environment files, and tool connector config. I am applying the paid starter checklist before allowing broad edit/test/shell scope.

This proof is not a security audit. It is a buyer-facing sanity receipt that makes the $7 upgrade feel concrete for teams already near an AI-agent run.
