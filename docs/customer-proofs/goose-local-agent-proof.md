# Goose local-agent teams — paid-pack readiness proof

Marker: `deadline-proof:goose-local-agent-proof`

Verified public target: [aaif-goose/goose](https://github.com/aaif-goose/goose) — 50730 GitHub stars, last updated `2026-07-06T23:48:19Z`.

## Why this named segment is a first-buyer fit

Goose teams run a local AI agent against developer workspaces. A preflight receipt helps separate Green repos from Yellow/Red handoff cases before an agent invokes tools or shell commands.

## What the free preflight proves before buying

Coding-agent buyers do not need to trust a seller claim first. They can run the free local scanner against their own repository and inspect the generated receipt before buying anything.

```bash
python3 tools/agent_preflight.py --path . --format markdown > agent-preflight-receipt.md
```

The receipt turns repo readiness into a Green/Yellow/Red decision for PR descriptions, issue handoffs, or internal approval before agent-assisted edits begin.

## Buy trigger for the paid starter pack

Buy the $5 AI Agent Safety Starter Pack when the receipt is **Yellow** or **Red**, or when the team needs a copy-paste handoff pack for:

- agent permission boundaries before install/test/build commands run;
- private-code and no-secrets handling rules;
- a reviewer checklist for AI-authored PRs;
- a concise risk summary that makes maintainers comfortable approving agent work.

If the receipt is clean Green and the team already has an agent-review checklist, skip the paid pack for now and keep using the free scanner.

Paid pack: https://payhip.com/b/1nmxV

## Trust note

This proof does not require uploading private code, secrets, or repository contents. The scanner and paid-pack templates are local-first; the buyer chooses what receipt text to share.
