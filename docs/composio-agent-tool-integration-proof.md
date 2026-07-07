# Composio agent tool-integration proof

Marker: COMPOSIO_AGENT_TOOL_INTEGRATION_PROOF

Verified public target: [ComposioHQ/composio](https://github.com/ComposioHQ/composio) — 29120 GitHub stars, updated 2026-07-07T06:55:56Z. Description observed during this pulse: Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action..

## Who this proof is for

This proof is for Composio tool-calling agent teams who need a quick, local repo-risk receipt before an agent receives external API/tool permissions through Composio. The buyer fear is not whether the agent framework works; it is whether a reviewer can see that tool permissions, scripts, CI, deploy, and secret-adjacent surfaces were checked before the agent touched the repo.

## Free preflight path

1. Clone or download the free preview: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>.
2. Run the lite scanner before starting the agent task.
3. Save the Markdown receipt beside the issue, PR, or handoff ticket.
4. Paste the receipt into the task so reviewers see the checked surfaces.

Example command:

```bash
python3 agent_preflight_lite.py /path/to/repo --format markdown --out preflight-receipt.md
```

## Composio tool-calling agent teams surfaces to check first

Use this proof when the repo contains or recently changed: composio config, tool/action manifests, OAuth/API-key setup docs, MCP/tool server config, package scripts, CI/deploy workflows.

Minimum useful receipt:

- Did the repo expose agent/tool permissions, tool config, shell scripts, CI, deploy paths, or secret-adjacent files?
- Did the task touch files that can run commands after checkout, install, test, or deploy?
- Is the result Green, Yellow, or Red before the agent continues?

## Buy / skip trigger

- **Green:** use the free scanner and skip the paid pack for now.
- **Yellow:** buy the $7 starter pack if you need the reusable hook, review-comment template, and copy-paste handoff receipt.
- **Red:** buy the $7 starter pack before handing the repo back to the agent or asking for review.

Paid bundle: <https://payhip.com/b/1nmxV>

## Copy-paste handoff receipt

```text
Composio tool-calling agent teams preflight receipt
Target checked: <repo path or PR URL>
Agent task: <short task>
Decision: Green / Yellow / Red
Key repo surfaces: <tool config, scripts, CI, deploy, secrets-adjacent files>
Next step: proceed / tighten task scope / run paid starter-pack hook and attach report
Proof marker: COMPOSIO_AGENT_TOOL_INTEGRATION_PROOF
```

Shipped by Wealth Hunter / Signal Loom Works via el-zachariah on 2026-07-07T02:21:19-05:00.
