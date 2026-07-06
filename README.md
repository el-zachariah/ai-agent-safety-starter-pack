# AI Agent Safety Starter Pack — free lite preflight

<!-- live-distribution-proof -->
## Live buyer proof
- [Zed Agent Panel preflight proof](docs/examples/preflight-before-zed-agent-panel-workflows.md) — for teams using `zed-industries/zed`, Zed Agent Panel, or editor-native AI workflows before repo edits, package scripts, MCP connectors, shell commands, or secret-adjacent files enter scope; Yellow/Red receipts point to the $7 pack: https://payhip.com/b/1nmxV
- [BMAD agent workflow preflight proof](docs/examples/preflight-before-bmad-agent-workflows.md) — for teams using `bmad-code-org/BMAD-METHOD` or BMAD-style analyst/PM/architect/dev/QA agents before generated stories, package scripts, or repo edits enter an agent run; Yellow/Red receipts point to the $7 pack: https://payhip.com/b/1nmxV
- [Open Interpreter local code-agent preflight proof](docs/examples/preflight-before-open-interpreter-local-agents.md) — for teams letting a local interpreter read repos, run shell/Python/package commands, or work near `.env`/API/browser scope; Yellow/Red receipts point to the $7 pack: https://payhip.com/b/1nmxV
- [OpenAI Agents SDK tool-agent preflight proof](docs/examples/preflight-before-openai-agents-sdk.md) — for teams connecting tool calls, MCP servers, package scripts, or API-backed actions before granting repo scope; Yellow/Red receipts point to the $7 pack: https://payhip.com/b/1nmxV
- [Vercel AI SDK agent preflight proof](docs/examples/preflight-before-vercel-ai-sdk-agents.md) — for Next.js / AI SDK teams before tool calls, route handlers, server actions, package scripts, `.env`, or preview/deploy settings enter agent scope; Yellow/Red receipts point to the $7 pack: https://payhip.com/b/1nmxV
- [Bolt-style browser app builder preflight proof](docs/examples/preflight-before-bolt-browser-app-builders.md) — for teams using `stackblitz-labs/bolt.diy`, Bolt.new-style builders, or hosted browser agents before package scripts, `.env`, preview/deploy config, or generated shell commands run; Yellow/Red receipts point to the $7 pack: https://payhip.com/b/1nmxV

- [Claude Code plugin marketplace install proof](docs/examples/preflight-before-claude-code-plugin-marketplace.md) — for Superpowers Marketplace, Tons of Skills, Build with Claude, and other plugin-marketplace users deciding whether to buy before installing commands/hooks/skills into a real repo.
- [Qwen Code CLI preflight proof](docs/examples/preflight-before-qwen-code-cli.md) — for `QwenLM/qwen-code` / Qwen-style terminal coding-agent users deciding whether to buy before granting repo, shell, package-script, MCP/tool, or `.env` scope.
- [Replit Agent workspace preflight proof](docs/examples/preflight-before-replit-agent-workspaces.md) — for hosted workspace users checking `.replit`, `replit.nix`, package scripts, secrets, and deploy/run commands before letting an agent act.

Before paying, verify the public distribution trail and buyer-specific trust evidence: [Live distribution proof](docs/live-distribution-proof.md). It links the open directory/marketplace PRs, free repo, support page, and the paid Payhip bundle so a first buyer can check that this is a real maintained offer rather than a cold checkout page.
- [Skills-curated marketplace reviewer preflight proof](docs/examples/preflight-before-skills-curated-marketplace-review.md) — for high-trust Claude Code plugin/skill marketplace reviewers checking `.claude-plugin/`, commands, hooks, package scripts, MCP settings, or secret-adjacent files before users install; Yellow/Red receipts point to the $7 pack: https://payhip.com/b/1nmxV
<!-- /live-distribution-proof -->


A small public preview from **Signal Loom Works** for developers who let AI coding agents work inside local repos.

AI agents are useful, but a surprising number of repos contain agent instructions, MCP/Cursor/Claude settings, shell scripts, package hooks, workflow files, and secret-adjacent files that are worth checking **before** a coding agent gets tool access.

