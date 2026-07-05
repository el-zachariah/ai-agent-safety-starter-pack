# Preflight before accepting agent/plugin marketplace PRs

Audience proof target: maintainers and small teams reviewing third-party Claude Code, Codex, Cursor, OpenCode, Gemini, or Copilot marketplace submissions before they recommend an agent, command, hook, skill, or plugin to downstream users.

Named segment examples this proof serves: `wshobson/agents`-style multi-harness marketplace maintainers, `numman-ali/n-skills` Agent Skills reviewers, and any curated Claude Code plugin list where a submitted command can inherit repo instructions, package scripts, MCP/tool config, or shell access after install.

This is not an endorsement claim from any marketplace. It is a concrete pre-merge review pattern for buyers/maintainers who need to decide whether a contributed agent package is safe enough to list or install.

## 5-minute marketplace PR review receipt

Run the free scanner against the submitted package or a local fixture repo that installs it:

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/submitted-agent-package-or-fixture
```

Paste a receipt like this into the PR checklist before merge:

```text
Marketplace PR preflight receipt
Package reviewed: <agent/plugin/skill/command name>
Target harnesses: Claude Code / Codex / Cursor / OpenCode / Gemini / Copilot
Scan result: Green / Yellow / Red
Findings:
- agent instructions: <present/absent + path>
- package scripts or install hooks: <present/absent + path>
- MCP/tool config: <present/absent + path>
- secret-adjacent files: <present/absent + path>
- risky shell patterns: <present/absent + path>
Decision:
- Green: list/install with normal review.
- Yellow: require maintainer handoff notes before listing.
- Red: block listing until commands, scripts, or tool scope are narrowed.
```

## Buy / skip trigger for this segment

- **Skip the paid pack for now** when the submitted package is Green, has no install hooks, no MCP/tool config, no secret-adjacent files, and no command that shells out into the user repo.
- **Buy the [$7 starter pack](https://payhip.com/b/1nmxV)** when a marketplace PR is Yellow/Red and you need a repeatable review template, destructive-command guardrail, demo risky repo, and verifier to reuse across future submissions instead of rebuilding the checklist for every PR.

## What this proof reduces

For a marketplace maintainer, the purchase anxiety is not "does the scanner run?" The anxiety is whether a small anonymous seller understands the actual review moment: a public PR adds an agent package, a curator must avoid endorsing risky automation, and downstream users may install it into real repos. This proof makes that moment explicit and gives the maintainer a free receipt before buying anything.
