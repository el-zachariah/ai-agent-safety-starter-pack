# Preflight before CAMEL-AI multi-agent workflows

Marker: `CAMEL_AI_MULTI_AGENT_PROOF`

Public target verified for this buyer proof:

- Repository: [`camel-ai/camel`](https://github.com/camel-ai/camel)
- GitHub stars when verified: `17330`
- Last updated when verified: `2026-07-06T12:44:20Z`
- Why it fits: teams evaluating CAMEL-AI are already close to the moment where autonomous or semi-autonomous agents receive tool, repo, package-script, API, or environment context. That is the exact moment the free scan should create a handoff receipt and the paid pack should save setup time when the result is Yellow/Red.

## Who this is for

Use this receipt before a CAMEL-AI or similar multi-agent run touches multi-agent role/task prompts, tool/API connectors, package scripts, generated repo edits, shell commands, and .env-adjacent values.

This is not a security audit of `camel-ai/camel`. It is a small pre-tool-access workflow for the team about to run agents in its own repo.

## 60-second receipt

Run the free scanner first:

```bash
python3 agent_preflight_lite.py /path/to/your/repo --json
python3 agent_preflight_lite.py /path/to/your/repo > agent-preflight-camel-ai-multi-agent-proof.md
```

Paste the short decision into the task handoff:

```text
CAMEL_AI_MULTI_AGENT_PROOF
Target agent workflow: CAMEL-AI multi-agent workflows
Repo scanned: <repo/path or commit>
Decision: Green / Yellow / Red
Risk buckets present: <agent instructions / package scripts / workflow files / secret-adjacent files / risky shell>
Allowed before agent run: <read-only / tests only / no shell / no secrets / specific commands>
Must ask first: <deploy, destructive commands, credential use, external network calls>
Reviewer: <person/team>
```

## Buy / skip trigger for the $7 pack

- **Green:** keep the free scanner output with the run notes. Do not buy just because the target repo is popular.
- **Yellow:** buy the `https://payhip.com/b/1nmxV` pack if the scan shows two or more buckets, package scripts, MCP/agent config, workflow files, or secret-adjacent paths and you need a reusable handoff template.
- **Red:** buy the pack before the agent run if destructive shell, credential-adjacent files, deploy scripts, or broad tool/API access are in scope; use the included destructive-command hook and report template before granting shell access.

## What the paid pack saves

The paid pack gives the repeatable report template, destructive-command hook, risky demo repo, buyer quickstart, and verifier so a CAMEL-AI team does not rebuild the handoff and guardrail after the scan already found Yellow/Red risk.
