# Flowise visual agent-builder workflow preflight proof

Marker: `FLOWISE_VISUAL_AGENT_BUILDER_PROOF`

Public target verified: [`FlowiseAI/Flowise`](https://github.com/FlowiseAI/Flowise) is active, not archived, and shows 54342 GitHub stars as of this pulse. Repository description: Build AI Agents, Visually

## Why this buyer should care before the agent touches the repo

Flowise-style visual agent builders make it easy to chain LLM nodes, chatflows, tool calls, vector stores, credential-backed integrations, webhooks, and custom JavaScript/function nodes. That also means an AI coding agent can inherit a lot of hidden execution surface if it edits the app repo, exports flows, Docker files, or deployment scripts without a preflight receipt.

Use this free proof before a Claude Code/Codex/Cursor/Roo/agent run changes Flowise app code, custom nodes, `docker-compose.yml`, package scripts, credential exports, vector-store settings, API/webhook handlers, or deployment env.

## 60-second free preflight

```bash
python3 agent_preflight_lite.py /path/to/flowise-or-agent-builder-repo --format markdown > agent-preflight-flowise.md
```

Check the receipt for:

- Flowise chatflow/agentflow exports, custom tool/function nodes, webhook handlers, or API routes that can trigger side effects.
- Secret-adjacent files such as `.env`, `.env.local`, provider keys, vector database credentials, or Flowise credential-store backups.
- Package scripts, Docker/Compose files, deploy scripts, migrations, or cron/workflow files an agent might run while changing the app.
- MCP, Claude, Cursor, Copilot, Dev Container, or GitHub Actions config that changes what the agent can read or execute.

## Copy-paste handoff receipt for a Flowise task

```text
Before this Flowise visual agent-builder task can run, attach agent-preflight-flowise.md.
Allowed: read Flowise app files, flow JSON, docs, and tests needed for this task.
Ask first: provider keys, vector-store credentials, webhook secrets, deployment env, DB migrations, Docker socket, production data, or destructive shell commands.
Stop: if the scan is Red, if a custom node executes shell/network side effects, or if package/deploy scripts are unclear.
Buy trigger: if the free scan is Yellow/Red, use the $7 starter pack to keep the reusable report template, destructive-command hook, demo risky repo, and verifier with the task.
```

## Green / Yellow / Red decision

- **Green:** no credential-adjacent files, no risky package/deploy scripts, no agent/tool config, and no custom nodes with external side effects. Keep using the free scanner and ordinary review.
- **Yellow:** one or two risk buckets appear: package scripts, Flowise exports, MCP/Cursor/Claude config, Docker/deploy files, webhooks, or secret-adjacent placeholders. Buy the $7 pack when the free scan is Yellow/Red because the paid workflow gives a repeatable handoff, command guardrail, and verifier instead of a one-off note.
- **Red:** real credentials, production endpoints, destructive shell, DB migrations, docker socket access, or custom nodes that can mutate external systems. Stop and write the full preflight before granting agent tools.

Paid reusable workflow: https://payhip.com/b/1nmxV

Trust/support before buying: https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/trust-and-support.md
