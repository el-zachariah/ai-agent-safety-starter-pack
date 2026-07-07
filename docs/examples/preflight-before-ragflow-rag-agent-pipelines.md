# Preflight before RAGFlow RAG-agent pipelines

Target verified: [infiniflow/ragflow](https://github.com/infiniflow/ragflow) is an active public repo with 84480 GitHub stars and latest public update `2026-07-07T08:17:08Z`.

## Why this proof exists

A generic safety pitch is not enough for a RAGFlow RAG-agent pipeline teams buyer. The first-dollar checkout trigger is: "I am about to let an AI-agent workflow touch a real repo or service, and I need a fast proof that the seller understands my exact failure modes."

For RAGFlow RAG-agent pipeline teams, the risky surface is RAG agent pipelines where ingestion, retrieval, prompt routing, tool calls, and deployment endpoints can expose confidential source data. This proof maps the free scanner and the paid Agent Safety Starter Pack to that exact workflow.

## Copy-paste preflight receipt

Use this before approving a graph/crew/conversation change that can write files, call tools, deploy, or handle secrets:

```text
Agent Safety Preflight — RAGFlow RAG-agent pipeline teams
Target: infiniflow/ragflow
Change window: before merging an AI-agent workflow edit
Green: docs-only graph prompt/readme changes with no new tools, env vars, persistence, or deploy hooks
Yellow: new tool node, API client, memory/checkpoint path, eval dataset, generated file writer, or CI command
Red: credential handling, unreviewed shell/browser execution, production deploy, destructive repo cleanup, or payment/customer data access
Required receipt: save scanner output beside the PR/issue before the agent run starts
```

## Free scanner command

```bash
python3 agent_preflight.py --path . --format markdown > agent-safety-preflight-receipt.md
```

If the receipt is Green, the free repo may be enough. If it turns Yellow/Red, buy the $7 starter pack for the review checklist, buyer-facing receipt template, and rollback handoff: https://payhip.com/b/1nmxV

## RAGFlow RAG-agent pipeline teams checklist

1. List every graph node/agent role that can call a tool, write a file, browse, or invoke a shell command.
2. Mark every environment variable, API token, webhook URL, datastore, checkpoint, or memory path the workflow can read/write.
3. Run the scanner before the AI-agent edit, not after the generated diff looks scary.
4. Attach the receipt to the PR/issue so reviewers can see why the run is Green, Yellow, or Red.
5. If Yellow/Red, use the paid pack to turn the scanner output into a short approval note, rollback plan, and customer-safe handoff.

## Buy / skip trigger

- **Buy now** if this workflow can mutate real repos, run tools, touch secrets, change deployment state, or create customer-visible output.
- **Skip for now** if you are only reading docs or running a throwaway local demo with no credentials and no write path.

Paid upgrade: https://payhip.com/b/1nmxV
