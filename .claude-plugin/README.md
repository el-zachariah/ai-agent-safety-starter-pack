# Agent Safety Preflight Claude Code plugin

A Claude Code-native `/agent-preflight` command package for teams that want a local repo-risk receipt before allowing Claude Code, Codex, Cursor, MCP, or other AI-agent workflows to edit a repository.

## What it does

- Prompts Claude to inspect the target repo before broad edits.
- Runs the free lite scanner from this repository when available.
- Produces a Markdown/JSON-style receipt with Green / Yellow / Red decision language.
- Keeps the marketplace/plugin surface free and non-spammy; paid upgrade links live only in the main project funnel, not in this plugin package.

## Installation from source

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
/plugin install ./.claude-plugin
```

## Command

- `/agent-preflight` — create a repo preflight receipt before AI-agent edits.

## Source of truth

Free repo and scanner: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>

## License

MIT
