# Copy-paste AI agent task prompt

Use this after running the free lite scan and before giving Claude Code, Codex, Cursor, or another coding agent shell access inside a repo.

It is intentionally short: paste it into the agent task, then replace the bracketed fields.

## 1. Run the free scan first

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-lite.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-lite.md
```

## 2. Paste this task prompt

```text
You are working in [REPO NAME]. Before making code changes, read the repo safety note below.

Repo safety note from ai-agent-safety-starter-pack lite scan:
[PASTE THE SHORT SCAN SUMMARY OR LINK TO agent-preflight-lite.md]

Allowed now:
- Read source, tests, docs, and config files needed for the task.
- Propose commands before running install, migration, deploy, Docker, or destructive filesystem commands.
- Prefer minimal diffs and explain any file that changes execution, secrets handling, CI, or deployment.

Do not run without explicit confirmation:
- rm/rmdir/delete commands outside build artifacts or temp files
- curl|sh / wget|sh installers
- chmod 777, force pushes, deploys, migrations, production commands, or Docker socket access
- commands that read or print secrets from .env, npm/pip tokens, cloud credentials, SSH keys, or local keychains

Task:
[PASTE THE ACTUAL CODING TASK]

Before executing shell commands, summarize:
1. which repo instruction/config files may affect your behavior,
2. which risky files/scripts you noticed,
3. which commands you want to run and why,
4. what you will avoid unless I approve.
```

## 3. When the paid pack is worth it

The free prompt is enough for a one-off lightweight check. Buy the $7 starter pack when you want the reusable full repo preflight mini, destructive-command hook examples, buyer quickstart, report templates, demo risky repo/report, verifier scripts, and limitations FAQ.

Paid bundle: https://payhip.com/b/1nmxV
