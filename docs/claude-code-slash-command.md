# Claude Code slash-command bridge

Use this when you want Claude Code to run the free repo preflight before it gets tool access in an unfamiliar or high-change repository.

## Copy into a project

From a checkout of this repository:

```bash
mkdir -p /path/to/target-repo/.claude/commands
cp commands/agent-preflight.md /path/to/target-repo/.claude/commands/agent-preflight.md
```

Then open Claude Code in the target repo and run:

```text
/agent-preflight .
```

The command tells the agent to run `agent_preflight_lite.py`, turn findings into a Green / Yellow / Red decision, and write the short run/ask/avoid handoff before shell commands begin.

## What the free command does

- Confirms the repo path before scanning.
- Runs the lite scanner in JSON mode when available.
- Flags agent instructions, MCP/Cursor/Claude config, package scripts, workflow files, risky shell patterns, and secret-adjacent filenames.
- Produces a compact handoff note: safe first commands, must-ask commands, and files the agent should avoid.

## When the paid pack saves time

Stay with the free command when the scan is Green. Buy the `$7` starter pack when the scan is Yellow/Red and the agent will run commands in a real repo. The paid bundle adds the reusable report template, destructive-command hook, demo risky repo, buyer quickstart, and verifier so the handoff is repeatable instead of a one-off note.

Payhip: https://payhip.com/b/1nmxV
