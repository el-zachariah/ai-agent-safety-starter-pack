# Goose local agent workflow preflight proof

Marker: GOOSE_LOCAL_AGENT_WORKFLOW_PROOF

Target verified: [`aaif-goose/goose`](https://github.com/aaif-goose/goose) — 50765 GitHub stars; updated 2026-07-07T10:43:34Z.

This is a buyer-specific proof for Goose teams before local agents, extensions, shell/file tools, MCP config, package scripts, and secret-adjacent runtime settings enter scope. It gives a first buyer a concrete receipt they can copy before buying the reusable $7 workflow bundle.

## One-minute preflight receipt

| Step | Agent/workflow risk to check | Receipt line to keep |
|---:|---|---|
| 1 | local shell/file tools touching repo or home paths | Record owner, touched file, and approve/skip before the agent continues. |
| 2 | extensions and MCP servers expanding tool scope | Record owner, touched file, and approve/skip before the agent continues. |
| 3 | package scripts or install hooks after agent edits | Record owner, touched file, and approve/skip before the agent continues. |
| 4 | provider keys and workspace config near the run | Record owner, touched file, and approve/skip before the agent continues. |
| 5 | logs retaining private repo context | Record owner, touched file, and approve/skip before the agent continues. |

## Copy-paste handoff receipt

```text
GOOSE_LOCAL_AGENT_WORKFLOW_PROOF
Target: aaif-goose/goose
Run scope: <agent / workflow / tool / config files changed>
Green: only prompts/docs/tests changed; no tools, package scripts, deployment files, or secret-adjacent config touched.
Yellow: tools, workflow config, package scripts, CI, deploy files, memory/vector stores, or API connectors changed; run the paid checklist before merging.
Red: credentials, authenticated user actions, production deploy, destructive shell, payment/customer data, or legal/KYC surfaces enter scope; stop and require owner review.
Decision: Green / Yellow / Red
Owner: Wealth Hunter / Signal Loom Works public preflight pattern
```

## Buy/skip trigger

- **Green:** use this free receipt and the lite scanner.
- **Yellow:** buy the reusable $7 starter pack when you need the report template, destructive-command guardrail, and repeatable handoff checklist: https://payhip.com/b/1nmxV
- **Red:** do not buy as a substitute for legal/security review; get an owner to approve credentials, production, payment, customer-data, or legal/KYC handling first.

Proof marker: GOOSE_LOCAL_AGENT_WORKFLOW_PROOF
