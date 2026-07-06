# Preflight before Agent Client Protocol (ACP) agents

Customer segment: teams testing Agent Client Protocol-compatible coding agents and editor integrations before giving them local repo context or command execution.

Public target evidence verified with GitHub CLI in this pulse:

- Repository: [agentclientprotocol/agent-client-protocol](https://github.com/agentclientprotocol/agent-client-protocol)
- Description:  A protocol for connecting any editor to any agent
- Stars at verification time: 3578

## Why this buyer segment cares

ACP-style integrations make it easier for an editor or agent client to hand a real repository to an external coding agent. That is exactly when a lightweight preflight receipt is useful: before the agent inherits repo instructions, package scripts, MCP/tool config, generated credentials, or shell access.

Run the free scanner first:

```bash
python3 agent_preflight_lite.py /path/to/acp-enabled-repo --json
```

## 60-second ACP handoff receipt

Copy this into the issue, task, or PR before the ACP-backed agent starts:

```text
ACP agent preflight receipt
Repo: <repo URL or local path>
Agent/client: <ACP-compatible client or server>
Scan command: python3 agent_preflight_lite.py . --json
Risk color: Green / Yellow / Red
Reviewed before tool access:
- AGENTS.md / CLAUDE.md / .cursorrules / .cursor/rules/*
- MCP, Claude, Cursor, Copilot, or editor-agent config
- package scripts and workflow files the agent may run
- secret-adjacent files such as .env, .npmrc, .pypirc, id_rsa
Allowed commands: <tests/build only, no deploy/destructive commands>
Must ask first: <package install, network calls, credential reads, deploys>
Must not touch: <secrets, production configs, release automation>
Upgrade trigger: buy the $7 pack if the scan is Yellow/Red and you need the reusable report template, destructive-command hook, demo risky repo, and verifier.
```

## Buy / skip rule for this segment

- **Green:** one or fewer low-risk findings; keep the free receipt with the ACP task and proceed with normal review.
- **Yellow:** two or three buckets, package scripts, agent instruction files, or MCP/editor config; use the paid pack when you want a repeatable handoff instead of rewriting this receipt.
- **Red:** destructive shell, secret-adjacent files, workflow automation, or unclear command scope; use the full $7 workflow before the ACP-backed agent gets tool access.

Paid bundle: <https://payhip.com/b/1nmxV>
