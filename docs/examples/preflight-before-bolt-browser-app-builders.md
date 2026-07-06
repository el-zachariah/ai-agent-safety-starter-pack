# Preflight before Bolt-style browser app builders

Customer segment: teams using `stackblitz-labs/bolt.diy`, Bolt.new-style browser AI app builders, or hosted coding workspaces that can edit project files, install packages, run dev servers, and touch deployment settings.

Target evidence checked: [`stackblitz-labs/bolt.diy`](https://github.com/stackblitz-labs/bolt.diy) is public/non-archived at pulse time, with 19,548 GitHub stars, updated `2026-07-05T18:45:13Z`, and description: "Prompt, run, edit, and deploy full-stack web applications using any LLM you want!".

Why this matters: browser app builders feel safer than a local terminal because the UI is friendly, but the generated project still has `package.json` scripts, framework config, environment variables, API keys, deploy hooks, and preview commands. A repo preflight receipt makes the buyer's risk concrete before the agent starts running installs/builds against a real app.

## 60-second preflight receipt

1. Freeze the target app branch or workspace snapshot before the browser agent edits or runs commands.
2. Run the free scanner:

   ```bash
   python3 agent_preflight_lite.py /path/to/generated-or-imported-app --json
   ```

3. Review these Bolt-style risk buckets before tool execution:
   - `package.json` install/build/dev scripts the agent may run automatically,
   - `.env`, `.env.local`, deployment tokens, or secret-adjacent files,
   - `vite.config.*`, `next.config.*`, `wrangler.toml`, Docker/dev-container config, or preview/deploy scripts,
   - MCP/Cursor/Claude/Copilot instruction files if the app is later handed to a local coding agent,
   - shell snippets copied from generated docs or package postinstall hooks.
4. Write a Green / Yellow / Red handoff:
   - **Green:** no secrets, no deploy scripts, one low-risk package script bucket.
   - **Yellow:** package scripts plus framework/deploy config or secret-adjacent files.
   - **Red:** secrets plus destructive shell, deploy credentials, or broad package hooks.

## Buy trigger for this segment

Use the free scanner when the generated app is Green. Buy the `https://payhip.com/b/1nmxV` starter pack when the scan is Yellow/Red and the browser agent is about to run install/build/deploy commands, because the paid bundle adds the reusable report template, destructive-command hook, demo risky repo, and verification scripts instead of forcing the team to rebuild the guardrail during the session.

## Copy-paste handoff note

```text
Bolt-style app-builder preflight: Yellow.
Allowed now: read generated files, propose diffs, run read-only checks.
Must ask first: npm/pnpm install, dev server, deploy/preview, commands that read .env or write outside the app directory.
Must not touch: .env*, deployment tokens, production project settings, billing/admin surfaces.
Upgrade trigger: buy/use the $7 starter pack before repeated agent runs or any Red finding.
```
