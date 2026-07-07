# Trust, support, and buyer proof

This page exists for the exact question a cautious buyer should ask before paying for a small tool from a new seller: **is this real, useful, and safe to try?**

## Public proof before purchase

- The free lite scanner is public: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>
- The live buyer page is public: <https://payhip.com/b/1nmxV>
- The product is intentionally low-ticket: **$7 USD** for a reusable repo-preflight workflow, command hook, templates, demo, and verifier.
- The free scanner should be run first. Buy only if the scan is Yellow/Red or you need a repeatable handoff before an AI coding agent gets shell access.

## Who is behind it

The product is published under **Signal Loom Works**, a small tool-and-template line for practical AI-agent workflows. The public work is maintained through the `el-zachariah` GitHub account so buyers can inspect the free code, docs, commit history, issues, and release artifacts before purchasing.

## What happens after purchase

The paid bundle is a downloadable ZIP. It is designed to stay local:

1. unzip the bundle,
2. run the included verifier,
3. copy the preflight/report templates into the repo you are preparing for an agent,
4. install or adapt the destructive-command hook if your workflow needs a command guardrail.

The bundle does **not** require sending your repository, secrets, or code to Signal Loom Works.

For buyers who want that boundary before checkout, use the [local-only privacy receipt](privacy-before-checkout.md). It states what stays local, what Signal Loom Works does not need, and what can safely go into a public support issue. `LOCAL_ONLY_PRIVACY_RECEIPT_2026_07_07`

For a quick confidence check after checkout, use the [90-second post-purchase ZIP verification](post-purchase-verification.md) before relying on the files in a real repo. `POST_PURCHASE_ZIP_VERIFICATION_2026_07_07`

If Payhip, download, or ZIP-verifier wording is confusing, use the [checkout friction help path](checkout-friction-help.md) before posting anything public. It keeps the support report limited to the free scan color, the step that stalled, and non-secret symptom text. `CHECKOUT_FRICTION_HELP_2026_07_07`

Before checkout, use the [paid bundle contents preview](paid-bundle-contents-preview.md) to inspect the expected v0.4 ZIP contents, SHA-256, file count, local verifier, and what is not included. `PAID_BUNDLE_CONTENTS_PREVIEW_2026_07_07`

## Support channel

For pre-sale questions, install friction, checkout-page friction, or a mismatch between the public description and the ZIP, use the public-safe buyer support form:

<https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>

You can also open a plain GitHub issue here:

<https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues>

Use the issue title prefix `[buyer question]` or `[support]` so it can be triaged quickly. If the Payhip page is unavailable or confusing, say what public page you were on and what non-private error text you saw; do not paste private code, secrets, credentials, customer data, card details, billing data, payment-provider screenshots, or order identifiers into public issues.

## What this is not

This pack is not a security audit, malware scanner, sandbox, secret scanner, compliance product, insurance policy, or replacement for human review. It is a practical pre-agent checklist and local guardrail starter for developers who want a cheap first pass before Claude Code, Cursor, Codex-style agents, or MCP-backed tools run commands in a real repo.

## Honest buy / skip rule

Buy the `$7` starter pack if:

- the free scan finds two or more risk buckets,
- the repo has MCP/Cursor/Claude settings or agent instruction files,
- package scripts/install steps include commands you do not want an agent running blindly,
- you need a reusable report template for repeated agent handoffs,
- you want a local destructive-command hook example instead of writing one from scratch.

Skip it for now if:

- the free scan is Green,
- the repo is disposable or already sandboxed,
- you only need a one-time note and not a repeatable workflow,
- you expect a full security audit or automated policy enforcement platform.

## Quick verification command

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py examples/sample-risky-repo
```

If the free sample is not useful to you, do not buy the paid bundle yet.
