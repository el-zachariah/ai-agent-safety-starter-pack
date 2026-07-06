# Microsoft AutoGen multi-agent workflow preflight proof

**Proof marker:** Microsoft AutoGen multi-agent preflight proof

**Named target verified:** `microsoft/autogen` is public and not archived at https://github.com/microsoft/autogen.

- Stars observed: `59524`
- Last updated: `2026-07-06T10:09:05Z`
- Description: A programming framework for agentic AI
- Preflight offer: free lite scanner + paid `$7` AI Agent Safety Starter Pack at https://payhip.com/b/1nmxV

## Why AutoGen teams should care before the first agent run

AutoGen-style multi-agent workflows turn one prompt into several autonomous roles, tool calls, generated code paths, and follow-up execution steps. The risk is not only a bad answer; it is an agent conversation that quietly touches package scripts, workflow files, local tool functions, API-backed connectors, or secret-adjacent config before a human has a short preflight receipt.

Use this proof when a team is about to let AutoGen agents or an AutoGen-like group chat operate inside a real repository.

## 90-second preflight receipt

1. Run the free lite scanner from this repo before giving agents write access:

   ```bash
   python3 scripts/agent_preflight_lite.py --path . --format markdown > agent-preflight-autogen.md
   ```

2. Attach `agent-preflight-autogen.md` to the issue, PR, runbook, or agent task card.
3. Check the Green / Yellow / Red decision before enabling code execution, package installs, shell commands, CI edits, or MCP/API tools.
4. If the receipt is Yellow or Red, pause and use the paid pack checklist/templates to shrink scope before the run starts.

## What the receipt should catch for AutoGen work

- `requirements.txt`, `pyproject.toml`, `package.json`, or generated scripts that an agent may execute without review.
- `.github/workflows/`, deployment config, or automation files that could be edited by an agent conversation.
- `.env`, `OAI_CONFIG_LIST`, API-key examples, vector/database config, or tool credentials that should stay outside prompt context.
- Tool/function definitions that allow file writes, network calls, browser automation, or shell execution.
- Nested agent handoffs where one role asks another role to run commands outside the original task scope.

## Buy / skip decision for this segment

- **Green:** small documentation-only AutoGen experiment, no repo writes, no shell/package/deploy tools, no secret-adjacent files. Skip the paid pack for now.
- **Yellow:** agents can read repo context, suggest edits, run tests, or touch workflow/package files. Buy the `$7` pack before the first run so the reviewer has a copy-paste scope checklist and rollback receipt.
- **Red:** agents can execute commands, call API-backed tools, deploy, mutate CI, or see secret-adjacent config. Buy the pack and require a human approval checkpoint before tools execute.

## Copy-paste task card

```md
Before enabling Microsoft AutoGen agents on this repo, run the free agent-preflight scanner and attach the Markdown receipt here. If the result is Yellow or Red, use the AI Agent Safety Starter Pack checklist to narrow file scope, tool permissions, rollback steps, and reviewer sign-off before the first autonomous run.
```

Links:

- Free scanner/source repo: https://github.com/el-zachariah/ai-agent-safety-starter-pack
- Landing page: https://el-zachariah.github.io/ai-agent-safety-starter-pack/
- Paid checklist/templates: https://payhip.com/b/1nmxV
