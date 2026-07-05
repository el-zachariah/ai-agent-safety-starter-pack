# Continuous-agent preflight example

This example is for developers running a **persistent Claude Code / MCP / agent harness** where the agent keeps state across sessions, uses hooks, and may execute repo commands after a handoff.

It is intentionally concrete because the first-dollar buyer is not a generic developer. The likely buyer is someone about to let an always-on or multi-session agent work inside a real repo and wanting a visible receipt before tool access.

## Named segment

- You use Claude Code, Codex, Cursor, MCP tools, or a continuous-agent wrapper.
- Your repo has `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `.cursor/rules/*`, MCP config, package scripts, GitHub Actions, or shell automation.
- The agent may run install/test/build/deploy commands, touch workflow files, or carry context between sessions.

## 7-minute preflight receipt

Run this before the first tool-enabled agent session:

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/your/continuous-agent-repo
```

Paste the result into the agent task or PR/issue handoff:

```markdown
## Agent preflight receipt

Repo: <repo or local path>
Decision: Green / Yellow / Red
Risk buckets: <instruction files, MCP/Claude/Cursor config, package scripts, workflows, secret-adjacent files, risky shell>

Agent may run:
- <safe read-only checks>
- <specific test command if pre-approved>

Agent must ask before:
- changing workflow/deploy scripts
- editing agent instruction files
- running install scripts or shell pipelines
- touching secret-adjacent files

Agent must not:
- run destructive commands
- push/force-push/release/deploy
- modify credentials or payment/KYC settings
```

## Buy/skip trigger for this segment

Skip the paid pack if the scan is Green and the agent will only read files or run one known-safe test command.

Buy the `$7` starter pack when the scan is Yellow/Red and you need the reusable workflow instead of a one-off note:

- a fuller repo preflight mini for handoff decisions,
- destructive-command hook examples,
- report templates,
- a buyer quickstart,
- demo risky repo/report,
- verification scripts.

Paid bundle: <https://payhip.com/b/1nmxV>

## Why this matters for continuous agents

A one-shot agent mistake is bad. A persistent agent mistake can be repeated across sessions. This preflight step creates a small, reviewable checkpoint before the harness inherits repo context, command access, and long-running state.

This is not a security audit or sandbox. It is a practical first-pass receipt that helps a human decide what the agent may read, run, avoid, or ask about before work begins.
