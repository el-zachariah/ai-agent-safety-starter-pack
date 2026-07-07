# Preflight before DeepEval LLM evaluation workflows

Buyer segment: teams using [confident-ai/deepeval](https://github.com/confident-ai/deepeval) to run LLM evaluation suites, agent regression tests, and red-team metrics before shipping agent changes.

Public target verified: `confident-ai/deepeval` is active, has 16,684 GitHub stars, and describes itself as: "The LLM Evaluation Framework". Last updated: 2026-07-07T03:14:20Z.

## Why this proof exists

DeepEval users already care about measurement, but checkout friction remains high when a seller only says "agent safety" generically. This page shows exactly where the free preflight and the paid starter pack fit in a DeepEval-style workflow.

## Copy-paste preflight receipt for a DeepEval change

1. Before a Claude Code/Codex/Cursor agent edits evaluation prompts, scorers, fixtures, or CI commands, run the free scanner from this repository at the repo root.
2. Save the Green/Yellow/Red receipt next to the DeepEval run output, for example `artifacts/agent-preflight-before-deepeval.txt`.
3. If the result is **Green**, proceed with the free scanner and keep the receipt in the PR.
4. If the result is **Yellow**, buy the starter pack for the paid handoff prompts/checklists before allowing the agent to mutate eval datasets, API-token plumbing, shell hooks, or deployment scripts.
5. If the result is **Red**, buy/use the paid pack only after freezing the risky command path, credential surface, and rollback checklist.

## DeepEval-specific risk map

| Surface | Preflight question | Buy trigger |
|---|---|---|
| Metric prompts and judge templates | Could an agent rewrite scoring criteria without a visible before/after receipt? | Yellow |
| Golden datasets and synthetic cases | Could generated fixtures include secrets, private examples, or unreviewed production traces? | Yellow |
| CI eval commands | Could the agent add a shell/install step that exfiltrates tokens or runs outside the repo? | Red |
| Cloud/API credentials | Are DeepEval or provider keys referenced in env files, notebooks, or webhook handlers? | Red |
| Regression reports | Does the PR include a compact preflight receipt maintainers can review before eval results? | Green/Yellow |

## Paid upgrade trigger

Use the free repository when you only need a quick local scanner. Buy the $7 starter pack when the DeepEval workflow is about to touch private traces, API tokens, model-provider keys, release gates, or customer-visible evaluation claims.

Paid pack: https://payhip.com/b/1nmxV

Seller identity: Wealth Hunter / Signal Loom Works.
