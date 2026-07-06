# Continue AI code assistant preflight proof

**Named segment:** teams using Continue / `continuedev/continue` or a Continue-style AI code assistant before they let an assistant read repo context, suggest edits, call tools, or touch shell/package workflow files.

**Public target evidence captured this pulse:** `continuedev/continue` at https://github.com/continuedev/continue has 34,708 GitHub stars and was last updated `2026-07-06T08:05:51Z`. Description observed: "open-source coding agent".

## Why this buyer should care before checkout

Continue users often connect an assistant directly to a real workspace. The free scanner gives a local, shareable preflight receipt before a teammate or agent expands scope into repo config, workflow files, package scripts, MCP/tool settings, or secret-adjacent files.

## 60-second local proof

1. Run the free lite scanner on the repo before enabling or expanding an AI coding session.
2. Attach the generated Markdown receipt to the PR/issue/task where the agent is being authorized.
3. Use the Green / Yellow / Red output to decide whether the free receipt is enough or whether to buy the paid starter pack for the ready-to-paste command hooks, review note, and handoff bundle.

## Buy / skip trigger for Continue teams

- **Green:** keep using the free scanner and link the receipt in the PR.
- **Yellow or Red:** buy the $7 starter pack at https://payhip.com/b/1nmxV when the repo includes checked-in assistant config/rules, package scripts, deploy workflows, MCP/tool definitions, or secret-adjacent environment paths that need a repeatable preflight command and review comment.

## Copy/paste receipt example

```text
Continue workspace preflight: ran ai_agent_safety_lite.py before expanding assistant scope.
Result: Yellow — agent/workflow config plus package scripts detected.
Action: require repo preflight hook + review comment before Continue-assisted edits merge.
Paid trigger: buy the $7 pack only if this Yellow/Red receipt needs repeatable commands/templates.
```

## Privacy and trust posture

The free proof stays local: no private code, secrets, or repo contents need to be sent to the seller. Buyers can verify the public source first at the GitHub repo, then use the paid pack only when they want the packaged hook/template workflow.
