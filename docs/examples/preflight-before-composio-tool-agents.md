# Preflight before Composio tool-integration agents

Buyer segment: teams using [`ComposioHQ/composio`](https://github.com/ComposioHQ/composio) or a similar agent tool-integration layer before granting agents access to GitHub, browser, SaaS, MCP, sandbox, or authentication-backed tools.

Public target evidence captured for this pulse: `ComposioHQ/composio` is live/non-archived, observed at 29,104 stars, updated `2026-07-05T20:56:43Z`, and describes itself as powering `1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench` for AI agents.

## Why this buyer should care

A Composio-style agent stack can turn a vague instruction into real external actions. Before that stack receives repo context, local package scripts, `.env` values, API credentials, or a tool session, keep a small preflight receipt in the task so the buyer can distinguish a safe Green run from a Yellow/Red run that needs the paid workflow.

## 60-second receipt

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-composio.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-composio.md
```

Paste this into the agent/tool run ticket before enabling broad tools:

```text
Composio tool-agent preflight receipt
- Target repo/workspace:
- Toolkits/connectors enabled:
- Agent may use:
- Agent must ask before:
- Agent must not touch:
- Free scan result: Green / Yellow / Red
- Risk buckets observed: agent config / MCP or tool config / package scripts / workflow files / secret-adjacent files / destructive shell
- Decision: continue with limited tools, or buy/use the full preflight workflow before widening scope.
```

## Yellow / Red buy trigger

Buy or use the [$7 AI Agent Safety Starter Pack](https://payhip.com/b/1nmxV) when the free scan finds two or more of these before a Composio-backed run:

- `.env`, token, auth, or deploy-adjacent files that should not be copied into agent context.
- MCP, tool, Claude, Cursor, Copilot, or other agent instruction/config files that can steer tool calls.
- Package scripts, lifecycle hooks, Docker/devcontainer commands, or workflow files the agent might trigger.
- Shell snippets such as `curl | sh`, `rm -rf`, broad chmods, force pushes, or Docker socket access.
- A tool route that can post comments, open PRs, browse authenticated pages, hit SaaS APIs, or mutate external state.

If the scan is Green, keep the free receipt and run with least-privilege tools. If it is Yellow/Red, the paid bundle saves the repeat setup work: full handoff template, destructive-command hook, demo risky repo, report template, and local verifier.

## Copy/paste guardrail for the first task

```text
Before using Composio tools, run the agent preflight scanner and attach the receipt. Use read-only or least-privilege tool scopes until the receipt names the repo risk buckets, allowed commands, must-ask actions, and must-not-touch paths. If the result is Yellow/Red, use the full preflight workflow before enabling write-capable tools or credential-backed connectors.
```
