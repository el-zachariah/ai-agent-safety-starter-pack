# Preflight before Mastra-style TypeScript agents

Use this 60-second proof before a Mastra or similar TypeScript agent workflow gets repo files, local tools, package scripts, MCP/API connectors, memory/storage config, or deployment secrets.

Public reference point: [`mastra-ai/mastra`](https://github.com/mastra-ai/mastra).

## Who this is for

- JavaScript/TypeScript teams wiring agent tools to real repositories.
- Agent builders adding package scripts, environment variables, memory stores, or deployment steps.
- Maintainers who want a visible handoff note before an agent run starts editing code or calling tools.

## Run the free check first

```bash
python3 agent_preflight_lite.py /path/to/your/mastra-project --json > agent-preflight-mastra.json
python3 agent_preflight_lite.py /path/to/your/mastra-project
```

Look for the buckets that matter most before a TypeScript agent run:

- `package.json` scripts that install, build, deploy, seed databases, or delete generated files.
- `.env`, `.npmrc`, provider keys, vector-store credentials, or secret-adjacent config.
- MCP / tool connector config that lets the agent read files, call APIs, browse, or run shell commands.
- workflow files that can publish packages, trigger deployments, or mutate production resources.

## Copy-paste run ticket

```text
Mastra preflight receipt: agent-preflight-mastra
Scan result: Green / Yellow / Red = ______
Risk buckets found: ______
May run without asking: npm test, npm run lint, read-only repo inspection
Must ask first: npm install, npm run build with network, migrations, deploy/publish scripts, tool calls using live API keys
Must not touch: .env*, .npmrc, production deployment config, billing/provider credentials
Upgrade trigger: buy/use the $7 full workflow if the scan is Yellow/Red or the agent needs package-script + credential-adjacent scope.
Paid workflow: https://payhip.com/b/1nmxV
```

## Example decision

| Signal | Decision |
|---|---|
| `package.json` has `deploy`, `db:push`, or script chains | Yellow: write may-run / must-ask rules before the agent acts |
| `.env.local`, provider keys, or vector-store credentials are present | Red until secrets are excluded and tool scope is narrowed |
| MCP/tool connector config is present | Yellow/Red depending on whether connectors can write, browse, or call paid APIs |
| No agent config, no risky scripts, no secret-adjacent files | Green: use the free scanner and normal review discipline |

## When the $7 pack is worth it

Buy the full starter pack only when the free scan creates real handoff work: multiple risk buckets, package-script execution, credential-adjacent config, MCP/tool connectors, or a repeatable agent-review process your team will reuse. The paid bundle adds the reusable preflight mini, destructive-command hook, report templates, buyer quickstart, risky demo repo, and verifier so you do not rebuild the workflow during the run.
