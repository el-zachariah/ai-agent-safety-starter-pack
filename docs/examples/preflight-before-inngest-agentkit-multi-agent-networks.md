# Inngest AgentKit multi-agent network preflight proof

Target verified: [inngest/agent-kit](https://github.com/inngest/agent-kit) — AgentKit builds TypeScript multi-agent networks with deterministic routing, rich tooling, and MCP support.

Marker: `INNGEST_AGENTKIT_MULTI_AGENT_NETWORK_PROOF`
Paid upgrade trigger: https://payhip.com/b/1nmxV

## Why this matters before a real agent run

Inngest AgentKit teams are likely to connect agents, network routers, tools, MCP servers, Inngest functions, package scripts, deployment config, and provider keys before they know whether the repo is safe for autonomous edits or command execution. A generic safety checklist feels theoretical; this receipt names the exact surfaces an AgentKit maintainer or adopter can inspect before handing the repo to Claude Code, Codex, Cursor, or another coding agent.

## Five-minute preflight

1. Run the free lite scan on the repo branch that will receive the agent/network work.
2. Confirm no real `.env`, provider key, webhook secret, Inngest signing key, or deployment token is inside the agent-visible context.
3. Review package scripts, workflow files, MCP/server config, and tool adapters before the agent can execute them.
4. Attach the generated Green/Yellow/Red receipt to the issue, PR, or internal task before widening tool scope.
5. Buy the $7 starter pack when the receipt is Yellow or Red and the team needs the reusable handoff template, destructive-command hook, and full preflight mini instead of a one-off note.

## Copy-paste handoff receipt

```text
Inngest AgentKit preflight: INNGEST_AGENTKIT_MULTI_AGENT_NETWORK_PROOF
Target: inngest/agent-kit style TypeScript multi-agent network
Scope checked: deterministic routing, MCP/tools, Inngest functions, package scripts, deploy config, workflow state, and secret-adjacent env values
Decision: Green = attach this receipt and proceed; Yellow/Red = use the $7 workflow pack before widening agent or tool scope
Upgrade: https://payhip.com/b/1nmxV
```

## Buy / skip trigger

- **Green:** use the free receipt and continue; do not buy yet.
- **Yellow:** buy the $7 pack if a real agent will run package scripts, call MCP/API tools, or edit workflow/deploy files.
- **Red:** buy before proceeding; add the destructive-command hook and full report template before exposing secrets, deploy commands, or high-impact tools.
