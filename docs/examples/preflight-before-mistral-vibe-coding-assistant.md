# Preflight before Mistral Vibe coding assistant sessions

Named customer segment: teams using `mistralai/mistral-vibe` before terminal AI coding sessions touch repo context, shell/package commands, workflow files, MCP/tool connectors, or secret-adjacent config.

Public target evidence checked during this deadline pulse: [`mistralai/mistral-vibe`](https://github.com/mistralai/mistral-vibe) is live, not archived, showed `4634` GitHub stars, and was updated `2026-07-06T04:33:59Z`. Repository description captured: "Minimal CLI coding agent by Mistral".

Why this is a checkout-start proof: a Vibe-style coding assistant buyer already understands terminal AI, but the purchase hesitation is whether this $7 bundle is real and immediately relevant. This page gives that buyer a free 60-second receipt first, then points only Yellow/Red repos to the reusable report template, destructive-command hook, demo risky repo, and verifier in the paid pack.

## 60-second receipt before a Vibe-style run

```bash
python3 agent_preflight_lite.py /path/to/repo --json > mistral-vibe-coding-assistant-preflight.json
python3 agent_preflight_lite.py /path/to/repo > mistral-vibe-coding-assistant-preflight.md
```

Write this into the issue, PR, or handoff note before the assistant gets shell access:

```text
Mistral Vibe coding assistant preflight receipt
Repo: <repo path or URL>
Decision: Green / Yellow / Red
Risk buckets found: <agent instructions, package scripts, workflows, MCP/tool config, secrets-adjacent files, destructive shell>
Allowed commands: <install/test/build commands allowed>
Must-ask actions: <deploy, credential, rm, chmod, force-push, external API mutation>
Next step: Green = proceed with review; Yellow/Red = use the reusable handoff template and command guardrail before the run.
```

## What to inspect before granting scope

- Repo instructions that can steer the assistant: `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`, `.github/copilot-instructions.md`, or project-specific agent notes.
- Package scripts, build scripts, workflow files, and generated commands the assistant may run without noticing side effects.
- MCP/tool connector config, browser/API automation, deployment files, or local services that could mutate external systems.
- Secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, SSH keys, cloud config, or token-bearing samples.
- Destructive shell patterns such as `rm -rf`, `chmod 777`, `curl | sh`, Docker socket access, force-pushes, or credential exfiltration risk.

## Buy / skip trigger

- **Green:** keep using the free scanner and ordinary code review.
- **Yellow:** buy the $7 pack if you need the reusable handoff template, checklist, and command guardrail before letting the assistant iterate.
- **Red:** stop the run until a human narrows scope; use the paid bundle to write the preflight report and block destructive commands before resuming.

Paid bundle: <https://payhip.com/b/1nmxV>
