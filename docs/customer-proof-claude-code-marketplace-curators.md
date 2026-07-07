# Customer proof: Claude Code marketplace curator safety pass

Target segment: maintainers and small-team buyers evaluating Claude Code command, hook, skill, or plugin submissions before they install or recommend them.

Named distribution targets this proof serves: `obra/superpowers-marketplace`, `wshobson/agents`, `jeremylongshore/claude-code-plugins-plus-skills`, and `davepoon/buildwithclaude`.

## Why this is immediately relevant

A curator has a different risk than a generic developer: one accepted listing can send many users to a command or hook that shells out, edits files, or asks for broad permissions. This proof shows how the Agent Safety Starter Pack is used as a fast acceptance receipt before a marketplace maintainer says yes.

## Five-minute curator pass

1. Clone or inspect the candidate Claude Code command, skill, hook, or plugin.
2. Run the public preflight route from this repository, starting with `agent_preflight_lite.py` when available.
3. Capture a receipt that answers four buyer-trust questions:
   - What commands, hooks, or scripts execute shell actions?
   - Are setup steps and permissions explicit enough for a first-time installer?
   - Does the repo include a rollback or uninstall path?
   - Is there a short support path if a buyer needs help after purchase?
4. If the receipt is clean, link the free public result in the listing review. If it is not clean, ask the submitter for a fix before recommending it.

## Paid upgrade trigger

Buy the $7 Agent Safety Starter Pack when the curator or small team wants the ready-made scanner, buyer checklist, demo report format, and local-first package rather than assembling the acceptance receipt manually.

Product: https://payhip.com/b/1nmxV

Support and trust proof: https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/trust-and-support.md

## Example acceptance note a curator can paste internally

> Preflight completed for this Claude Code listing. The repo exposes its executable surface, setup path, and support route clearly enough for a cautious install recommendation. I would still keep normal marketplace review, but this passes the first five-minute safety screen.

## Why this seller is real enough to test

- Public funnel and support page are live.
- The proof is tied to concrete Claude Code marketplace review work, not generic AI safety copy.
- The paid pack is low-ticket and meant to save one manual review cycle, not require a sales call.
