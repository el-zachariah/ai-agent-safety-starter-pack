# Preflight review comment template

Use this when you are about to hand a pull request, issue, or repo cleanup task to Claude Code, Codex, Cursor, or another tool-enabled AI coding agent.

The goal is not to slow the agent down. The goal is to leave a short, visible receipt of what the agent may run, what it must ask about, and when the `$7` starter pack saves you from rebuilding the same guardrails again.

## 1. Run the free scan

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight.txt
```

## 2. Paste this review comment

```markdown
### AI-agent repo preflight

I ran the free AI Agent Safety lite preflight before giving an agent tool access.

**Decision:** Green / Yellow / Red

**Risk buckets found:**
- Agent instructions: yes/no — `<files>`
- MCP/Cursor/Claude config: yes/no — `<files>`
- Package scripts/workflows: yes/no — `<files>`
- Secret-adjacent files: yes/no — `<files>`
- Risky shell patterns: yes/no — `<files>`

**Agent may run:**
- `<safe read/test/build commands>`

**Agent must ask before:**
- `<install/deploy/write/delete/secret-adjacent actions>`

**Agent must not touch:**
- `<secrets, production config, generated artifacts, deployment files>`

**Upgrade trigger:** if this is Yellow/Red or I expect to repeat this workflow, use the full starter pack for the reusable report template, destructive-command hook, demo risky repo, and verifier: https://payhip.com/b/1nmxV
```

## 3. Fast buy/skip rule

- **Green:** keep the comment and use normal review discipline.
- **Yellow:** write the run / ask / avoid rules before the agent gets shell access.
- **Red:** use a repeatable preflight workflow and a destructive-command hook before the agent can run commands.

If you are doing this once, the free scanner and comment are probably enough. If you are doing it repeatedly or inside a repo with real install/deploy scripts, the paid `$7` pack exists to save setup time.
