# Preflight before Crush terminal coding agents

Marker: `CRUSH_TERMINAL_AGENT_PROOF`

Target segment: teams evaluating [`charmbracelet/crush`](https://github.com/charmbracelet/crush) or a Crush-style terminal coding agent before it edits files, runs package scripts, shells out, reads repo instructions, or works near secret-adjacent files.

Public target evidence captured in this pulse:

- Repository: `charmbracelet/crush`
- Description: Glamourous agentic coding for all 💘
- Stars observed: `26113`
- Updated at: `2026-07-06T07:17:54Z`

## Why this buyer should care before paying

Crush is explicitly an agentic coding workflow. The checkout-start problem for this product is trust: a buyer needs to see the exact moment where a cheap preflight is useful rather than another vague security checklist.

Use the free scanner first:

```bash
python3 agent_preflight_lite.py /path/to/repo --json
python3 agent_preflight_lite.py /path/to/repo > crush-preflight-receipt.md
```

Buy the `https://payhip.com/b/1nmxV` bundle only if the scan is Yellow or Red and Crush will touch a real repo: multiple risk buckets, package scripts, workflow files, agent instructions, secret-adjacent files, MCP/tool config, or shell commands that need a reusable may-run / must-ask / must-not-touch handoff.

## 60-second Crush handoff receipt

Copy this into the issue/PR/task before starting a terminal coding-agent session:

```md
Crush task: <one sentence>
Repo/path scanned: <path or commit>
Free preflight result: Green / Yellow / Red
Risk buckets found: <agent instructions, package scripts, workflow files, secrets-adjacent, risky shell, MCP/tool config>
May run: <safe test/lint/build commands>
Must ask first: <network installs, migrations, deploys, deletes, credential-adjacent edits>
Must not touch: <.env, tokens, production deploy config, unrelated workflows>
Upgrade trigger: If this is Yellow/Red, use the $7 AI Agent Safety Starter Pack for the reusable report template, destructive-command hook, demo risky repo, and verifier before handing Crush broad shell scope.
```

## What the paid pack adds when the scan is Yellow/Red

- a repeatable repo preflight mini instead of an ad-hoc note,
- local destructive-command hook examples before agent shell commands run,
- report templates that can travel with the Crush task or PR,
- a demo risky repo plus verifier so the buyer can check the workflow before using it on private code.

If the scan is Green, skip the purchase for now and keep the free receipt with normal code review discipline.

Paid bundle: https://payhip.com/b/1nmxV
