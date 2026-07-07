# Preflight before curated Claude skill/plugin marketplace installs

Audience proof target: developers browsing `trailofbits/skills-curated`, `numman-ali/n-skills`, or similar curated Claude Code skill/plugin marketplaces before installing a skill into a real repository.

This is not an endorsement claim from those projects. It is a buyer-fit proof for the same practical buyer segment: a team trusts a curated marketplace enough to try a skill, but still needs a fast local receipt before that skill or agent harness inherits repo files, package scripts, MCP/tool config, and credentials-adjacent context.

## Why curated does not mean ready-to-run

A curated skill list can reduce source-discovery risk, but it does not know the target repository. Before a Claude Code skill/plugin/command runs against a private or production-adjacent repo, check for:

- `CLAUDE.md`, `AGENTS.md`, `.claude/skills/`, `.claude/settings.json`, and repo-specific instruction files;
- `.mcp.json`, MCP server config, browser/API tools, or extension settings that widen tool reach;
- `package.json` scripts, workflow files, install hooks, or shell snippets copied from a plugin README;
- `.env.example`, cloud config, deployment files, or private package registry hints;
- cross-harness handoff risk when the same repo also uses Cursor, Codex CLI, OpenCode, Gemini CLI, or GitHub Copilot agents.

That is the checkout-start trust question: the buyer is not asking whether the marketplace is reputable; they are asking whether this particular repo is safe enough for the next agent run.

## 60-second receipt before enabling a curated skill

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/repo --json > /tmp/agent-preflight-curated-skills.json
python3 agent_preflight_lite.py /path/to/repo > /tmp/agent-preflight-curated-skills.txt
```

Paste this into the agent task or PR before enabling the skill:

```text
Curated skill/plugin preflight receipt
Source marketplace: <trailofbits/skills-curated, n-skills, or other URL>
Skill/plugin/command: <name + source URL>
Repo checked: <repo/path>
Decision: Green / Yellow / Red
Findings: <instructions, MCP/tool config, package scripts, secret-adjacent files, workflow/deploy files>
May run without asking: <safe read/test commands>
Must ask first: <install, network, deploy, destructive, credential-touching, or broad write commands>
Must not touch: <secrets, production config, payment/customer data, release credentials>
```

## Buy / skip trigger for this segment

Skip the paid pack when the curated skill only reads a toy repo and the free scan is Green.

Buy the `$7` bundle when the scan is Yellow/Red and the curated skill will run in a real repo, especially if it can install packages, edit scripts, call MCP/API tools, or hand work to another agent harness. The paid pack turns the one-off note into the reusable report template, destructive-command hook pattern, buyer quickstart, demo risky repo, and verifier so a team can reuse the same handoff before every skill install.

Paid bundle: https://payhip.com/b/1nmxV
