# Preflight before Agent2Agent protocol workflow runs

Marker: `A2A_AGENT_PROTOCOL_WORKFLOW_PROOF`

Verified public target: [`a2aproject/A2A`](https://github.com/a2aproject/A2A)
- Stars observed during this deadline pulse: `24645`
- Updated at: `2026-07-06T11:44:04Z`
- Description: Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications.

## Who this is for

This proof is for teams using Agent2Agent protocol services before connecting repo-backed tools before an AI coding assistant receives agent-to-agent connectors, package scripts, API tools, workflow files, and secret-adjacent config.

The trust problem for a first buyer is simple: a cold checkout page does not prove the seller understands their exact workflow. This page gives that buyer a copy-paste receipt they can run with the free scanner first, then buy the `https://payhip.com/b/1nmxV` bundle only when the result is Yellow or Red.

## 60-second preflight receipt

Copy this into the issue, PR, task brief, or agent handoff before the agent is allowed to act:

```text
A2A_AGENT_PROTOCOL_WORKFLOW_PROOF
Target workflow: Agent2Agent protocol / AI coding-agent session
Repo under review: <repo path or URL>
Agent scope requested: <read/edit/test/shell/MCP/API/deploy scope>
Free preflight command run: python3 agent_preflight_lite.py <repo>
Decision: Green / Yellow / Red
Allowed without approval: <read-only / tests / specific commands>
Must ask first: package installs, deploys, credential access, destructive commands, workflow edits
Paid-pack trigger: buy only if this receipt is Yellow/Red and the team needs the reusable handoff template + destructive-command hook + verifier.
```

## Green / Yellow / Red buy trigger

- **Green:** no agent instruction files, no risky package/deploy scripts, no workflow edits, and no secret-adjacent files. Use the free scanner and skip the paid bundle for now.
- **Yellow:** one or more agent config/instruction files, package scripts, MCP/tool settings, workflow files, or secret-adjacent paths need a scoped handoff. Buy the `$7` pack if the team wants the reusable report template and guardrail hook instead of writing a one-off checklist.
- **Red:** destructive shell patterns, credential-adjacent files, deploy automation, or broad shell/API scope would enter the run. Buy the `$7` pack before allowing the agent to execute commands.

## Why this makes the product real for Agent2Agent protocol users

Agent2Agent protocol buyers already understand the value of fast AI-assisted coding. The missing step is a tiny operational receipt before the assistant inherits repo authority. The free scanner produces the initial signal; the paid pack turns Yellow/Red findings into a repeatable local workflow with a report template, buyer quickstart, destructive-command hook, demo risky repo, and verifier.

Payhip bundle: https://payhip.com/b/1nmxV
