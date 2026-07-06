# Preflight before DSPy LLM program and eval pipelines

**DSPy LLM program preflight proof.** Use this when a team using [`stanfordnlp/dspy`](https://github.com/stanfordnlp/dspy) is about to let an LLM program, optimizer, evaluator, tool wrapper, notebook, or CI job operate against a real repository, API-backed dataset, or deployment environment.

Target evidence checked during this pulse: [`stanfordnlp/dspy`](https://github.com/stanfordnlp/dspy) was public on GitHub, not archived, with 35,871 stars and updated at `2026-07-06T13:23:38Z`. Description observed: "DSPy: The framework for programming—not prompting—language models".

## Why this buyer should care before checkout

DSPy users often wire prompts, retrieval modules, tools, eval scripts, notebooks, datasets, package scripts, provider keys, and CI workflows together. A quick preflight receipt makes it obvious whether a run is still a safe sandbox or has crossed into repo, shell, credential-adjacent, or deployment scope.

## Free preflight before the DSPy run

1. Run the free scanner before giving the DSPy workflow repo, package-script, notebook, eval, dataset, MCP/tool, or deployment scope:

   ```bash
   python3 agent_preflight_lite.py --repo /path/to/dspy-project --output-md agent-preflight-dspy.md --output-json agent-preflight-dspy.json
   ```

2. Paste this receipt into the task, PR, or experiment note before the DSPy run starts:

   ```text
   DSPy LLM program preflight receipt
   - Target workflow: <optimizer/eval/tool/notebook/CI job>
   - Repo/branch scanned: <repo + branch>
   - Decision: Green / Yellow / Red
   - Risk buckets: <agent config, package scripts, workflow files, secrets, tool/API connectors, deployment config>
   - Human approval required before: shell/package scripts, deploy steps, secret-adjacent files, paid APIs, destructive data changes
   ```

3. Keep the free scanner if the result is Green. Buy only when the run is Yellow/Red or the workflow touches real repo writes, shell commands, provider keys, deployment settings, notebooks with credentials, or API-backed datasets.

## Paid-pack trigger

Buy the [$7 AI Agent Safety Starter Pack](https://payhip.com/b/1nmxV) when the DSPy workflow is about to run against a real repository, package script, CI job, provider key, eval dataset, MCP/API connector, or deployment surface and the free scan is **Yellow/Red**.

Machine marker for verification: `DSPY_LLM_PROGRAM_PROOF`.
