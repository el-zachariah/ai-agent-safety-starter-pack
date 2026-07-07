# Cline agent preflight proof

Marker: CLINE_AGENT_WORKFLOW_PREFLIGHT_PROOF

Verified public target: [cline/cline](https://github.com/cline/cline) — 64379 GitHub stars, updated 2026-07-07T06:37:30Z. Description observed during this pulse: Autonomous coding agent as an SDK, IDE extension, or CLI assistant..

## Who this proof is for

This proof is for Cline / VS Code agent users who want a quick, local repo-risk receipt before a Cline task runs shell commands, MCP tools, or multi-file edits in a real repository.

The problem is not whether the coding agent is useful. The first-dollar buyer fear is: “Can I prove I checked obvious repo hazards before I let the agent touch my project?” This page shows the free path and the exact point where the paid starter pack is worth buying.

## Free preflight path

1. Clone or download the free repo preview: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>.
2. Run the lite scanner against the repository before starting the agent task.
3. Save the Markdown receipt beside the PR, issue, or task handoff.
4. Paste the short receipt into the agent task so reviewers can see what was checked.

Example command:

```bash
python3 agent_preflight_lite.py /path/to/repo --format markdown --out preflight-receipt.md
```

## Cline / VS Code agent users surfaces to check first

Use this proof when the repo contains or recently changed any of these surfaces: .clinerules, .cline/, mcp.json, package.json scripts, GitHub Actions, deploy config.

For a Cline / VS Code agent users workflow, the minimum useful receipt should answer:

- Did the repo expose agent/tool permissions, MCP/tool config, shell scripts, CI, or deploy paths?
- Did the agent task touch files that can run commands after checkout, install, test, or deploy?
- Are secret-adjacent files excluded from the receipt while still flagging real credential files?
- Is the result Green, Yellow, or Red before the agent begins its edit loop?

## Buy / skip trigger

- **Green:** use the free scanner and skip the paid pack for now.
- **Yellow:** buy the $7 starter pack if you need the reusable hook, review-comment template, and copy-paste handoff receipt before letting the agent continue.
- **Red:** buy the $7 starter pack before handing the repo back to the agent or asking a maintainer to review.

Paid bundle: <https://payhip.com/b/1nmxV>

## Copy-paste handoff receipt

```text
Cline / VS Code agent users preflight receipt
Target checked: <repo path or PR URL>
Agent task: <short task>
Decision: Green / Yellow / Red
Key repo surfaces: <agent config, scripts, CI, deploy, secrets-adjacent files>
Next step: proceed / tighten task scope / run paid starter-pack hook and attach report
Proof marker: CLINE_AGENT_WORKFLOW_PREFLIGHT_PROOF
```

Shipped by Wealth Hunter / Signal Loom Works via el-zachariah on 2026-07-07T01:43:11-05:00.
