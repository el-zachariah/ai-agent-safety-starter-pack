# Preflight before Goose-style local AI agents

Named customer segment: teams using [`aaif-goose/goose`](https://github.com/aaif-goose/goose) or similar local AI agents with MCP, extension, shell, browser, and repository-edit access.

Public target evidence captured 2026-07-05T09:40:21.330104-05:00:

- Repository: `aaif-goose/goose`
- Stars observed through GitHub API/search: `50671`
- Last updated: `2026-07-05T14:31:11Z`
- Description: an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

## Why this proof exists

A Goose-style local agent can move from "chat helper" to "hands on the repo" very quickly: it can read project files, run commands, use MCP/extensions, and touch local environment assumptions. That is exactly where a cheap preflight receipt helps a buyer decide whether to pause, share a receipt with a teammate, or buy the full checklist before granting wider scope.

## 30-second preflight receipt before giving the agent scope

Run the free scanner from the public repo before opening a real codebase to a local AI agent:

```bash
python3 scripts/repo_preflight_lite.py --path . --format markdown --output goose-preflight-receipt.md
python3 scripts/repo_preflight_lite.py --path . --format json --output goose-preflight-receipt.json
```

Attach the Markdown receipt to the PR/issue/session note before the agent edits files or runs shell commands.

## What a Goose/local-agent reviewer should look for

- MCP or extension config that can expose tools, browsers, repo contents, or credentials.
- Package scripts that can run network/install/build/test commands under agent control.
- `.env`, token, browser-profile, wallet, payment, deploy, or admin surface references.
- Hidden automation entry points such as `.goose/`, `.mcp.json`, `.cursor/`, `.continue/`, `.claude/`, workflow files, or custom agent hooks.
- A missing rollback/test command before autonomous edits begin.

## Buy / skip decision

Buy the $7 **AI Agent Safety Starter Pack** if the receipt is Yellow/Red, if a local agent will run shell/package scripts, or if MCP/extensions can reach anything private. Use the paid pack for the complete handoff checklist, reviewer prompts, and reusable receipt templates.

Skip it for now if the repo is a disposable toy repo, contains no secrets/config/tooling, and the agent is strictly read-only.

Product: <https://payhip.com/b/1nmxV>
