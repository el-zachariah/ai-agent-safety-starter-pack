# Preflight before browser-use web agents

Customer segment: teams using [`browser-use/browser-use`](https://github.com/browser-use/browser-use) or similar browser automation agents before they let an agent browse authenticated apps, use API keys, edit repo files, or run local test commands.

Target evidence captured for this proof:

- Repository: [`browser-use/browser-use`](https://github.com/browser-use/browser-use)
- Stars at capture: `102817`
- Updated at capture: `2026-07-05T13:22:17Z`
- Public description: `🌐 Make websites accessible for AI agents. Automate tasks online with ease.`

## Why this segment should care before buying

Browser agents are often tested in real product repos with `.env` files, browser profiles, local servers, and payment/admin surfaces nearby. A repo preflight is the fast sanity check before an agent receives that environment.

Run the free scanner first. If it reports **Yellow** or **Red**, the paid **AI Agent Safety Starter Pack** gives the repeatable command hook, checklist, and handoff receipt needed to make browser-agent runs reviewable instead of vibes-based.

## 30-second browser-agent preflight

1. Clone or open the repo that will host the browser-use task.
2. Run the free lite preflight scanner from this repo.
3. Look for:
   - exposed secrets or `.env` files near browser automation code,
   - destructive shell commands in scripts that the agent might call,
   - missing allow/deny boundaries for network, filesystem, and payment/admin pages,
   - no human-readable receipt for what the agent is allowed to touch.
4. If the scan is **Green**, use the free receipt template and move on.
5. If the scan is **Yellow/Red**, buy the [$7 full pack](https://payhip.com/b/1nmxV) before handing the browser agent broader credentials or shell access.

## Copy/paste review receipt

```md
Browser-use preflight receipt
- Target agent/task: <browser-use task or workflow>
- Repo scanned: <repo/branch>
- Risk level: Green / Yellow / Red
- Browser credentials/profile used: none / test-only / production-adjacent
- Secrets found near run path: yes/no
- Commands the agent may run: <explicit allowlist>
- Payment/admin pages blocked or test-only: yes/no
- Human reviewer: <name/handle>
- Decision: proceed / proceed with guardrails / block until fixed
```

## Paid upgrade trigger

Buy the [$7 AI Agent Safety Starter Pack](https://payhip.com/b/1nmxV) when the browser-use workflow is about to touch a real repo, authenticated browser profile, local `.env`, or payment/admin surface and the free scan is not clearly Green.
