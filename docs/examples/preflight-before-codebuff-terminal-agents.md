# Preflight before Codebuff terminal coding-agent runs

Marker: `CODEBUFF_TERMINAL_AGENT_PROOF`

Target evidence checked 2026-07-06T02:10:23-0500: [`CodebuffAI/codebuff`](https://github.com/CodebuffAI/codebuff) is public/non-archived, observed stars `7114`, updated `2026-07-06T06:26:04Z`. Description: Generate code from the terminal!.

## Who this is for

Teams trying Codebuff-style terminal coding agents before the assistant receives real repo files, edit scope, shell/package-manager commands, workflow files, or secret-adjacent environment/config paths.

## Why this proof can start a checkout

Codebuff buyers already understand terminal-native code generation. The checkout friction is trust: before paying for a generic-looking preflight bundle, they need to see a receipt that names their exact run surface and tells them when the paid bundle is worth it.

This free page gives a 60-second receipt to paste into the first Codebuff task. The paid `$7` pack is the upgrade only when that receipt is Yellow/Red and the team needs repeatable report templates, destructive-command hooks, and verifier scripts instead of an improvised note.

## 60-second free preflight

From the repository that Codebuff will inspect or edit:

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-codebuff.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-codebuff.md
```

Paste this into the Codebuff task before broad edits or command execution:

```text
Codebuff terminal-agent preflight receipt
- Repo/workspace checked:
- Task delegated to Codebuff:
- Scan level: GREEN / YELLOW / RED
- Agent instruction files reviewed:
- Package/install/test/deploy commands allowed:
- Workflow/CI files in scope:
- Secret-adjacent files excluded:
- Must ask before:
```

## Codebuff-specific checks

Review these before the first command-running task:

1. `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, `.github/copilot-instructions.md`, and other repo-level instructions that can steer an AI coding agent.
2. `package.json`, `pyproject.toml`, `Makefile`, shell scripts, and workflow files that Codebuff or a teammate may run during the patch.
3. `.env`, `.npmrc`, cloud/deploy config, API client settings, and credential-adjacent paths that should stay out of the prompt or command scope.
4. Any destructive command pattern in the planned task: force-push, deploy, migration, delete, `curl | sh`, privileged Docker, or credential-printing commands.

## Buy / skip trigger

`YELLOW_RED_BUY_TRIGGER_CODEBUFF`: buy the `$7` starter pack only when the free scan is Yellow/Red and Codebuff will edit real code, run package scripts, touch CI/workflow config, or operate near credentials. The paid bundle adds reusable report templates, destructive-command hook examples, demo risky repo, buyer quickstart, and verification scripts so the receipt becomes a repeatable team gate.

Payhip bundle: https://payhip.com/b/1nmxV

Skip the paid pack for now when the scan is Green, the task is read-only, or the repo has no agent instructions, package scripts, workflow files, risky shell, or secret-adjacent paths.

This is an independent preflight example for Codebuff-style workflows; it is not affiliated with or endorsed by CodebuffAI.
