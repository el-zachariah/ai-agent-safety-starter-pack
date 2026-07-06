# ElizaOS agentic OS/plugin workflow preflight proof

`ELIZAOS_AGENTIC_OS_PLUGIN_PROOF`

Public target verified: [`elizaOS/eliza`](https://github.com/elizaOS/eliza), described as "Open source agentic operating system" with topics including agentic, autonomous, plugins, RAG, swarm, Discord, Telegram, and Slack. This proof is for teams evaluating ElizaOS-style agentic operating-system/plugin workflows before agents receive repo context, package scripts, plugin hooks, RAG/vector settings, bot credentials, workflow/deploy config, MCP/API tools, or secret-adjacent environment files.

## 60-second free receipt before ElizaOS touches a real repo

```text
Target: ElizaOS agentic OS / plugin workflow
Repo: <repo, plugin, package, or bot integration under review>
Preflight command: python3 agent_preflight_lite.py . --json
Decision: Green / Yellow / Red
Allowed before first agent action: read docs, inspect plugin manifests, propose scope
Must ask before: npm/pnpm install, package script, bot token/env access, deploy workflow edit, RAG/vector store config, MCP/API connector, destructive shell command
```

## What the free scanner is checking

- agent instruction files such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, or project-specific plugin/agent rules;
- package scripts, monorepo workspaces, CI workflows, Docker/devcontainer files, and generated integration code that an ElizaOS-style agent may run or modify;
- bot/channel/plugin configuration for Discord, Telegram, Slack, RAG/vector stores, API tools, MCP connectors, and deployment workflows;
- secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, local keys, provider credentials, bot tokens, or wallet/payment config;
- destructive or high-blast-radius shell patterns that should be blocked before autonomous agent or plugin execution.

## Buy / skip trigger

- **Green:** no meaningful repo/tooling risk signals. Keep the free receipt and skip the paid pack for now.
- **Yellow/Red:** two or more buckets light up, or the agent/plugin can touch package scripts, workflow files, bot credentials, RAG/vector config, MCP/API connectors, deployment files, or secret-adjacent paths. That is the point to buy the $7 AI Agent Safety Starter Pack: https://payhip.com/b/1nmxV

## Copy-paste handoff

```text
Before an ElizaOS agent, plugin, or bot workflow receives write/shell/tool scope, attach the free preflight receipt.
If the scan is Yellow/Red, use the paid starter pack to turn the receipt into: allowed commands, blocked destructive commands, files the agent must not read, token/env handling rules, plugin/RAG/API approval gates, and the human approval points for package/deploy/workflow changes.
```
