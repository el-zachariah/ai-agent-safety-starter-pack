# Approval packet before checkout

`APPROVAL_PACKET_BEFORE_CHECKOUT_2026_07_08`

Use this public-safe packet when a maintainer, team lead, reviewer, or manager asks for the short version before a $7 Payhip checkout. It keeps the decision tied to a local free scan and one real agent run, not a vague tool impulse.

## Start with the local scan

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/repo
```

Keep private code, secrets, billing details, order details, account screenshots, and private repo findings out of public issues. Share only the Green / Yellow / Red result and non-secret risk categories.

## One-screen approval summary

```text
AI Agent Safety Starter Pack approval packet

Public source and free scanner: https://github.com/el-zachariah/ai-agent-safety-starter-pack
Checkout link: https://payhip.com/b/1nmxV
Seller/public project: Signal Loom Works
Price: $7

Free scan result: <Green / Yellow / Red>
Agent scope: <read-only / edit files / shell / package scripts / MCP tools / browser / deployment-adjacent>
Why the paid ZIP is needed: <one setup loop saved / reusable handoff needed / destructive-command guardrail needed / skip because Green>
Private data boundary: local scan only; public support gets only non-secret symptoms.
Decision: <skip for now / buy before this agent run continues>
```

## What to attach internally

- [Two-minute value check](value-check-before-checkout.md) — use this to decide Green skip, Yellow buy only if it saves one setup loop, or Red buy before a broad agent run.
- [Team purchase note](team-purchase-note.md) — copy this when a maintainer or team lead wants plain-language context.
- [Expense/reimbursement note](expense-reimbursement-note.md) — copy this when a manager needs a small purchase note.
- [Security-review factsheet](security-review-factsheet.md) — share local-only data handling, ZIP SHA/file count, and pass/pause criteria.
- [Paid bundle contents preview](paid-bundle-contents-preview.md) — verify what the ZIP includes before Payhip.
- [Privacy before checkout](privacy-before-checkout.md) — keep private repository details local.

## Buy / skip rule

- **Green:** skip the paid ZIP for this repo run and keep the free scanner result.
- **Yellow:** buy only when the reusable report, hook pattern, demo, and verifier save at least one setup/review loop.
- **Red:** buy before continuing if the agent can run shell commands, touch workflow/deployment-adjacent config, or operate near credentials.

If checkout, download, or ZIP-verifier wording is unclear, use the public-safe buyer question / checkout help form and include only non-secret symptom text: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>.

