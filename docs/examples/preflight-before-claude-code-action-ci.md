# Preflight before Claude Code GitHub Action CI runs

Customer segment: teams using issue/PR-triggered Claude Code automation in GitHub Actions.

Public target evidence checked for this proof:

- Repository: [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action)
- Stars at scout time: 8,248
- Last updated at scout time: `2026-07-05T10:36:59Z`
- Why it matters: a GitHub Action can run from pull requests, issue comments, labels, or workflow dispatch events while inheriting repository context, workflow permissions, and configured secrets. That is exactly the moment a cheap preflight receipt helps a maintainer decide what the agent may inspect or execute.

This page is not an Anthropic endorsement and does not claim a vulnerability. It is a buyer-fit proof for maintainers who want a small local receipt before enabling a coding-agent workflow in a real repository.

## 5-minute preflight receipt

Run this before the workflow gets broad repository write permissions, repository secrets, deploy credentials, or issue-comment triggers.

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/target-repo --json > agent-preflight-ci.json
python3 agent_preflight_lite.py /path/to/target-repo > agent-preflight-ci.md
```

Attach the Markdown receipt to the PR, issue, or workflow setup note.

## Example CI-agent receipt

```text
Decision: Yellow
Why: GitHub Actions workflow files and package scripts are present, and the planned Claude Code Action run can be triggered from PR or issue context.
Allowed now: read files, inspect tests, propose patches, run documented unit tests.
Ask first: changing workflow permissions, touching deploy scripts, modifying release automation, or reading secret-adjacent config.
Do not allow: automatic publish/deploy, permission widening, or credential-dependent commands until the receipt is reviewed.
```

## Buy/skip trigger

Skip the paid pack if the free scan is Green and the Claude Action only proposes code without shell commands or elevated workflow permissions.

Buy the `$7` pack if any of these are true:

1. the workflow uses `pull_request_target`, issue-comment triggers, labels, or broad write permissions;
2. the repo has package scripts, deployment workflows, MCP/Cursor/Claude configs, or secret-adjacent filenames;
3. a maintainer needs a repeatable report template before approving AI-agent PRs;
4. the team wants a local destructive-command hook and verifier instead of rebuilding guardrails from scratch.

Paid bundle link: <https://payhip.com/b/1nmxV>

## Pasteable maintainer note

```text
Before enabling the Claude Code GitHub Action on this repo, I ran the free agent preflight scan and attached the receipt. The scan decides what the agent may run, what needs human approval, and whether the $7 workflow bundle is worth using before the action receives broader repository permissions.
```
