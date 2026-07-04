# Pre-agent run checklist

Use this before giving an AI coding agent tool access in an unfamiliar repository.

- [ ] Read `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, and similar instruction files.
- [ ] Review MCP / Claude / Cursor settings and confirm every server/tool is expected.
- [ ] Search for secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, `.netrc`, and private keys.
- [ ] Review `package.json` scripts, shell scripts, Makefiles, and CI workflows before running install/test/deploy commands.
- [ ] Look for destructive commands: `rm -rf`, force-push, disk formatting, `curl | sh`, `chmod 777`, Docker socket mounts.
- [ ] Decide which files/directories should be off-limits before the agent starts.
- [ ] Run the lite scanner:

```bash
python3 agent_preflight_lite.py /path/to/repo
```

The paid bundle adds a reusable report template, full preflight scanner, destructive-command hook, and verification scripts: https://payhip.com/b/1nmxV