This repository includes a free lite scanner/checklist. The paid `$7` starter pack adds the full repo preflight mini, a destructive-command hook, buyer quickstart, demo risky repo, report templates, and verification scripts.

**Buy the full bundle:** https://payhip.com/b/1nmxV

**Trust/support before buying:** [`docs/trust-and-support.md`](docs/trust-and-support.md) explains who is behind the pack, what happens after purchase, the public support channel, privacy limits, and the honest buy/skip rule.

**Named buyer proof:** [`docs/proofs/wshobson-agents-multi-harness-preflight.md`](docs/proofs/wshobson-agents-multi-harness-preflight.md) shows how a team evaluating multi-harness agent catalogs such as `wshobson/agents` can use the free scan first and only buy the `$7` bundle when the repo returns Yellow/Red risk.

**30-second buy/skip rule:** run the free scan first. Buy the `$7` pack only when the result is Yellow/Red: two or more risk buckets, MCP/Cursor/Claude config, package scripts, secret-adjacent files, or shell commands the agent might run. If the result is Green, keep using the free lite scanner and normal review discipline.

## What the free lite scanner catches

`agent_preflight_lite.py` looks for common AI-agent workspace risk signals:

- agent instruction files such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`
- MCP / Claude / Cursor / GitHub Copilot / Dev Containers / Replit workspace instruction config files
- secret-adjacent files such as `.env`, `.npmrc`, `.pypirc`, `id_rsa`
- risky shell patterns such as `rm -rf`, `curl | sh`, `chmod 777`, `docker.sock`, and `force push`
- package scripts and GitHub Actions workflow files that an agent may touch

It is intentionally lightweight. It is **not** a sandbox, malware scanner, secret scanner, or security audit.


## Claude Code plugin source package

Marketplace reviewers and Claude Code users can inspect or install the free native plugin source at [`.claude-plugin/`](.claude-plugin/README.md). It packages the `/agent-preflight` command without direct paid-link spam, so third-party plugin directories can review the safety workflow from the public source repo first.

## Quick start

```bash
python3 agent_preflight_lite.py /path/to/repo
python3 agent_preflight_lite.py /path/to/repo --json
```

Want a no-risk demo first?

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py examples/sample-risky-repo
```

Example output is in [`examples/sample-report.md`](examples/sample-report.md). It now prints the same **Green / Yellow / Red** decision used by the buy/skip rule, so you can see when the `$7` workflow bundle saves setup time instead of guessing.

One-minute scorecard: [`docs/one-minute-risk-scorecard.md`](docs/one-minute-risk-scorecard.md) turns scan findings into a Green / Yellow / Red go/no-go decision before an agent gets shell access.

Red-flag matrix: [`docs/red-flag-to-action-matrix.md`](docs/red-flag-to-action-matrix.md) maps scan findings to run / ask / avoid decisions before an agent gets shell access.

Claude Code slash-command bridge: copy [`commands/agent-preflight.md`](commands/agent-preflight.md) into `.claude/commands/agent-preflight.md`, then run `/agent-preflight .` before a tool-enabled session. Setup notes: [`docs/claude-code-slash-command.md`](docs/claude-code-slash-command.md).

CrewAI multi-agent workflow proof: [`docs/examples/preflight-before-crewai-multi-agent-workflows.md`](docs/examples/preflight-before-crewai-multi-agent-workflows.md) shows the 5-minute receipt to write before a CrewAI-style crew gets tool access, package scripts, `.env` values, or API-backed execution scope.

AutoGen multi-agent workflow proof: [`docs/examples/preflight-before-autogen-agent-workflows.md`](docs/examples/preflight-before-autogen-agent-workflows.md) shows the 5-minute receipt before AutoGen-style function-calling agents inherit repo, shell, package-script, MCP, browser, or API-backed tool access.

