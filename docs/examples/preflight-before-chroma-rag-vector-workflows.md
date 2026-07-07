# Preflight before Chroma RAG/vector workflows

Buyer segment: teams using [chroma-core/chroma](https://github.com/chroma-core/chroma) or Chroma-style vector/RAG infrastructure before AI agents, eval jobs, or coding assistants touch retrieval code, ingest scripts, and deployment config.

Public target verified: `chroma-core/chroma` is active, has 28,719 GitHub stars, and describes itself as: "Search infrastructure for AI". Last updated: 2026-07-07T03:16:13Z.

## Why this proof exists

Chroma teams already manage real application memory and retrieval context. A generic checkout page does not answer their immediate question: "what exactly should I check before an AI agent changes vector collections, embedding pipelines, package scripts, or credential-adjacent deployment files?" This proof makes the $7 starter pack feel relevant before checkout.

## Copy-paste preflight receipt for a Chroma change

1. Before a Claude Code/Codex/Cursor agent edits retrieval code, collection setup, ingest scripts, eval notebooks, CI, or deploy commands, run the free scanner from this repository at the repo root.
2. Save the Green/Yellow/Red receipt next to the RAG change, for example `artifacts/agent-preflight-before-chroma-rag-vector-workflows.txt`.
3. If the result is **Green**, attach the free receipt to the issue or PR and keep normal review discipline.
4. If the result is **Yellow**, buy the starter pack for the paid handoff prompts/checklists before letting the agent mutate collections, embeddings, retrievers, metadata filters, persistence paths, provider keys, package scripts, Docker/deploy files, and secret-adjacent env values.
5. If the result is **Red**, buy/use the paid pack only after freezing the risky command path, credential surface, rollback notes, and collection/data backup plan.

## Chroma-specific risk map

| Surface | Preflight question | Buy trigger |
|---|---|---|
| Collections and persistence | Could the agent delete, reindex, or repoint a collection without a visible before/after receipt? | Yellow |
| Embedding and retrieval code | Could generated changes alter chunking, metadata filters, or scoring in a way maintainers cannot audit quickly? | Yellow |
| Ingest/eval scripts | Could the agent run a package, Docker, notebook, or CI command that touches private data or external services? | Red |
| Provider/API credentials | Are vector DB, embedding provider, cloud, or webhook keys referenced in env files, deploy config, notebooks, or docs? | Red |
| PR handoff | Does the change include a compact preflight receipt before agent-written retrieval changes merge? | Green/Yellow |

## Paid upgrade trigger

Use the free repository when you only need a quick local scanner. Buy the $7 starter pack when the Chroma workflow is about to touch production collections, private documents, provider keys, deploy scripts, notebooks, or customer-visible retrieval/eval claims.

Paid pack: https://payhip.com/b/1nmxV

Seller identity: Wealth Hunter / Signal Loom Works.
