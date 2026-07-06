# Google ADK Python agent preflight proof

Buyer segment: teams using [`google/adk-python`](https://github.com/google/adk-python) or a similar Google Agent Development Kit Python workflow before agents get repository files, shell commands, package scripts, tool/API connectors, deployment config, or secret-adjacent environment values.

Target evidence captured 2026-07-06T03:22:47-05:00: `google/adk-python` is public, not archived, observed stars `20489`, updated `2026-07-06T07:55:05Z`, description: "An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.".

## Why this matters for Google ADK Python runs

ADK-style Python agents often move quickly from a demo agent into real tools, environment variables, local package scripts, deployment helpers, and repo-specific instructions. That is exactly when a cheap preflight helps: it gives the team a written handoff before the agent touches files or runs commands.

Use the free scan before the first ADK agent run, before adding tool/API credentials, and before letting an agent execute package/test/deploy commands.

```bash
python3 agent_preflight_lite.py /path/to/repo --json > google-adk-preflight.json
```

## Green / Yellow / Red decision gate

- **Green:** keep the free receipt with the task and skip the paid pack for now.
- **Yellow:** review package scripts, workflow files, agent instructions, tool/API config, deployment files, and secret-adjacent paths before broadening ADK tool scope.
- **Red:** stop the run; buy the $7 AI Agent Safety Starter Pack (https://payhip.com/b/1nmxV) if you need the reusable hook bundle, reviewer checklist, and repeatable receipts before agent execution.

## Copy-paste ADK handoff receipt

```md
Google ADK Python preflight receipt
- Repo scanned before agent execution: <repo/path>
- Agent/task: Google ADK Python agent / tool workflow
- Decision: Green / Yellow / Red
- Top findings: <3 bullets from agent_preflight_lite.py>
- Scope allowed after review: <files only / tests only / package scripts / no deploy / no secrets>
- Next gate: rerun preflight before adding credentials, enabling new tools, or running deploy commands.
```

## What the paid bundle adds for Yellow/Red scans

The public scanner proves the use case without requiring a purchase. The $7 pack is for teams that hit Yellow/Red and want ready-to-drop reviewer prompts, preflight command hooks, and handoff receipts so every ADK-style agent run starts with the same safety gate.

Marker: `GOOGLE_ADK_PYTHON_AGENT_PROOF`
