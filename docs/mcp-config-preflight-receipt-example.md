# MCP config preflight receipt example

Customer segment: small teams and maintainers adding or changing MCP servers for Claude Code, Cursor, or local agent harnesses before those agents get tool access.

Use this when a repo includes `.mcp.json`, Claude/Cursor MCP settings, agent instructions, package scripts, or workflow files and you need a short receipt before the agent starts reading tokens, calling tools, or running shell commands.

## 6-minute receipt

**Repo:** `example/mcp-enabled-internal-tools`

**Agent/run:** Claude Code with a new filesystem + GitHub MCP setup

**Command:**

```bash
python3 agent_preflight_lite.py . --json > agent-preflight-mcp.json
python3 agent_preflight_lite.py . > agent-preflight-mcp.md
```

**Decision:** Yellow — run only after a written MCP handoff.

**Buckets found:**

- MCP / Claude / Cursor config: `.mcp.json`, `.claude/settings.json`
- agent instructions: `CLAUDE.md`
- package scripts: `package.json` has `test`, `build`, and `deploy` scripts
- secret-adjacent files: `.env.example`, `.npmrc`
- workflow files: `.github/workflows/release.yml`

## Handoff before the MCP-backed agent starts

**May run without asking:**

- read `README.md`, `src/**`, `tests/**`, and `docs/**`
- run `npm test` after dependencies already exist
- run the free lite scanner again after edits

**Must ask first:**

- editing `.mcp.json`, `.claude/settings.json`, `.cursor/**`, or `CLAUDE.md`
- running `npm install`, `npm run build`, `npm run deploy`, or any command that talks to GitHub/npm/cloud APIs
- reading `.env*`, `.npmrc`, token files, or private config files
- adding a new MCP server or broadening filesystem/network permissions

**Must not do in this run:**

- print environment variables or credential-looking values
- run deploy/release/publish scripts
- use `docker.sock`, `chmod 777`, `rm -rf`, force-push, or curl-piped shell installers

## Buy/skip trigger for this segment

Skip the paid pack if the scan is Green and the MCP config is read-only, local-only, and already reviewed.

Buy the `$7` starter pack when the scan is Yellow/Red and you need the same MCP handoff repeatedly: report template, destructive-command hook, demo risky repo, buyer quickstart, and local verifier instead of rebuilding the receipt every agent run.

Payhip bundle: <https://payhip.com/b/1nmxV>

Free scanner/source: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>
