# Preflight before Roo Code agent teams

**Roo Code agent-team preflight proof.** Use this when a team is about to let Roo Code act like an in-editor agent team: read a real repository, edit multiple files, run terminal/package commands, invoke MCP/tools, or operate near `.env`, deployment, browser, or API-backed context.

Target evidence checked during this pulse: [`RooCodeInc/Roo-Code`](https://github.com/RooCodeInc/Roo-Code) was public on GitHub with 24,304 stars and updated at `2026-07-05T19:37:50Z`. Description observed: "Roo Code gives you a whole dev team of AI agents in your code editor."

## Why this buyer should care

Roo Code's value proposition is a whole agent team inside the editor. That makes the first risky handoff easy to miss: a mode change, auto-approval setting, MCP server, or terminal command can move from harmless code reading into repo mutation, package-script execution, credential-adjacent inspection, or deployment-impacting edits. A small team needs a visible receipt before granting broad agent-team scope.

## Five-minute free preflight

1. Run the free scanner before Roo Code receives broad edit, terminal, MCP, or auto-approval scope:

   ```bash
   python3 agent_preflight_lite.py --repo /path/to/repo --output-md agent-preflight-roo-code.md --output-json agent-preflight-roo-code.json
   ```

2. In the generated receipt, check for:
   - repo-level agent instructions such as `AGENTS.md`, `.roo/`, `.clinerules`, `.cursor/rules`, or Claude/Codex guidance files;
   - package-manager scripts, task runners, or workflow files that an editor agent can execute;
   - MCP/tool config, browser/API automation, deployment config, or `.env`-adjacent files;
   - generated decision level: **Green**, **Yellow**, or **Red**.
3. Paste the Markdown receipt into the task issue, PR, or team approval note before Roo Code gets write/terminal/tool scope.

## When to buy the $7 pack

Buy the paid pack if the scan is **Yellow/Red**, if Roo Code will run commands or use MCP/tools, if auto-approval is on, or if you need the copy-paste hooks, review templates, and remediation checklists that turn the one-off receipt into a repeatable agent-team safety gate: https://payhip.com/b/1nmxV

Skip it for now if the scan is **Green**, Roo Code has no terminal/MCP/API/deployment scope, and a one-off free receipt is enough.

## Copy-paste approval note

> I ran the Roo Code agent-team preflight before granting editor-agent write, terminal, MCP/tool, deployment, or credential-adjacent scope. Current decision: `<Green|Yellow|Red>`. If Yellow/Red, I will reduce scope, sandbox the session, or use the paid starter pack checklist before allowing auto-approval, package scripts, browser/API tools, or broad repo mutation.

Related free repo assets: [`/agent-preflight`](../../commands/agent-preflight.md), [review-comment template](../preflight-review-comment-template.md), and [trust/support notes](../trust-and-support.md).
