# Preflight before MCP TypeScript SDK server edits

**Verified public target:** `modelcontextprotocol/typescript-sdk` — https://github.com/modelcontextprotocol/typescript-sdk  
**Why this segment is real:** GitHub reports 12805 stars, last updated `2026-07-06T19:30:04Z`, and describes it as: "The official TypeScript SDK for Model Context Protocol servers and clients".

MCP TypeScript SDK server users are a strong first-buyer segment for the AI Agent Safety Starter Pack because they already let an AI coding agent inspect or change real repositories. The friction is not whether they understand agents; it is whether they trust a tiny seller enough to pay for a local-first preflight bundle. This page gives them a public, copy-paste proof before checkout.

## 60-second local preflight for MCP TypeScript SDK server users

Run the free scanner first, before asking the agent to edit files or prepare a PR:

```bash
python3 scripts/lite_repo_preflight.py --format markdown --output preflight-receipt.md .
```

Use the resulting receipt as the handoff boundary:

- **Green:** run the MCP TypeScript SDK server task with the free receipt attached; skip the paid pack for now.
- **Yellow:** buy the $7 pack when the receipt shows missing tests, missing rollback notes, broad dependency edits, or risky automation surfaces.
- **Red:** stop the agent task until a human narrows scope, protects secrets, and adds a rollback/test plan.

## Copy-paste handoff receipt

```markdown
AI-agent preflight for MCP TypeScript SDK server
Target repo: <your repo>
Agent task: <one sentence>
Decision: Green / Yellow / Red
Risk buckets: tests, secrets, dependency changes, generated files, destructive commands
Required before agent edits: commit clean worktree, attach preflight-receipt.md, define rollback command, name reviewer
Paid upgrade trigger: if decision is Yellow/Red, use the AI Agent Safety Starter Pack before asking the agent to continue.
```

## Why the paid bundle is relevant only after Yellow/Red

The public scanner proves the seller is not hiding the core idea behind checkout. The paid pack at https://payhip.com/b/1nmxV is for teams who hit Yellow/Red and want the fuller repo-preflight workflow, command hook, review-comment template, and reusable risk receipts before letting an agent touch production-adjacent code.

**Not affiliated with `modelcontextprotocol/typescript-sdk`.** This is a customer-specific safety proof for people using that style of terminal coding-agent workflow.
