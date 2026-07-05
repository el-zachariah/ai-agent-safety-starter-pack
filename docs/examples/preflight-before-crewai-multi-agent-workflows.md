# Preflight before CrewAI-style multi-agent workflows

Use this when a repo is about to run a CrewAI-style workflow where multiple agents can call tools, read local files, invoke package scripts, or use API-backed `.env` values.

The goal is not to slow the team down. It is to write a short receipt before the first crew run so a human knows what the agents may read, what commands they may run, and which files stay out of scope.

## 5-minute receipt

```bash
python3 agent_preflight_lite.py /path/to/crewai-project --json > agent-preflight-crewai.json
python3 agent_preflight_lite.py /path/to/crewai-project > agent-preflight-crewai.md
```

Then review the CrewAI-specific surface the lite scanner cannot fully understand by itself:

- `agents.yaml`, `tasks.yaml`, or equivalent crew definitions
- custom tools under `tools/`, `src/*/tools/`, or similar folders
- `.env`, `.env.example`, `.crewai/`, `knowledge/`, vector-store, or cache folders
- package scripts that start crews, load secrets, scrape the web, call paid APIs, or write files
- CI/deploy jobs that can run the same crew with broader permissions than a local test

## Pasteable run note

```text
CrewAI preflight receipt
- Scan result: Green / Yellow / Red: <fill in>
- Risk buckets found: <agent config, package scripts, workflows, secret-adjacent files, risky shell>
- Crew entrypoint: <command or script>
- Allowed before approval: read repo files, run unit tests, run the crew only against fixture/demo data
- Must ask first: live API calls, scraping real sites, writing outside the repo, using production tokens, installing new packages, deployment
- Must not touch: .env, credentials, payment/admin dashboards, customer data, production databases
- Upgrade trigger: if the scan is Yellow/Red or the crew needs real tokens/tool access, use the full $7 bundle to keep the report template, destructive-command hook, and verifier with the repo.
```

## Why the paid bundle helps here

Multi-agent repos tend to sprawl: one YAML task can call a tool, the tool can call a package script, and the package script can touch secrets or external services. The free scanner gives the first pass. The paid bundle is useful when the scan finds enough risk that you want the reusable report template, command hook, and verification scripts instead of recreating them for every crew run.

Buy the full bundle only when this receipt turns Yellow/Red: <https://payhip.com/b/1nmxV>