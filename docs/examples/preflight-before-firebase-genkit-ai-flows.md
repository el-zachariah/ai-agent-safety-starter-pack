# Agent preflight before Firebase Genkit AI flows

Named buyer segment: Firebase Genkit teams building AI flows, tools, and provider-backed app actions using [genkit-ai/genkit](https://github.com/genkit-ai/genkit).

Public target verification for this proof:

- Repository: `genkit-ai/genkit`
- Stars at verification: `6192`
- Archived: `False`
- Updated at verification: `2026-07-06T15:22:19Z`
- Description: Open-source framework for building AI-powered apps in JavaScript, Go, and Python, built and used in production by Google

## Why this segment feels immediate

Genkit projects often put agent risk in normal application files: a flow starts calling a new tool, a schema accepts a broader action payload, or provider/model settings change which user context reaches the model. A maintainer needs a compact preflight receipt before merging that PR, not a generic AI safety lecture.

## 6-minute starter receipt

1. Run the free scanner before merging an agent-generated change to Genkit flows, tools, model/provider config, schemas, eval prompts, or deployment hooks.
2. Paste the receipt into the PR with the command, timestamp, touched risk areas, and whether the scanner saw new tool/action paths.
3. If the result is Green, keep using the free scanner.
4. If the result is Yellow or Red, buy the paid pack for the escalation checklist, reviewer prompts, and release-gate template: https://payhip.com/b/1nmxV

## Buy trigger for this exact segment

Buy the paid pack when a Genkit PR touches any two of these at once:

- `defineFlow`, `defineTool`, action handlers, or schema definitions.
- Provider/model routing, safety settings, or fallback model config.
- Eval prompts, golden tests, or release gates for AI behavior.
- Deployment/runtime code that can call external services or mutate user data.

Skip buying if the repo only changed docs, copy, CSS, or a demo prompt with no tool/action path.

## Minimal PR comment template

```text
Agent preflight for Firebase Genkit change
- Scope checked: flows / tools / schemas / provider config / eval prompts / deployment hooks
- Free scanner result: Green | Yellow | Red
- Merge condition: no new side-effecting flow or tool path without reviewer sign-off
- Paid escalation used? no unless Yellow/Red
```

Public funnel: https://el-zachariah.github.io/ai-agent-safety-starter-pack/