OpenAI Agents SDK workflow proof: [`docs/examples/preflight-before-openai-agents-sdk-workflows.md`](docs/examples/preflight-before-openai-agents-sdk-workflows.md) shows the 60-second handoff receipt before SDK agents get repo files, function tools, MCP/API connectors, package scripts, or credentials.

<!-- deadline-llamaindex-agent-proof:start -->
LlamaIndex agent workflow proof: [`docs/examples/preflight-before-llamaindex-agent-workflows.md`](docs/examples/preflight-before-llamaindex-agent-workflows.md) shows the 60-second receipt before LlamaIndex-style tool, retrieval, MCP/API connector, package-script, or deployment context is handed to an agent workflow.
<!-- deadline-llamaindex-agent-proof:end -->

PR-Agent review bot proof: [`docs/examples/preflight-before-pr-agent-review-bots.md`](docs/examples/preflight-before-pr-agent-review-bots.md) shows the 60-second receipt before a PR review bot inherits pull request comments, workflow permissions, package scripts, or repo context.

Smolagents tool-running agent proof: [`docs/examples/preflight-before-smolagents-tool-agents.md`](docs/examples/preflight-before-smolagents-tool-agents.md) shows the 60-second receipt before a `CodeAgent` or Python tool-calling workflow gets repo files, package scripts, `.env`-adjacent values, browser/API tools, or shell scope.

Continuous-agent example: [`docs/continuous-agent-preflight-example.md`](docs/continuous-agent-preflight-example.md) shows a 7-minute receipt for persistent Claude Code / MCP / agent harnesses before they inherit repo context, command access, and long-running state.

Claude Code hook/TDD proof: [`docs/claude-code-hook-preflight-proof.md`](docs/claude-code-hook-preflight-proof.md) gives hook, TDD guard, MCP routing, and continuous-agent users a 6-minute preflight receipt before automation starts running commands.

MCP config preflight receipt: [`docs/mcp-config-preflight-receipt-example.md`](docs/mcp-config-preflight-receipt-example.md) shows the exact Yellow handoff for Claude Code/Cursor/MCP-server changes before an agent can read tokens, call tools, or run shell commands.

CI preflight recipe: [`docs/ci-preflight-recipe.md`](docs/ci-preflight-recipe.md) shows a copy-paste GitHub Actions step for attaching a Green / Yellow / Red preflight receipt to AI-agent pull requests.

Review comment template: [`docs/preflight-review-comment-template.md`](docs/preflight-review-comment-template.md) gives maintainers a copy-paste PR/issue comment for the scan result, allowed commands, must-ask actions, and buy/skip trigger.

Maintainer receipt example: [`docs/maintainer-preflight-receipt-example.md`](docs/maintainer-preflight-receipt-example.md) shows the exact proof a maintainer can ask for before an AI-agent PR gets shell access, including a Red sample from the included risky demo repo.

Free handoff guide: [`docs/agent-handoff-playbook.md`](docs/agent-handoff-playbook.md) shows a 10-minute flow for turning the scan into Claude Code/Codex/Cursor run rules before an agent gets tool access.

Copy-paste task prompt: [`docs/copy-paste-agent-task-prompt.md`](docs/copy-paste-agent-task-prompt.md) gives a short agent instruction block to paste after the scan and before shell access.

Upgrade decision guide: [`docs/upgrade-decision-checklist.md`](docs/upgrade-decision-checklist.md) turns the scan result into a concrete buy/skip checklist for the `$7` bundle.

## Proof for Claude Code/plugin curators

If you maintain a Claude Code plugin, slash-command, or AI-agent tools directory, start with the curator proof page: [`docs/claude-code-marketplace-proof.md`](docs/claude-code-marketplace-proof.md). It explains the exact user, the signals the free scanner catches, and why this is a small pre-tool-access utility rather than a broad security claim.

## Why this exists

Before I let an autonomous coding agent work in a repo, I want a cheap first pass that answers:

1. What instruction/config files will shape the agent's behavior?
2. Are there obvious destructive commands or risky install/deploy scripts?
3. Are there secret-adjacent files that should be excluded or protected?
4. Which files deserve a human look before agent execution?

