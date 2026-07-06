# Preflight before AnythingLLM agent workspace workflows

**Named buyer segment:** teams using `Mintplex-Labs/anything-llm` or similar AnythingLLM agent workspace workflows before agents, low-code flows, connectors, package scripts, deployment config, or secret-adjacent files enter an AI-assisted run.

**Public target evidence captured:** `Mintplex-Labs/anything-llm` is public at https://github.com/Mintplex-Labs/anything-llm; stars observed `62687`; updated `2026-07-06T18:27:43Z`; description: "Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience ".

**Proof marker:** `ANYTHINGLLM_AGENT_WORKSPACE_PROOF`

## 60-second free preflight

Run the free scanner before a Flowise/agent-workflow change gets tool or repo access:

```bash
python3 agent_preflight_lite.py /path/to/flowise-or-agent-workflow-repo --format markdown > agent-preflight-flowise.md
```

Paste the receipt into the task, issue, PR, or runbook before the agent can touch:

- credential-backed connectors, vector-store docs, webhooks, or custom function/code nodes;
- `.env`, `.npmrc`, Docker/compose/deploy config, workflow files, or package scripts;
- generated app edits, shell commands, API keys, or production automation settings.

## Buy / skip trigger

- **Green:** keep the free receipt and normal review discipline; do not buy yet.
- **Yellow:** buy the `https://payhip.com/b/1nmxV` pack if two or more buckets light up, or if the run needs a reusable handoff/template before agents touch connectors or shell commands.
- **Red:** buy/use the full workflow before proceeding; freeze scope, exclude secret-adjacent files, and install the destructive-command hook before generated edits run.

## Copy-paste handoff

```text
ANYTHINGLLM_AGENT_WORKSPACE_PROOF
Before this Flowise/agent-workflow task can run, attach agent-preflight-flowise.md.
Allowed now: inspect docs, safe config, and non-secret workflow metadata.
Ask first: reading env/credential files, changing connector secrets, running package scripts, editing Docker/deploy settings, or touching production workflow exports.
Upgrade trigger: Yellow/Red free scan -> use the $7 AI Agent Safety Starter Pack workflow and hook: https://payhip.com/b/1nmxV
```
