# Skills-curated marketplace reviewer preflight proof

Public target evidence: `trailofbits/skills-curated` describes itself as a "Curated, community-vetted Claude Code plugin marketplace" and the GitHub API showed 456 stars on 2026-07-05. This page is not an endorsement or affiliation; it is a concrete proof for teams reviewing high-trust Claude Code skills/plugins before install.

## Buyer segment

Claude Code plugin/skill marketplace reviewers and small teams installing third-party `.claude-plugin/`, `.claude/commands/`, hooks, MCP settings, or package scripts into a real repo.

## What changed for this segment

The free scanner now treats files under `.claude-plugin/` as agent/workflow configuration, so a marketplace candidate that ships plugin metadata, commands, or hooks produces a pre-install receipt instead of looking like an ordinary JSON folder.

## 60-second pre-install receipt

```bash
git clone <candidate-plugin-or-skill-repo> /tmp/plugin-candidate
python3 agent_preflight_lite.py /tmp/plugin-candidate --json
```

Keep the output with the marketplace review. Use the result as the buy/skip trigger:

- **Green:** keep the free receipt and continue normal code review.
- **Yellow/Red:** buy the $7 starter pack for the reusable handoff template, destructive-command hook, demo risky repo, and buyer quickstart: https://payhip.com/b/1nmxV

## Why this reduces checkout friction

A first buyer can see the seller has a real, public, segment-specific workflow for a named Claude Code marketplace use case, not just a generic download page. The paid product is positioned only when the free scan finds enough risk to justify a repeatable process.