The full starter pack turns this into a reusable preflight workflow plus a command hook that blocks obvious destructive shell commands.

Use the free scanner before you clone-and-run an unfamiliar repo, hand a backlog task to Claude Code/Codex/Cursor, enable a new MCP config, or let an agent run install/test/deploy commands.

## Upgrade trigger

Run the free lite check first. The `$7` bundle is meant for the moment the scan finds enough signals that you want a repeatable handoff instead of a one-off note:

1. capture the repo preflight result,
2. decide what the agent may read or run,
3. block obvious destructive commands with a local hook, and
4. keep a reusable report template with the repo before assigning Claude Code, Codex, Cursor, or another AI coding agent.

<!-- deadline-continue-ide-agent-proof:start -->
### Continue.dev IDE agent preflight proof

Teams using [`continuedev/continue`](https://github.com/continuedev/continue) or a similar IDE agent can preview a concrete [Continue.dev IDE agent preflight proof](docs/examples/preflight-before-continue-ide-agents.md) before exposing `.continue/` config, MCP/context providers, package scripts, and repo secrets to an agent run.
<!-- deadline-continue-ide-agent-proof:end -->

<!-- deadline-github-copilot-coding-agent-proof:start -->
### GitHub Copilot coding agent preflight proof

Teams using GitHub Copilot coding agent or repository-level `.github/copilot-instructions.md` can preview a concrete [Copilot coding agent preflight proof](docs/examples/preflight-before-github-copilot-coding-agent.md) before exposing workflow secrets, package scripts, repo instructions, or issue/PR automation scope. The free scanner now flags `copilot-instructions.md` as an agent instruction file so buyers can verify the handoff trigger before purchasing.
<!-- deadline-github-copilot-coding-agent-proof:end -->

<!-- deadline-pr-agent-review-bot-proof:start -->
### PR-Agent review bot preflight proof

Teams using PR-Agent or similar PR review bots can preview a concrete [PR-Agent review bot preflight proof](docs/examples/preflight-before-pr-agent-review-bots.md) before exposing workflow secrets, package scripts, repo instructions, comment-triggered automation, or issue/PR permissions to the bot.
<!-- deadline-pr-agent-review-bot-proof:end -->


<!-- deadline-acp-agent-proof:start -->
### Agent Client Protocol (ACP) agent preflight proof

Teams testing `agentclientprotocol/agent-client-protocol` or ACP-compatible editor agents can preview a concrete [ACP agent preflight receipt](docs/examples/preflight-before-agent-client-protocol-agents.md) before a client hands repo context, package scripts, MCP/editor config, or shell access to a coding agent.
<!-- deadline-acp-agent-proof:end -->

## Full bundle

The `$7` Payhip bundle includes:

- Agent Repo Preflight Mini
- AI Coding Safety Hook Kit
- destructive-command hook examples
- buyer quickstart
- report templates
- demo risky repo and generated demo report
- verification scripts
- support/limitations FAQ

Payhip: https://payhip.com/b/1nmxV

## License

The free lite files in this public repository are MIT licensed. The paid bundle is sold separately on Payhip.

## Buyer-fit proofs

- [Claude Code marketplace curator safety pass](docs/customer-proof-claude-code-marketplace-curators.md)

<!-- deadline-tdd-guard-proof:start -->
## Named workflow: preflight before TDD Guard

If you are installing a Claude Code enforcement hook such as TDD Guard, run the free local preflight first and keep the receipt with your first hook-enforced PR: [Preflight before TDD Guard hooks](docs/examples/preflight-before-tdd-guard.md).
<!-- deadline-tdd-guard-proof:end -->


<!-- deadline-continuous-claude-proof:start -->
## Named workflow: preflight before Continuous Claude-style loops

Running a persistent Claude Code / MCP / hook loop such as Continuous Claude? Keep a 5-minute receipt before the agent inherits shell access, repo instructions, and long-running state: [Preflight before Continuous Claude-style loops](docs/examples/preflight-before-continuous-claude.md).
<!-- deadline-continuous-claude-proof:end -->

<!-- deadline-agent-skills-proof:start -->
## Agent Skills-compatible package

Using an Agent Skills / n-skills-style workflow with Claude Code, Codex, or other AI coding agents? This repo now includes a portable [`skills/agent-safety-preflight/SKILL.md`](skills/agent-safety-preflight/SKILL.md) package so teams can install the same local preflight habit before an agent gets command access.
<!-- deadline-agent-skills-proof:end -->


<!-- deadline-multi-harness-proof:start -->
## Named workflow: preflight before multi-harness agent marketplace installs

Using a Claude Code / Codex CLI / Cursor / OpenCode / Copilot / Gemini agent marketplace such as `wshobson/agents`? Keep a 5-minute receipt before the package inherits repo instructions, tool configs, and shell access: [Preflight before multi-harness agent marketplace installs](docs/examples/preflight-before-multi-harness-agent-marketplaces.md).
<!-- deadline-multi-harness-proof:end -->

<!-- deadline-marketplace-pr-reviewer-proof:start -->
## Named workflow: preflight before accepting agent/plugin marketplace PRs

Maintaining or reviewing a Claude Code / Codex / Cursor / OpenCode / Gemini / Copilot marketplace PR? Keep a 5-minute listing-safety receipt before merging a submitted command, hook, skill, or plugin: [Preflight before accepting agent/plugin marketplace PRs](docs/examples/preflight-before-marketplace-pr-reviewers.md).
<!-- deadline-marketplace-pr-reviewer-proof:end -->

<!-- deadline-runtime-safety-proof:start -->
## Named workflow: preflight before runtime safety enforcement hooks

Evaluating a runtime safety layer for Claude Code/Codex-style agents, such as a `gensee-crate`-style hook or monitoring wrapper? Run the free preflight first so the runtime layer inherits reviewed repo instructions, MCP/tool configs, package scripts, and shell rules: [Preflight before runtime safety enforcement hooks](docs/examples/preflight-before-runtime-safety-enforcement.md).
<!-- deadline-runtime-safety-proof:end -->

### OpenHands-style autonomous repo agents proof

If your first buyer path is an OpenHands / Devin-style autonomous repo-agent workflow, use the new free proof page before starting the agent: [`docs/examples/preflight-before-openhands-autonomous-agents.md`](docs/examples/preflight-before-openhands-autonomous-agents.md). It gives a 60-second receipt, Yellow/Red buy trigger, and pasteable run-ticket note for teams deciding whether the $7 pack is needed before widening agent scope.

## Customer proof examples
- [MCP server repo preflight proof](docs/examples/preflight-before-mcp-server-repos.md) — for MCP server maintainers and buyers checking launch commands, secrets, Docker/package scripts, and client configs before attaching the server to Claude Code/Cursor/Codex.
- [CrewAI multi-agent workflow preflight proof](docs/examples/preflight-before-crewai-multi-agent-workflows.md) — for teams running multi-agent crews with local tools, package scripts, `.env` values, API calls, or write-capable workflows.
<!-- deadline-claude-action-ci-proof:start -->
## Named workflow: preflight before Claude Code GitHub Action CI runs

Using `anthropics/claude-code-action` or similar issue/PR-triggered coding automation? Run the free local preflight before granting workflow secrets, write permissions, or shell command scope: [Preflight before Claude Code GitHub Action CI runs](docs/examples/preflight-before-claude-code-action-ci.md).
<!-- deadline-claude-action-ci-proof:end -->


### Codex CLI / PR-agent preflight proof

Teams using [openai/codex](https://github.com/openai/codex)-style AI coding agents can now preview a concrete [Codex CLI preflight handoff example](docs/examples/preflight-before-codex-cli.md) before buying. It shows how to paste a Green/Yellow/Red receipt into a Codex task, constrain risky commands, and decide when the $7 paid pack is worth it.

<!-- deadline-gemini-cli-proof:start -->
### Gemini CLI terminal-agent preflight proof

Teams using [Google Gemini CLI](https://github.com/google-gemini/gemini-cli) or similar terminal AI coding agents can now preview a concrete [Gemini CLI preflight receipt example](docs/examples/preflight-before-gemini-cli.md) before buying. It shows what to paste before the agent edits files or runs shell commands, and when the $7 pack is worth it because the scan is Yellow/Red.
- [Browser-use web-agent preflight proof](docs/examples/preflight-before-browser-use-web-agents.md) — for teams running `browser-use/browser-use` or similar browser agents before repo/API credentials; Yellow/Red scan → buy the [$7 full pack](https://payhip.com/b/1nmxV).
<!-- deadline-gemini-cli-proof:end -->


<!-- deadline-e2b-code-interpreter-proof:start -->
### E2B code-interpreter agent preflight proof

Teams using [E2B](https://github.com/e2b-dev/E2B)-style code-interpreter sandboxes can now preview a concrete [E2B preflight receipt example](docs/examples/preflight-before-e2b-code-interpreter-agents.md) before buying. It shows what to check before an agent receives repo files, sandbox templates, env vars, package scripts, or API-backed execution scope.
- [Goose/local AI-agent preflight proof](docs/examples/preflight-before-goose-local-ai-agent.md) — for Block Goose / MCP / shell-enabled local agents before repo, env, extension, or package-script scope.
<!-- deadline-e2b-code-interpreter-proof:end -->

<!-- deadline-opencode-proof:start -->
### OpenCode terminal-agent preflight proof

Teams using [OpenCode](https://github.com/anomalyco/opencode)-style terminal coding agents can now preview a concrete [OpenCode preflight receipt example](docs/examples/preflight-before-opencode-terminal-agents.md) before buying. It shows what to paste before the agent edits files, runs tests, or touches package/workflow scripts, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-opencode-proof:end -->

### VS Code agent extension preflight proof

Teams using [Cline](https://github.com/cline/cline), Roo Code, or similar VS Code agent extensions can now preview a concrete [editor-agent preflight example](docs/examples/preflight-before-vscode-agent-extensions.md) before buying. It shows how to paste a risk receipt into the agent chat, constrain terminal/MCP/editor access, and decide when the $7 paid pack is worth it.

<!-- deadline-cursor-rules-proof:start -->
### Cursor rules / background-agent preflight proof

Teams using Cursor with `.cursorrules`, `.cursor/rules/*`, background agents, or repo-level rule packs can now preview a concrete [Cursor rules preflight receipt](docs/examples/preflight-before-cursor-rules-background-agents.md) before buying. It shows what to review before a Cursor assistant inherits project instructions, MCP/tool config, package scripts, or broad edit/test scope.
<!-- deadline-cursor-rules-proof:end -->

<!-- deadline-roo-code-proof:start -->
### Roo Code agent-team preflight proof

Teams using [Roo Code](https://github.com/RooCodeInc/Roo-Code) as an in-editor agent team can now preview a concrete [Roo Code preflight receipt](docs/examples/preflight-before-roo-code-agent-teams.md) before buying. It shows what to check before auto-approval, terminal commands, MCP/tools, package scripts, or deployment-adjacent files enter the session, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-roo-code-proof:end -->

<!-- deadline-aider-proof:start -->
### Aider terminal pair-programming preflight proof

Teams using [Aider](https://github.com/Aider-AI/aider)-style terminal pair-programming can now preview a concrete [Aider preflight receipt](docs/examples/preflight-before-aider-terminal-pair-programming.md) before buying. It shows what to paste into the handoff before an assistant edits files, runs tests, or touches install/build scripts in a real repo.
<!-- deadline-aider-proof:end -->


<!-- deadline-pydantic-ai-proof:start -->
### Pydantic AI production-agent preflight proof

Teams using [Pydantic AI](https://github.com/pydantic/pydantic-ai)-style typed Python agents can now preview a concrete [Pydantic AI preflight receipt](docs/examples/preflight-before-pydantic-ai-agents.md) before buying. It shows what to check before toolsets, dependency changes, MCP/API connectors, env vars, or package scripts enter a production agent run, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-pydantic-ai-proof:end -->

<!-- deadline-swe-agent-proof:start -->
### SWE-agent autonomous patch preflight proof

Teams using [SWE-agent](https://github.com/SWE-agent/SWE-agent)-style autonomous issue-to-patch workflows can now preview a concrete [SWE-agent preflight receipt](docs/examples/preflight-before-swe-agent-autonomous-patches.md) before buying. It shows what to paste into the run ticket before the agent edits files, runs tests, or touches package/workflow scripts in a real repo.
<!-- deadline-swe-agent-proof:end -->

<!-- deadline-langgraph-proof:start -->
### LangGraph stateful-agent preflight proof

Teams using [LangGraph](https://github.com/langchain-ai/langgraph)-style stateful agents can now preview a concrete [LangGraph preflight receipt](docs/examples/preflight-before-langgraph-stateful-agents.md) before buying. It shows what to check before graph nodes, tool calls, checkpoint stores, package scripts, MCP/API connectors, or deployment config enter an agent run, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-langgraph-proof:end -->

<!-- deadline-openhands-proof:start -->
### OpenHands task-branch preflight proof

Teams using [OpenHands](https://github.com/OpenHands/OpenHands)-style autonomous software-engineering agents can now preview a concrete [OpenHands task-branch preflight receipt](docs/examples/preflight-before-openhands-task-branches.md) before buying. It shows what to check before an agent receives branch, shell, package-script, CI, or MCP/tooling scope, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-openhands-proof:end -->

<!-- deadline-mastra-proof:start -->
### Mastra TypeScript agent preflight proof

Teams using [Mastra](https://github.com/mastra-ai/mastra)-style TypeScript agents can now preview a concrete [Mastra preflight receipt](docs/examples/preflight-before-mastra-typescript-agents.md) before buying. It shows what to check before tools, package scripts, MCP/API connectors, memory/storage config, or deployment secrets enter an agent run, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-mastra-proof:end -->

<!-- deadline-devcontainer-proof:start -->
### Dev Containers / Codespaces agent preflight proof

Teams using [Dev Containers](https://github.com/devcontainers/spec), GitHub Codespaces, or containerized coding-agent workspaces can preview a concrete [Dev Containers / Codespaces preflight receipt](docs/examples/preflight-before-devcontainer-codespaces-agents.md) before buying. It shows what to check before `.devcontainer/devcontainer.json`, lifecycle commands, mounts, forwarded ports, package scripts, or repo write access enter an agent run, plus the Yellow/Red trigger for the $7 workflow bundle. The free scanner now flags `.devcontainer/` and `devcontainer.json` as agent/workflow config.
<!-- deadline-devcontainer-proof:end -->

### Curated Claude skill/plugin marketplace preflight proof

Teams browsing high-trust skill/plugin marketplaces such as [`trailofbits/skills-curated`](https://github.com/trailofbits/skills-curated) or [`numman-ali/n-skills`](https://github.com/numman-ali/n-skills) can now preview a concrete [curated Claude skill marketplace preflight proof](docs/examples/preflight-before-curated-claude-skill-marketplaces.md) before enabling a skill in a real repo. It gives a 60-second receipt, named repo-risk checks, and the Yellow/Red trigger for the $7 workflow bundle.

<!-- deadline-ruflo-swarm-proof:start -->
### Ruflo / Claude Flow-style swarm preflight proof

Teams using [Ruflo](https://github.com/ruvnet/ruflo) or a similar Claude Code / Codex / Hermes multi-agent swarm can now preview a concrete [swarm preflight receipt](docs/examples/preflight-before-ruflo-agent-swarms.md) before buying. It shows what to freeze before multiple workers inherit repo instructions, MCP/tool config, shell scope, memory/checkpoints, package scripts, or secret-adjacent files.
<!-- deadline-ruflo-swarm-proof:end -->

## Buyer proof for named workflows

- [MCP server maintainer proof](docs/mcp-server-maintainer-proof.md) — buy/skip criteria for MCP server maintainers considering the $5 pack after a yellow/red agent preflight.


## Buyer proof: SuperClaude command frameworks

- [SuperClaude command framework preflight proof](docs/examples/preflight-before-superclaude-command-frameworks.md) — for teams installing command/persona/MCP frameworks before Claude Code gets repo, shell, package-script, or secrets-adjacent scope.

<!-- deadline-semantic-kernel-proof:start -->
### Semantic Kernel agent framework preflight proof

Teams using [Semantic Kernel](https://github.com/microsoft/semantic-kernel)-style agents, planners, plugins, memory connectors, or tool-calling workflows can now preview a concrete [Semantic Kernel preflight receipt](docs/examples/preflight-before-semantic-kernel-agents.md) before buying. It shows what to check before repo context, package scripts, API connectors, or secret-adjacent config enter an agent run, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-semantic-kernel-proof:end -->

<!-- deadline-composio-tool-agent-proof:start -->
### Composio tool-integration agent preflight proof

Teams wiring [Composio](https://github.com/ComposioHQ/composio)-style toolkits, MCP connectors, auth-backed actions, or sandboxed workbenches into AI agents can now preview a concrete [Composio tool-agent preflight receipt](docs/examples/preflight-before-composio-tool-agents.md) before buying. It shows what to freeze before repo context, API tools, package scripts, or credential-adjacent files enter an agent run, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-composio-tool-agent-proof:end -->

### Dify / Flowise low-code agent builder proof

Teams using Dify, Flowise, or similar visual agent builders still expose real repo, API, `.env`, webhook, database, and deployment scope once a workflow leaves the demo sandbox. Use the [low-code agent builder preflight example](docs/examples/preflight-before-low-code-agent-builders.md) to decide when a visual workflow is safe to run and when the $7 checklist/templates are the faster path.



## Buyer-specific preflight examples

- [Cline autonomous VS Code agent preflight](docs/examples/preflight-before-cline-autonomous-vscode-agents.md) — named proof for teams letting Cline edit files, run commands, or use MCP tools before buying the starter pack.

### Named buyer proof: n8n AI workflow automation

- [n8n AI workflow preflight proof](docs/examples/preflight-before-n8n-ai-workflows.md) — for teams using self-hosted workflow automation, webhooks, credentials, custom code nodes, or low-code AI workflows before granting agent/repo/API scope. Buy the [$7 starter pack](https://payhip.com/b/1nmxV) when the scan is Yellow/Red; skip it when the workflow has no real credentials or repo access.


## Customer-specific proof examples
- [Agent observability and eval pipeline preflight proof](docs/examples/preflight-before-agent-observability-eval-pipelines.md) - for Langfuse, Phoenix, and eval teams that need a before-run repo-scope receipt before traced agent runs.


<!-- deadline-humanlayer-agent-approval-proof:start -->
### HumanLayer-style agent approval preflight proof

Teams using [HumanLayer](https://github.com/humanlayer/humanlayer)-style human-in-the-loop approvals for Claude Code, Codex, OpenCode, or other coding agents can now preview a concrete [HumanLayer approval preflight receipt](docs/examples/preflight-before-humanlayer-agent-approval-workflows.md) before approving shell commands, package scripts, MCP/API actions, or repo edits. It gives the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-humanlayer-agent-approval-proof:end -->

<!-- deadline-vercel-ai-sdk-proof:start -->
### Vercel AI SDK tool-calling agent preflight proof

Teams using [Vercel AI SDK](https://github.com/vercel/ai)-style TypeScript/Next.js agents can now preview a concrete [Vercel AI SDK preflight receipt](docs/examples/preflight-before-vercel-ai-sdk-agents.md) before buying. It shows what to check before tool calls, route handlers, server actions, package scripts, `.env`, MCP/API connectors, or preview/deploy settings enter an agent run, plus the Yellow/Red trigger for the $7 workflow bundle.
<!-- deadline-vercel-ai-sdk-proof:end -->
