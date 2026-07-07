# Local-only privacy receipt before checkout

`LOCAL_ONLY_PRIVACY_RECEIPT_2026_07_07`

Use this page before buying if the main hesitation is privacy: **the free scan and the paid ZIP workflow are designed to run locally on your machine.** Signal Loom Works does not need your private repository, secrets, customer data, or screenshots to make the basic buy/skip decision.

## What stays local

- Run the free scanner against your own checkout from your terminal.
- Keep the scan output in your repo, issue, pull request, or local notes unless you choose to share a sanitized summary.
- After purchase, unzip the bundle locally and run the included verifier before copying templates or hooks into a real repo.
- Review MCP, Cursor, Claude, package-script, workflow, and `.env`-adjacent findings inside your own environment.

## What Signal Loom Works does not need

Do **not** paste private source code, secrets, credentials, `.env` values, card details, billing data, payment-provider screenshots, customer data, or order identifiers into public GitHub issues.

A public-safe support note can say:

- which public page you were reading,
- which public command or step failed,
- operating system and Python version,
- non-secret error text,
- whether the free scan was Green, Yellow, or Red.

## Buy / skip boundary

Buy the $7 pack only when a local scan is Yellow/Red or when you need the reusable handoff, hook, template, demo, and verifier for repeated agent runs. If the scan is Green and you do not need a reusable receipt, keep the free scanner and normal review process.

Product page: <https://payhip.com/b/1nmxV>
Support path: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>
