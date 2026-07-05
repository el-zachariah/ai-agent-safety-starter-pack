# Preflight before TDD Guard hooks

Customer segment: Claude Code users and maintainers evaluating or installing [TDD Guard](https://github.com/nizos/tdd-guard)-style enforcement hooks.

TDD Guard is valuable because it enforces test-first behavior while Claude Code works. The practical purchase anxiety for this segment is different from a generic developer: before a hook starts enforcing behavior inside a real repository, the buyer wants a quick, local receipt showing that the repo instructions, agent-facing docs, and obvious command-risk markers were checked first.

## 5-minute workflow

1. Run the free local preflight from this repository before enabling any Claude Code enforcement hook:

   ```bash
   python3 agent_preflight_lite.py --path /path/to/repo --output markdown > agent-preflight-receipt.md
   ```

2. Read the generated Green/Yellow/Red receipt before installing or turning on the hook.
3. Fix Yellow/Red items that are about project instructions, risky scripts, or agent-facing docs.
4. Then enable TDD Guard and keep the receipt with the first hook-enforced PR.

## Why this matters before a hook

- Hooks run in the context of a developer's real project, so trust is highest when the check runs locally and does not upload private code.
- A preflight receipt gives maintainers a review artifact before agent-driven changes start landing.
- The free scanner is intentionally small: it is a first screen, not a replacement for code review or security review.

## Buy/skip guidance for this segment

Buy the paid starter pack if you need the ready-made prompts, maintainer-review templates, and preflight playbooks for a team adopting Claude Code hooks/commands across multiple repos.

Skip the paid pack and use the free scanner only if you are experimenting alone and only need a quick local receipt.

Paid bundle: <https://payhip.com/b/1nmxV>

Support/trust notes: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/trust-and-support.md>
