# Preflight before Google ADK agent workflows

<!-- deadline-google-adk-agents-proof:start -->

First-buyer proof for teams using Google Agent Development Kit / `google/adk-python` before handing repo files, tool calls, package scripts, deployment config, or `.env` scope to an agent run.

## Public target verified

- Repository: [google/adk-python](https://github.com/google/adk-python)
- Description: An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.
- Stars at verification: 20498
- Updated at verification: 2026-07-06T15:49:23Z
- Verification time: 2026-07-06T11:21:46-05:00

## Why this reduces checkout friction

A buyer using google/adk-python is not asking for a generic AI-safety checklist. They need a tiny receipt before a tool-enabled agent sees a real repo, because the risky part is usually the surrounding project: instructions, package scripts, MCP/tool config, deployment commands, and secret-adjacent files. This proof page shows exactly where the free preflight ends and when the paid $7 bundle saves setup time.

## 60-second receipt before widening agent scope

1. Run the free lite scan before the ADK-style agent receives repo or shell access.
   ```bash
   python3 agent_preflight_lite.py /path/to/adk-enabled-repo --json
   ```
2. Look specifically for `google-adk`, `adk`, agent tool callbacks, deployment YAML, package scripts, and secret-adjacent `.env`/credential files.
3. Paste this handoff note into the task ticket before the agent run:
   ```text
   Agent preflight done for google/adk-python workflow.
   Result: Green / Yellow / Red
   Allowed scope: <files/tools/commands>
   Must ask before: secrets, deploys, payment, destructive commands, or external account changes
   Next reviewer: <person or queue>
   ```
4. Keep the scan output with the first PR or issue so a maintainer can see the exact risk bucket before approving tool use.

## Green / Yellow / Red buy trigger

- **Green:** no agent instructions, no secret-adjacent files, no package/deploy scripts, and no tool config near the requested change. Use the free scanner and skip the paid pack.
- **Yellow:** one or two risk buckets appear, such as package scripts plus agent/tool config. Buy the $7 bundle if you want the reusable handoff template, repo preflight mini, and destructive-command hook instead of improvising the receipt.
- **Red:** secret-adjacent files, deployment commands, destructive shell patterns, or multiple automation configs are in scope. Buy the $7 bundle before handing the repo to the agent, then run the included hook/checklist before the first tool-enabled session.

Paid bundle: https://payhip.com/b/1nmxV

## Copy-paste buyer note

```text
I am using google/adk-python or a similar ADK-style agent workflow. I ran the free preflight first. If it is Yellow/Red, I am buying the $7 pack for the repeatable handoff receipt and destructive-command guard before the agent gets broader repo/tool scope.
```

<!-- deadline-google-adk-agents-proof:end -->
