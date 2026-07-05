# MCP server maintainer proof

**Named buyer segment:** MCP server maintainers — maintainers accepting PRs that add .mcp.json, server configs, tool schemas, or agent-authored install commands.

This page exists so a maintainer can see, before purchase, exactly how the public free asset and the paid starter pack apply to their workflow.

## Fast fit check

- **Use the free public preflight when:** a contributor proposes MCP server/tooling changes and you want a visible preflight receipt before running or merging them.
- **Buy the paid starter pack when:** buy the $5 AI Agent Safety Starter Pack when the PR touches MCP config, command hooks, install scripts, or secrets-adjacent files and you need the deeper checklist, reviewer prompts, and copy-paste policy gates.
- **Skip the paid pack when:** the change is docs-only, already covered by your normal CI, and no agent-generated commands/configs enter the repo.

## Why this is relevant

Agent-generated repository changes often look small, but the risky part is usually the surrounding execution path: config files, local install commands, CI hooks, tool schemas, and review shortcuts. For MCP server maintainers, the proof target is not abstract agent safety; it is whether a maintainer can approve an agent-assisted PR without creating a command-execution or secret-handling surprise.

Public signals this proof is designed around: `.mcp.json`, `MCP server`, `tool schemas`, `agent-authored commands`.

## 10-minute maintainer workflow

1. Ask the contributor to run the free `/agent-preflight` command from the public repository before review.
2. Require the receipt to name changed files, command hooks, install steps, and secret-touching assumptions.
3. If the receipt lands in a yellow/red zone, use the paid pack's copy-paste review prompts and policy gates before merge.
4. Paste the final preflight receipt or checklist decision into the PR so future maintainers can audit why the agent-assisted change was accepted.

## Buyer trust notes

- No private repository upload is required to evaluate the fit.
- The free public command is inspectable before purchase.
- The paid pack is a downloadable checklist/prompt/template bundle, not a SaaS connection to your code.
- Support and pre-sale questions route through the public product/funnel links already shown in this repository.

## Links

- Free public repo: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>
- Live paid pack: <https://payhip.com/b/1nmxV>
- Trust/support page: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/trust-and-support.md>
