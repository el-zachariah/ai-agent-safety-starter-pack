# AI Agent Safety Starter Pack — free lite preflight

<!-- live-distribution-proof -->
## Live buyer proof

Before paying, verify the public distribution trail and buyer-specific trust evidence: [Live distribution proof](docs/live-distribution-proof.md). It links the open directory/marketplace PRs, free repo, support page, and the paid Payhip bundle so a first buyer can check that this is a real maintained offer rather than a cold checkout page.
<!-- /live-distribution-proof -->


A small public preview from **Signal Loom Works** for developers who let AI coding agents work inside local repos.

AI agents are useful, but a surprising number of repos contain agent instructions, MCP/Cursor/Claude settings, shell scripts, package hooks, workflow files, and secret-adjacent files that are worth checking **before** a coding agent gets tool access.

This repository includes a free lite scanner/checklist. The paid `$7` starter pack adds the full repo preflight mini, a destructive-command hook, buyer quickstart, demo risky repo, report templates, and verification scripts.

**Buy the full bundle:** https://payhip.com/b/1nmxV

**Trust/support before buying:** [`docs/trust-and-support.md`](docs/trust-and-support.md) explains who is behind the pack, what happens after purchase, the public support channel, privacy limits, and the honest buy/skip rule.

**30-second buy/skip rule:** run the free scan first. Buy the `$7` pack only when the result is Yellow/Red: two or more risk buckets, MCP/Cursor/Claude config, package scripts, secret-adjacent files, or shell commands the agent might run. If the result is Green, keep using the free lite scanner and normal review discipline.

## What the free lite scanner catches

`agent_preflight_lite.py` looks for common AI-agent workspace risk signals:

- agent instruction files such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/*`
- MCP / Claude / Cursor config files
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

<!-- deadline-aider-proof:start -->
### Aider terminal pair-programming preflight proof

Teams using [Aider](https://github.com/Aider-AI/aider)-style terminal pair-programming can now preview a concrete [Aider preflight receipt](docs/examples/preflight-before-aider-terminal-pair-programming.md) before buying. It shows what to paste into the handoff before an assistant edits files, runs tests, or touches install/build scripts in a real repo.
<!-- deadline-aider-proof:end -->

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
