# Preflight before multi-harness agent marketplace installs

Audience proof target: developers discovering agent workflows through `wshobson/agents`-style multi-harness marketplaces for Claude Code, Codex CLI, Cursor, OpenCode, GitHub Copilot, and Gemini CLI.

This is not an endorsement claim from that repository. It is a concrete buyer-fit example for the same segment: a small team or maintainer about to install an agent/plugin/command from a marketplace and let it run inside a real repo.

## Why this buyer should care before checkout

A multi-harness agent stack can inherit several kinds of local context at once:

- Claude/Cursor/Codex instruction files that change behavior;
- MCP and tool configs that may expose files, APIs, or tokens;
- package scripts and workflow files the agent may edit or execute;
- shell snippets copied from plugin README files;
- long-running state when the same task hops between harnesses.

The free scanner gives that buyer a visible preflight receipt before the first tool-enabled run. The paid `$7` bundle is for the moment the receipt is Yellow/Red and the team wants the reusable handoff template, destructive-command hook, report format, and verifier rather than rebuilding them for every agent package.

## 5-minute receipt for a marketplace-installed agent

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/repo --json > /tmp/agent-preflight.json
python3 agent_preflight_lite.py /path/to/repo > /tmp/agent-preflight.txt
```

Attach this short note to the agent task before shell access:

```text
Preflight before marketplace agent run
Target agent/package: <name + source URL>
Repo checked: <repo/path>
Decision: Green / Yellow / Red
Findings: <agent instructions, MCP/tool config, package scripts, risky shell, secret-adjacent files>
May run without asking: <safe read/test commands>
Must ask before running: <install/deploy/destructive/network commands>
Must not touch: <secrets, prod configs, deployment credentials>
```

## Buy / skip trigger for this segment

Skip the paid pack when the marketplace agent is only reading a toy repo and the free scan is Green.

Buy the `$7` bundle when the scan is Yellow/Red and any of these are true:

1. the agent package asks for MCP/tool permissions;
2. a README suggests install scripts, shell aliases, or hooks;
3. the target repo has `.env`, `.npmrc`, cloud config, deployment workflows, or private package credentials;
4. multiple harnesses may run against the same repo and the team needs one shared receipt.

That is the checkout-start reason: the buyer is not buying abstract security. They are buying a repeatable handoff before a marketplace agent gets real repo access.

Paid bundle: https://payhip.com/b/1nmxV
