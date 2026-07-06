# Preflight before Zed Agent Panel / editor-agent workflows

Buyer segment: teams using `zed-industries/zed`, Zed's Agent Panel / assistant-style editor workflows, or Zed-adjacent AI coding sessions before repo edits, shell commands, package scripts, MCP connectors, or secret-adjacent files enter scope.

Why this proof exists: Zed users already live inside a fast editor. The risky moment is not opening the editor; it is handing an AI helper enough repository context and command authority that a package script, generated patch, MCP config, or hidden `.env`-adjacent file can shape the run. This page gives a first buyer a concrete receipt they can copy before deciding whether the $7 starter pack saves setup time.

Target evidence checked during the deadline pulse:

- Public repo: https://github.com/zed-industries/zed
- Observed via GitHub API: non-archived, 86k+ stars, updated 2026-07-06.
- Fit: editor-native AI workflows are most likely to hit the exact pain this pack solves: fast repo context plus tool/run permissions without a written preflight receipt.

## 60-second Zed agent preflight receipt

Run the free scan before a Zed Agent Panel / editor-agent session gets write or command scope:

```bash
python3 agent_preflight_lite.py /path/to/repo
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-zed.json
```

Copy this into the issue, PR, or handoff note:

```text
Zed Agent Panel preflight receipt
Repo: <repo/path>
Scan decision: Green / Yellow / Red
Risk buckets: <agent instructions, package scripts, MCP/Cursor/Claude/Zed-adjacent config, workflows, secret-adjacent files, risky shell>
Allowed now: <read files, edit specific paths, run listed test command>
Must ask first: package installs, deploy/preview commands, credential/API/MCP changes, workflow edits, destructive shell, broad rewrites
Must not touch: .env, tokens, release/publish commands, production deploy settings, billing/payment/admin surfaces
Upgrade trigger: buy/use the reusable $7 workflow if this is Yellow/Red and the agent will run commands or edit a real repo.
```

## Buy / skip decision for this segment

- **Green:** zero or one low-risk signal, no package/deploy scripts, no secret-adjacent files, no agent/tool config. Use the free scan and normal review.
- **Yellow:** package scripts, workflow files, agent instructions, MCP/config files, or secret-adjacent filenames are present. Use the paid pack's report template and command hook so the Zed run has clear may-run / must-ask / must-not-touch rules.
- **Red:** destructive shell patterns, credential-adjacent files, deploy/publish commands, or multiple high-risk buckets appear. Do not start the editor-agent run until the reusable preflight receipt and guardrail hook are in place.

Paid workflow link for Yellow/Red runs: https://payhip.com/b/1nmxV

## Example handoff for a Zed session

1. Run the lite scan and attach the JSON/Markdown summary.
2. List exactly which files the agent may edit.
3. List one test command the agent may run without asking.
4. Put package installs, preview/deploy commands, MCP changes, and `.env` access under **Must ask first**.
5. If the scan is Yellow/Red, use the $7 bundle's full template and destructive-command hook before granting command scope.

This is intentionally narrow: it is not a security audit or sandbox. It is a trust receipt that makes the checkout feel tied to a real Zed/editor-agent workflow instead of a generic safety page.
