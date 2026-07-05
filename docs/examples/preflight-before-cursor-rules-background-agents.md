# Preflight before Cursor rules / background agents

Customer segment: teams using **Cursor** with `.cursorrules`, `.cursor/rules/*`, background agents, or repository rules that shape how an AI coding assistant edits and runs commands in a real checkout.

Public fit evidence captured 2026-07-05: [`cursor/cursor`](https://github.com/cursor/cursor) was public/non-archived with 33,008 GitHub stars and updated `2026-07-05T18:51:31Z`; [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) was public/non-archived with 40,226 GitHub stars and updated `2026-07-05T18:07:11Z`. That is a live buyer segment already curating Cursor rule files and agent-editing workflows.

## 60-second Cursor preflight receipt

Run the free scanner before a Cursor agent or rules-driven assistant gets broad edit/test scope:

```bash
python3 agent_preflight_lite.py /path/to/repo --json
```

Write this short note into the task, PR, or handoff doc:

```text
agent-preflight-cursor-rules
Repo: <repo/path>
Decision: Green / Yellow / Red
Cursor inputs reviewed: .cursorrules, .cursor/rules/*, Cursor project settings, MCP/tool configs
Package/workflow scripts reviewed: <yes/no + paths>
Allowed now: <safe read/edit/test commands>
Must ask first: install/deploy/migration/secret/network/broad shell actions
Do not expose: .env, tokens, private keys, production data, unreviewed MCP servers
```

## What the free scan should catch

- `.cursorrules`, `.cursor/rules/*`, and related agent instruction files;
- `.mcp.json`, Claude/Cursor/MCP tool config that can widen file, shell, or API scope;
- package scripts, workflows, and risky shell patterns the assistant may try to run;
- secret-adjacent files that should be excluded before a background agent reads context.

## Buy / skip trigger

- **Skip the paid pack for now** if the scan is Green and Cursor is only making a small supervised edit.
- **Buy the [$7 AI Agent Safety Starter Pack](https://payhip.com/b/1nmxV)** if the scan is Yellow/Red, the repo has multiple Cursor rule sources, package scripts, MCP/tool configs, or the background agent will run install/test/build commands without a human watching every step.

The paid bundle gives you the reusable repo preflight mini, destructive-command hook, report template, and verifier so every Cursor task gets the same handoff instead of a one-off note.
