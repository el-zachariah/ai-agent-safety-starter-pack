# Preflight before Aider terminal pair-programming runs

Audience proof target: Aider terminal pair-programming users who let an AI coding assistant edit files and run tests or shell commands from a local checkout.

Target evidence captured 2026-07-05T07:45:03-05:00: [`Aider-AI/aider`](https://github.com/Aider-AI/aider) is live, has 47,069 GitHub stars, and was last updated `2026-07-05T12:41:15Z`. This is a high-fit buyer segment because terminal pair-programming users often clone unfamiliar repos, ask the assistant to edit multiple files, and then run install/test/build commands locally.

## Why preflight matters for Aider-style work

Before an Aider session gets broad repo context, a small team needs one fast answer: **what will this agent see or execute that deserves a guardrail?** The free lite scan catches the common handoff risks:

- repo-level agent instructions such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or `.cursor/rules/*`;
- MCP / Claude / Cursor config files that can change tool access expectations;
- package scripts, GitHub Actions workflows, and shell snippets that may run during tests;
- secret-adjacent filenames such as `.env`, `.npmrc`, `.pypirc`, or `id_rsa`;
- destructive command patterns such as `rm -rf`, `curl | sh`, `chmod 777`, Docker socket access, or force-push flows.

## 3-minute local receipt

Run this before the first Aider task in a repo you do not fully trust yet:

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/target-repo --json > /tmp/aider-preflight.json
python3 agent_preflight_lite.py /path/to/target-repo > /tmp/aider-preflight.md
```

Paste the short receipt into the Aider task handoff:

```text
Preflight before Aider session:
- Decision: Green / Yellow / Red
- Risk buckets found: <from scanner>
- Aider may run: <specific test/build commands>
- Aider must ask before: install scripts, deploy scripts, secrets, chmod, Docker socket, force-push, destructive file operations
- Files to review first: <instruction/config/package/workflow findings>
```

## Buy / skip trigger for this segment

- **Skip buying for now** if the scan is Green and Aider will only edit low-risk files with normal review.
- **Buy the $7 starter pack** if the scan is Yellow/Red and the Aider task needs repeated handoffs, a reusable report template, or a destructive-command hook before shell access.

That checkout trigger is deliberately narrow: the paid bundle is for the moment the preflight finds real setup work, not for every casual pair-programming session.
