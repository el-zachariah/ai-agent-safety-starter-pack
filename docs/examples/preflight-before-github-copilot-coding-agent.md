# Preflight before GitHub Copilot coding agent tasks

Named buyer segment: teams using GitHub Copilot coding agent, repository custom instructions, issue/PR automation, or workflow-backed developer tasks before a coding agent receives repo context and command scope.

Why this is a checkout-start proof: a Copilot coding-agent task often begins from an issue or PR, but the risk still lives in the repo: `.github/copilot-instructions.md`, workflow files, package scripts, secret-adjacent config, and install/test commands. The free scanner now flags `copilot-instructions.md` so a buyer can see the handoff trigger before paying for the reusable template and destructive-command hook.

## 60-second receipt

```bash
python3 agent_preflight_lite.py /path/to/repo --json > copilot-agent-preflight.json
python3 agent_preflight_lite.py /path/to/repo > copilot-agent-preflight.md
```

Keep this note with the issue/PR before assigning the coding-agent task:

```text
Copilot coding agent preflight
Decision: <GREEN|YELLOW|RED>
Found: <agent instructions / workflows / package scripts / secret-adjacent files / risky shell>
May run: <exact test/build commands>
Must ask before: dependency installs, migrations, deploys, secret/config edits, workflow permission changes, destructive shell
Must not touch: .env*, token files, production deploy config, billing/admin surfaces
Buy trigger: Yellow/Red + real repo command scope → use the $7 starter pack template and hook instead of rebuilding the handoff manually.
```

## What to inspect before assignment

- `.github/copilot-instructions.md` or other repository instructions that shape the agent's behavior.
- `.github/workflows/*` permissions, secrets, write tokens, deployment jobs, and pull-request triggers.
- `package.json`, `pyproject.toml`, `Makefile`, shell scripts, and install/test commands the agent may run.
- `.env*`, `.npmrc`, `.pypirc`, cloud config, or other secret-adjacent files that should stay outside agent context.

## Green / Yellow / Red decision

- **Green:** no agent instructions, no workflow/package-script risk, no secret-adjacent files. Assign the task with normal review.
- **Yellow:** Copilot instructions or workflows exist, but no obvious destructive command. Paste the receipt into the issue and constrain commands.
- **Red:** workflows/secrets/package scripts plus risky shell or production deployment scope. Stop, use the full preflight template, and add the destructive-command hook before assigning the task.

## Why the paid pack helps

The free scanner tells you whether the task is Green, Yellow, or Red. The $7 pack saves the repeated setup when the result is Yellow/Red: reusable report template, local command guardrail, demo risky repo, and verification steps you can attach before a Copilot coding-agent task starts.

Paid bundle: <https://payhip.com/b/1nmxV>
