# Preflight before Coze Studio agent builders

**Named segment:** teams using [`coze-dev/coze-studio`](https://github.com/coze-dev/coze-studio) or Coze Studio-style visual agent builders before workflows, plugins, knowledge bases, API connectors, webhook handlers, deploy files, or secret-adjacent environment values enter scope.

**Public target evidence captured this pulse:** `coze-dev/coze-studio` is public and not archived, with 21,119 GitHub stars observed, updated `2026-07-07T09:44:40Z`, and description: "An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and deployment like never before. Coze your way to AI Agent creation.".

## Why this is a first-dollar buyer fit

Coze Studio users can move quickly from a demo bot into a real app surface: workflow nodes, plugins/tools, uploaded knowledge, API-backed actions, bot publishing, Docker/deploy settings, and environment secrets. The buyer does not need a broad security audit before trying the product; they need a fast, local proof that the seller understands their exact handoff risk.

`COZE_STUDIO_AGENT_BUILDER_PROOF`

## Five-minute preflight

1. Run the free lite scanner before the Coze workflow or assistant receives repo, tool, or deployment context:

```bash
python3 agent_preflight_lite.py /path/to/coze-studio-agent-app --format markdown > coze-agent-preflight.md
```

2. Check the receipt for:
   - `.env`, `.env.local`, deployment, Docker, or provider-key placeholders;
   - plugin/tool/webhook/API connector code that can mutate data or call paid services;
   - package scripts, migrations, workflow files, or publish/deploy helpers;
   - project instructions that expand agent authority beyond the current task.
3. Paste the receipt into the issue, PR, or run ticket before enabling agent edits or tool calls.

## Buy/skip trigger

- **Green:** skip the paid pack and keep the receipt with the task.
- **Yellow/Red:** buy the $7 AI Agent Safety Starter Pack for the reusable checklist, hook, and handoff templates before the next Coze Studio workflow touches tools, deploy settings, or secret-adjacent config: https://payhip.com/b/1nmxV

## Copy-paste receipt

> I ran `agent-preflight-coze-studio` before giving a Coze Studio-style agent workflow access to repo, plugin/tool, webhook, or deployment scope. Current decision: `<Green|Yellow|Red>`. If Yellow/Red, I will narrow scope or use the paid starter pack before enabling package scripts, connector calls, deploy helpers, or secret-adjacent work.
