# smolagents tool-calling preflight proof

Target segment: teams using `huggingface/smolagents` (https://github.com/huggingface/smolagents) for terminal/agent-assisted development before repository edits, tool calls, package scripts, workflow files, or secret-adjacent paths enter an agent run.

Public target verification, captured 2026-07-06T063132--0500:

- Repository: `huggingface/smolagents`
- URL: https://github.com/huggingface/smolagents
- Archived: `false`
- Stars observed: `28211`
- Last updated: `2026-07-06T11:08:58Z`
- Public description: 🤗 smolagents: a barebones library for agents that think in code.

## Why this checkout-start proof exists

A generic repo-safety pitch is easy to ignore. This proof names the files and actions a smolagents tool agents user already understands: `tools.py`, `managed agents`, `API/tool credentials`. The free scanner gives a fast Green / Yellow / Red signal before a human hands a repo to an agent. The paid $7 starter pack is positioned only when that scan is Yellow or Red and the team wants the copy-paste command hook, PR receipt, and handoff template immediately.

## One-minute preflight for this segment

1. Run the free scanner from the public repo before starting a smolagents tool agents session.
2. Treat Yellow/Red as a stop-and-review signal for shell commands, package scripts, workflow edits, MCP/tool connectors, or secret-adjacent paths.
3. Paste the generated receipt into the PR, issue, or agent handoff so reviewers can see what was checked before the agent touched the repo.
4. If the scan is Yellow/Red and you need a ready-to-use command hook + review receipt now, buy the paid starter pack: https://payhip.com/b/1nmxV

## Buy / skip trigger

- **Buy the $7 pack** if the free scan is Yellow/Red, the agent will run commands or edit workflow/tooling files, and you need a copy-paste preflight hook plus a reviewer-facing receipt today.
- **Skip for now** if the free scan is Green, no commands or sensitive files are in scope, or you only need the open-source lite scanner.

## No-private-code assurance

This proof does not ask a buyer to upload private code. The scanner runs locally, the public repo shows the lite implementation, and the paid bundle adds operational templates rather than collecting repository contents.
