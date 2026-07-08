# Two-minute value check before checkout

`VALUE_CHECK_BEFORE_CHECKOUT_2026_07_08`

Use this page after the free scanner runs and before opening Payhip. It keeps the $7 decision tied to one concrete agent task instead of a vague sense that the bundle might be useful.

## Run the free scan first

```bash
git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git
cd ai-agent-safety-starter-pack
python3 agent_preflight_lite.py /path/to/repo
```

Do not share private repository contents, screenshots, order identifiers, billing details, account details, API keys, tokens, `.env` values, or secret-adjacent file contents in a public issue. Keep the scan local and copy only the color plus non-secret risk categories into your own task note.

## Buy / skip threshold

- **Green: skip the paid ZIP.** If the free scan shows zero or one low-risk item and the agent is not getting broad shell, package, workflow, MCP, browser, or deployment scope, keep the free receipt and normal review discipline.
- **Yellow: buy only if it saves one setup loop.** If the scan flags package scripts, MCP/Cursor/Claude config, workflow files, secret-adjacent paths, or a repo handoff that would take another review pass to write cleanly, the paid ZIP is reasonable when it saves that one setup loop.
- **Red: buy if the agent run needs a reusable handoff.** If the agent can run commands, edit workflows, touch deployment-adjacent config, or operate near credentials, use the paid pack for the reusable handoff, destructive-command hook pattern, demo report, and local verifier before giving the agent tool access.

## Copy-paste task note

```text
Free scan result: <Green / Yellow / Red>
Agent scope: <read-only / edit files / run shell / package scripts / MCP tools / browser / deployment-adjacent>
Why the paid ZIP is or is not needed: <one setup loop saved, reusable handoff needed, or skip because Green>
Private data stays local: yes
Decision: <skip for now / buy the $7 starter pack at https://payhip.com/b/1nmxV before this agent run>
```

Use Payhip only after the decision is Yellow/Red for a real repo run: <https://payhip.com/b/1nmxV>.
