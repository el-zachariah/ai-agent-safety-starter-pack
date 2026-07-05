# Preflight before VS Code agent extensions (Cline / Roo Code-style)

Customer segment: teams using **Cline**, **Roo Code**, or similar VS Code agent extensions that can read workspace context, edit files, run terminal commands, call MCP tools, and keep conversational state inside the editor.

Target evidence captured in this deadline pulse:

- Repository: [cline/cline](https://github.com/cline/cline)
- Public description: Autonomous coding agent as an SDK, IDE extension, or CLI assistant.
- Stars observed: 64298
- Last updated observed: 2026-07-05T11:17:41Z
- Adjacent repository checked: [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) — 24304 stars, updated 2026-07-05T08:55:30Z

## Why this segment should care before buying

VS Code agent extensions are attractive because they sit where the developer already works: editor tabs, terminal, MCP/tool settings, task history, and repo files are all nearby. That convenience also makes a cheap preflight receipt useful before the extension is allowed to run install/test/build commands or act on an unfamiliar workspace.

The free scanner gives a public preview: instruction files, MCP/Cursor/Claude configs, package scripts, workflow files, risky shell patterns, and secret-adjacent filenames. The paid **AI Agent Safety Starter Pack** is the $7 upgrade when the scan is Yellow/Red and the buyer wants a reusable handoff template plus destructive-command guardrail instead of rewriting rules for every agent session.

## 5-minute workflow before letting an editor agent run commands

1. Run the lite scanner from a normal terminal before starting the agent extension task.
2. Paste the Green / Yellow / Red receipt into the agent chat as the first message.
3. Mark which files the extension may edit, which scripts it may run, and which MCP/tool configs require a human pause.
4. Ask the agent to restate the allowed command list before it opens a terminal.
5. If the scanner returns **Yellow** or **Red**, buy the $7 pack before continuing with broad write or shell scope.

## Copy-paste guardrail for a Cline/Roo Code task

```markdown
Before editing this workspace, obey this preflight receipt.

- Do not run package manager install/build/test commands until you list the exact command and why it is safe.
- Do not read, print, transform, or summarize secret-adjacent files flagged by the scan.
- Treat MCP, Cursor, Claude, and editor-agent config files as scope-setting files; ask before changing them.
- Keep a final "Preflight receipt" note with the decision level, risky buckets, commands run, and commands skipped.

If the receipt is Yellow or Red, stop after preparing the safe command plan unless the repo owner approves the paid handoff checklist.
```

## Example receipt snippet

```markdown
Preflight receipt for VS Code agent extension run

Decision: YELLOW — continue only with constrained terminal access.
Risk buckets:
- .vscode/tasks.json can launch repo scripts
- MCP/tool config present
- package scripts include install/build hooks

Allowed now:
- inspect source files and tests
- propose edits without running install scripts
- run one documented test command after approval

Pause before:
- modifying editor-agent or MCP config
- running network/install/deploy commands
- touching secret-adjacent files or generated credentials
```

Paid upgrade trigger: buy the $7 pack at <https://payhip.com/b/1nmxV> when the editor agent needs repeatable run/ask/avoid rules, a report template, and a destructive-command hook before it continues with terminal access.
