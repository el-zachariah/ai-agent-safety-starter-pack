# Preflight before Semantic Kernel multi-agent runs

Customer segment: **Semantic Kernel multi-agent teams**.

Public target verified for fit:

- Repository: `microsoft/semantic-kernel`
- URL: https://github.com/microsoft/semantic-kernel
- Stars at proof time: 28268
- Updated at proof time: 2026-07-06T13:58:24Z
- Description: Integrate cutting-edge LLM technology quickly and easily into your apps

## Why this proof exists

Semantic Kernel multi-agent buyers are likely to let an agent or tool chain touch prompts, retrieval code, tool definitions, and repo state. The risk is not abstract: one missed secret, missing rollback note, or unclear human approval gate can turn a useful agent workflow into a cleanup bill.

This page shows the free receipt a buyer can run before teams composing Semantic Kernel planners, tools, memories, and agent handoffs before the first autonomous repository run.

## Five-minute free preflight

Run this from a copy of the repo before granting the agent write access:

```bash
python3 agent_preflight_lite.py --path . --profile agent-workflow
```

Suggested fixture to scan: **Directory.Build.props or pyproject.toml with semantic-kernel plus agent prompt folders**.

The free receipt should answer four first-buyer trust questions:

1. What files can the agent mutate?
2. Are secrets, env files, tokens, or local config exposed?
3. Is there an approval gate before commands, migrations, network calls, or deploys?
4. Is there a rollback note if the agent run makes a bad edit?

## Yellow/Red buy trigger

- **Green:** no paid upgrade needed; keep using the free scanner and checklist.
- **Yellow:** buy the starter pack when the scan finds missing approval gates, no rollback note, or unclear agent/tool boundaries.
- **Red:** buy before the next autonomous run when secrets, deploy files, production credentials, or destructive commands are in scope.

Paid bundle: https://payhip.com/b/1nmxV

## Copy-paste handoff receipt

```text
Segment: Semantic Kernel multi-agent
Target repo evidence: microsoft/semantic-kernel (28268 stars, updated 2026-07-06T13:58:24Z)
Free action: run agent_preflight_lite.py before the first repo-changing agent workflow.
Paid trigger: Yellow/Red findings around secrets, approval gates, rollback, or destructive tools.
Offer: AI Agent Safety Starter Pack at https://payhip.com/b/1nmxV
```

This is a trust proof, not a public endorsement by `microsoft/semantic-kernel`.
