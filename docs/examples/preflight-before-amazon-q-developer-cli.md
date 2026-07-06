# Preflight before Amazon Q Developer CLI agent sessions

Customer segment: teams using [`aws/amazon-q-developer-cli`](https://github.com/aws/amazon-q-developer-cli) or Amazon Q Developer CLI-style terminal AI coding sessions before an agent reads repo context, runs shell commands, changes package scripts, or works near AWS credentials.

Public evidence checked in this pulse: `aws/amazon-q-developer-cli` is live at https://github.com/aws/amazon-q-developer-cli; GitHub API reported 1,975 stars, updated `2026-07-06T02:20:32Z`, description `✨ Agentic chat experience in your terminal. Build applications using natural language.`, topics `agent, ai, amazon-q, cli, linux, llm, macos, mcp`.

## Why this is a buyer-fit proof

Amazon Q Developer CLI sits at the same decision point as the paid pack: a developer is about to let a terminal AI assistant inspect a local checkout, execute commands, and possibly touch cloud-adjacent config. A short preflight receipt makes the seller/product feel concrete before purchase because it shows exactly what to do before a Q CLI session enters a real repo.

The free scanner now treats `.amazonq/` as agent/workflow config, so an Amazon Q user can verify relevance locally before deciding whether the paid `$7` bundle saves setup time.

## 60-second Amazon Q handoff receipt

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-amazon-q.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-amazon-q.md
```

Paste this into the Amazon Q task notes before authorizing edits or shell commands:

```text
AMAZON_Q_DEVELOPER_CLI_PROOF
Repo preflight: agent-preflight-amazon-q.md
Decision: <Green / Yellow / Red>
Q may run: <tests, linters, read-only inspection>
Q must ask first: <package installs, deploys, AWS/account commands, workflow edits>
Q must not touch: <.env, AWS credentials, production deploy config, destructive shell>
Buy trigger: if the scan is Yellow or Red, use the paid $7 workflow bundle for the reusable handoff template, destructive-command hook, demo risky repo, and verifier before giving Q broader tool scope.
```

## What to review first

- `.amazonq/`, `AGENTS.md`, `CLAUDE.md`, `.cursor/`, `.continue/`, `.github/workflows/`, or other agent/workflow config.
- Package scripts, Makefiles, deploy scripts, `wrangler`, `terraform`, `cdk`, `sam`, `serverless`, or cloud-facing commands Q might run.
- Secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, AWS config/credential references, or token-bearing local files.
- Risky shell patterns such as `curl | sh`, `rm -rf`, `chmod 777`, Docker socket access, or force pushes.

## Buy / skip rule

Skip the paid pack for a Green toy repo with no agent config, no package/deploy scripts, and no secret-adjacent files. Buy the `$7` starter pack at https://payhip.com/b/1nmxV when the scan is Yellow/Red and the Q CLI session will edit files, run package/deploy/test commands, or work near AWS/cloud credentials. That is when the paid report template and destructive-command hook save setup time immediately.

## Trust signal for first buyers

This page is a customer-specific proof, not generic funnel copy: it names the exact Amazon Q Developer CLI workflow, points to public GitHub evidence, gives a pasteable receipt, and keeps the paid ask tied to a concrete Yellow/Red risk trigger.
