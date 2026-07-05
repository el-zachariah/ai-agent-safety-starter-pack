# Claude Code hook preflight proof

This page is for developers already using **Claude Code hooks, TDD guardrails, MCP routing, or continuous-agent harnesses** and deciding whether a repo-safety preflight is worth adding before the agent gets tools.

It targets a concrete first-buyer segment: people who already trust local automation enough to let it run commands, but need a fast receipt before the run starts.

## The 6-minute proof

Run the free scanner before a hook/TDD/continuous-agent session:

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py examples/sample-risky-repo
python3 agent_preflight_lite.py examples/sample-risky-repo --json
```

Expected sample signal:

- **Agent instructions**: review `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, and `.cursor/rules/*` before the session inherits them.
- **MCP / Claude / Cursor config**: note configs that may route tools or context into the run.
- **Package scripts and workflows**: mark install/test/deploy commands that the agent may execute.
- **Secret-adjacent files**: exclude `.env`, `.npmrc`, `.pypirc`, SSH-key-looking paths, and other sensitive local files.
- **Risky shell patterns**: stop and review commands like `rm -rf`, `curl | sh`, `chmod 777`, `docker.sock`, and force-push language.

## Hook-session handoff

Before enabling the hook, TDD guard, or long-running agent loop, paste this tiny receipt into the task notes:

```text
Preflight result: Green / Yellow / Red
Risk buckets found: <agent instructions / MCP config / package scripts / workflows / secrets / risky shell>
Agent may run: <exact commands>
Agent must ask before: <install, delete, network, deploy, credential, workflow, MCP config changes>
Agent must not touch: <secret-adjacent files, production deploy paths, protected branches>
Upgrade trigger: if Yellow/Red and this pattern repeats, use the $7 bundle for the full template + destructive-command hook.
```

## When the $7 bundle is the practical next step

Buy the starter pack only when the free preflight finds real setup work:

- the repo has two or more risk buckets,
- a hook or continuous harness will keep state across multiple agent runs,
- package scripts, workflows, or MCP configs can be executed by the agent,
- the team wants the same report template and command guardrail every time.

If the scan is Green, keep using the free scanner. If it is Yellow/Red and the run matters, the paid bundle saves the repeated setup: full repo preflight mini, destructive-command hook examples, buyer quickstart, demo risky repo/report, templates, and verifier.

Paid bundle: <https://payhip.com/b/1nmxV>
