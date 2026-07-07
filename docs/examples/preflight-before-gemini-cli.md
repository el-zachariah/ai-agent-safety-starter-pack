# Preflight before Gemini CLI terminal agents

Customer segment: teams using Google Gemini CLI or similar terminal AI coding agents against a real repository checkout.

Target evidence captured 2026-07-05T08:12:52-05:00: [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli) is live, shows 105,755 GitHub stars, was last updated `2026-07-05T13:08:02Z`, and describes itself as: "An open-source AI agent that brings the power of Gemini directly into your terminal."

## Why this matters before checkout-start

Gemini CLI buyers already understand the value of a terminal-native coding agent, but the trust blocker is trust: before a tool edits files or runs shell commands, the buyer needs proof that the repo was checked locally and that the seller understands the exact risk surface.

This free proof page gives them a concrete receipt to run before a Gemini CLI task. If the receipt is Yellow or Red, the paid $7 pack is the immediate upgrade path because it adds the reusable command hook, review-comment template, agent handoff checklist, and packaged workflow instead of a one-off scan.

## Five-minute receipt

From the repository you are about to hand to Gemini CLI:

```bash
python3 tools/agent_preflight_lite.py . --json > agent-preflight-gemini-cli.json
python3 tools/agent_preflight_lite.py . > agent-preflight-gemini-cli.md
```

Attach the Markdown receipt to the first Gemini CLI task or paste this note before asking the agent to edit:

```text
Before changing files, read agent-preflight-gemini-cli.md.
If the decision is Green: proceed with the requested patch only.
If Yellow: summarize the risky package scripts, workflows, MCP/tool configs, or secret-adjacent files before editing.
If Red: stop and ask for human approval before running install/build/test commands or touching workflow/credential paths.
```

## Gemini CLI-specific checks

- Look at package scripts and task runners before allowing the CLI to run installs, builds, or tests.
- Check repo instructions, `.gemini`, `.cursor`, `.claude`, MCP config, and tool-wrapper files for hidden command policy changes.
- Keep generated receipts in the PR/issue thread so a maintainer can review the agent handoff without trusting chat memory.
- Re-run the receipt after dependency or workflow-file changes.

## Buy / skip trigger

- **Skip for now** when the receipt is Green and the task is a small read-only or docs-only change.
- **Buy the $7 pack** when the receipt is Yellow/Red, when Gemini CLI will run shell commands, or when the task touches package scripts, CI workflows, MCP/tool config, auth/secret paths, or repo-wide refactors.

Paid upgrade: <https://payhip.com/b/1nmxV>
