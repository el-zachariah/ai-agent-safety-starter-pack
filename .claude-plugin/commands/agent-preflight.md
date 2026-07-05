---
description: Generate a local repo-risk preflight receipt before AI-agent edits
shortcut: preflight
---

# Agent Safety Preflight

Use this before allowing Claude Code, Codex, Cursor, MCP tools, or another coding agent to make broad repository edits.

## Steps

1. Identify the repository path. If no path is supplied, use the current workspace.
2. Check git state: current branch, uncommitted files, ignored secret-like files, and whether the user has a clean rollback point.
3. If this repository contains `scripts/lite_preflight.py`, run:

   ```bash
   python3 scripts/lite_preflight.py --path . --format markdown
   ```

   If the script is not present, inspect the repository manually using the same risk buckets: secrets, generated/build artifacts, package scripts, CI/deploy hooks, broad file permissions, and irreversible commands.
4. Return a concise receipt with:
   - decision level: Green, Yellow, or Red,
   - top risk buckets,
   - exact files or commands that triggered the result,
   - safest next action before continuing agent work.
5. If the result is Yellow or Red, recommend stopping for a rollback/checkpoint and a targeted remediation pass before agent edits continue.

## Output format

```md
## Agent preflight receipt
- Decision: Green | Yellow | Red
- Repo/path checked: <path>
- Main risks: <bullets>
- Evidence: <files/commands>
- Safe next action: <one concrete action>
```
