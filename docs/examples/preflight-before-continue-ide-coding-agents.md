# Preflight before Continue IDE coding-agent workflows

Marker: `CONTINUE_IDE_CODING_AGENT_PROOF`

Verified public target: [continuedev/continue](https://github.com/continuedev/continue) — 34726 GitHub stars, updated `2026-07-07T09:08:43Z`. open-source coding agent

## Why this named buyer should care

Continue users let an IDE agent inspect a repository, propose code edits, call tools, run shell commands, and sometimes connect MCP/context providers before a maintainer reviews the diff.

The free scanner in this repo gives the buyer a concrete go/no-go receipt before the agent run becomes a risky PR. That makes the paid `$7` pack a practical upgrade only when the result is not obviously Green.

## Copy-paste preflight for Continue IDE coding-agent workflow teams

1. Run the free lite scan before accepting the generated diff:

   ```bash
   python3 tools/repo_preflight_lite.py --repo . --format markdown --output preflight-receipt.md
   ```

2. Attach `preflight-receipt.md` to the PR or internal handoff before the agent changes workflow files, package scripts, tool config, MCP/context config, secret-adjacent paths, generated tests, or CI.
3. Use the decision rule:
   - **Green:** skip the paid pack for now; keep the free receipt.
   - **Yellow/Red:** buy the `$7` pack at <https://payhip.com/b/1nmxV> for the expanded checklist, command hook, review comment template, and handoff prompts.

## Yellow/Red trigger for this segment

Yellow/Red if Continue will touch workflow files, package scripts, MCP config, secrets-adjacent paths, or generated CI before the team has a reproducible receipt.

This is a seller-trust proof, not a generic ad: the target repo is public and current, the free scanner is inspectable, and the paid trigger is bounded to a visible Yellow/Red risk receipt.
