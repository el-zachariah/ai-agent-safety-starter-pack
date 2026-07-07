# Two-minute team purchase note

`TEAM_PURCHASE_NOTE_2026_07_07`

Use this public-safe note when a maintainer, team lead, or teammate needs a plain-language reason before buying the $7 AI Agent Safety Starter Pack from Payhip.

The note deliberately avoids private repo details, billing details, account screenshots, secret names, and anything that should not be posted in a public issue or chat.

## Copy-paste note

```text
AI-agent repo preflight purchase note

Context: we are about to let an AI coding agent, tool-calling agent, or local automation work inside a real repository.

Free scan already run: yes/no
Free scan result: Green / Yellow / Red
Risk buckets seen: agent instructions / MCP or tool config / package scripts / workflow files / secret-adjacent paths / destructive shell commands / other: ____

Decision:
- Green: keep using the free lite scanner for this run; do not buy the pack for this repo yet.
- Yellow: buy the $7 pack if we need the reusable report template, destructive-command hook, demo risky repo, and verification scripts before the agent continues.
- Red: pause the agent run and buy the $7 pack before handing the repo back to the agent or asking a reviewer to sign off.

Private-data boundary: do not paste private code, secrets, order details, card details, or account screenshots into public support. Share only the free scan color and a non-secret symptom if help is needed.

Checkout link: https://payhip.com/b/1nmxV
Public source and free scanner: https://github.com/el-zachariah/ai-agent-safety-starter-pack
```

## When this note is enough

Use the note when the only blocker is a teammate asking, “why buy this instead of using the free scanner?” The answer is:

- the free scanner is enough for Green results;
- Yellow or Red results create repeatable handoff work;
- the paid pack saves rebuilding the same report, hook, demo, and verifier every time an agent run touches a risky repo.

## When not to use this note

Do not use it as a substitute for formal legal, security, procurement, or payment-provider review. If your organization requires a formal process, follow that process and keep private repository details out of public support channels.

If the checkout, download, or ZIP-verifier wording is unclear, use the public-safe checkout help path instead: https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml
