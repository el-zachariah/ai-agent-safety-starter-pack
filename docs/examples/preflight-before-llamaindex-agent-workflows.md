# Preflight before LlamaIndex agent workflows

**Named segment:** Python teams using `run-llama/llama_index` or similar LlamaIndex agent/workflow repos before granting tool, retrieval, MCP/API connector, environment, package-script, or deployment context to an agent run.

**Public target evidence captured:** `https://github.com/run-llama/llama_index` is public; stars observed `50660`; updated `2026-07-05T20:06:40Z`; description: "LlamaIndex is the leading document agent and OCR platform".

## Why this buyer cares before checkout

LlamaIndex-style agent workflows often sit close to retrieval indexes, API connectors, tool functions, notebooks, `.env`-adjacent configuration, and deployment scripts. The first-dollar buyer does not need a broad security audit; they need a fast receipt that says whether the repo is safe enough for an agent handoff or whether it deserves a repeatable preflight bundle.

## 60-second handoff receipt

Run the free scan before the workflow agent gets shell/API scope:

```bash
python3 agent_preflight_lite.py /path/to/llamaindex-agent-repo --format markdown > agent-preflight-llamaindex.md
```

Paste this receipt into the handoff:

```text
LlamaIndex agent preflight receipt
Repo: <repo-url-or-path>
Agent scope requested: tools / retrieval / MCP or API connectors / package scripts / deployment context
Scan result: Green / Yellow / Red
Signals found: <risk buckets + top findings>
Decision: Green = proceed with ordinary review; Yellow/Red = require the reusable report template, destructive-command hook, and explicit owner signoff before the agent run.
```

## Buy/skip trigger for this segment

- **Skip the paid pack** if the free scan is Green and the agent only reads docs or examples.
- **Buy the $7 starter pack** if the scan is Yellow/Red because the repo has two or more risk buckets, tool/API credentials, package scripts, notebooks with side effects, workflow files, MCP/API connector config, or deployment commands. The paid bundle gives the repeatable report template, destructive-command hook, demo risky repo, and verifier so the handoff can be reused instead of rewritten during the task.

## What to review first in a LlamaIndex repo

1. Tool/function definitions that can call network, shell, database, or SaaS APIs.
2. Retrieval/index storage paths that may expose local data or embeddings.
3. `.env`, notebook, CI, deployment, and package-script files near the agent workflow.
4. MCP/API connector configuration and tokens that an agent could inherit.
5. Any generated-code or write-back step that changes repo files, docs, or production assets.
