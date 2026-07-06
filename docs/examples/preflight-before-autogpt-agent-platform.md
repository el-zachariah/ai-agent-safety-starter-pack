# AutoGPT agent platform preflight proof

**Named buyer segment:** teams using [`Significant-Gravitas/AutoGPT`](https://github.com/Significant-Gravitas/AutoGPT) or AutoGPT-style agent platforms before autonomous workflows receive repository context, tool/API connectors, package scripts, workflow files, browser/API actions, or secret-adjacent configuration.

**Public target evidence captured this pulse:** `Significant-Gravitas/AutoGPT` is public and not archived, with 185,402 GitHub stars observed, updated `2026-07-06T12:43:48Z`, and description: "AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.".

## Why AutoGPT-style teams should run the free preflight first

AutoGPT-style agent platforms can turn a high-level goal into chained steps, tool calls, generated files, browser/API actions, and follow-up commands. The risky moment is when the workflow moves from demo prompts into a real repo with package scripts, deployment settings, credentials, or write-capable tools.

Run the free scanner before the platform gets broad scope:

```bash
python3 agent_preflight_lite.py /path/to/autogpt-workspace --json > autogpt-agent-preflight.json
python3 agent_preflight_lite.py /path/to/autogpt-workspace > autogpt-agent-preflight.md
```

Attach the Markdown receipt to the issue, PR, or run ticket before widening the agent from read-only planning to repo writes, package-script execution, API connectors, browser actions, or deployment workflows.

## Buy / skip trigger for AutoGPT agent-platform teams

- **Green:** demo prompt, read-only repo context, no package scripts, no API/tool credentials, no deploy or browser automation. Skip the paid pack for now.
- **Yellow:** package scripts, workflow files, tool/API config, generated commands, or secret-adjacent paths are present. Review the receipt before the AutoGPT-style workflow continues.
- **Red:** the agent will write files, run package/deploy scripts, use browser/API credentials, or touch production automation. Buy the [$7 starter pack](https://payhip.com/b/1nmxV) for the repeatable hook, reviewer prompt, rollback checklist, and handoff receipt before the run.

## Copy-paste run-ticket receipt

```text
AutoGPT agent platform preflight receipt
- Repo/workspace: <name>
- Agent goal: <goal>
- Allowed actions: <read-only | scoped edits | commands allowed>
- Blocked actions: package/deploy scripts, browser/API credentials, secret-adjacent files unless approved
- Free scanner result: <Green | Yellow | Red>
- Decision: if Yellow/Red, use the $7 AI Agent Safety Starter Pack before enabling broad agent/tool scope
```

Marker: `AUTOGPT_AGENT_PLATFORM_PROOF`

This is an independent preflight example for AutoGPT-style workflows; it is not affiliated with or endorsed by AutoGPT.
