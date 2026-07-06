# Preflight before Tabby self-hosted coding assistants

Customer segment: teams using [`TabbyML/tabby`](https://github.com/TabbyML/tabby) or similar self-hosted coding assistants before indexing private repositories, exposing package scripts, letting generated code touch CI workflows, or connecting agent-like IDE/server workflows near secret-adjacent files.

## Public target evidence

- Target repo: `TabbyML/tabby`
- Stars observed via GitHub API: `33682`
- Updated at: `2026-07-06T03:00:45Z`
- Description: Self-hosted AI coding assistant

This is not an endorsement by TabbyML. It is a concrete first-buyer proof for teams who already trust self-hosted AI coding assistance but need a visible repo-safety receipt before a tool sees a real codebase.

## 60-second Tabby preflight receipt

Run the free scanner before a Tabby-style assistant indexes or works near a real repository:

```bash
python3 agent_preflight_lite.py /path/to/repo --json > agent-preflight-tabby.json
python3 agent_preflight_lite.py /path/to/repo > agent-preflight-tabby.md
```

Paste this into the first Tabby rollout note or PR description:

```text
Self-hosted Tabby preflight receipt
Repo/workspace:
Tabby scope: <completion only / chat / generated edits / CI or package-script work>
Scan decision: Green / Yellow / Red
Flagged surfaces: <agent instructions, package scripts, workflows, MCP/tool configs, secret-adjacent files>
Allowed now: <read-only context / named paths / named commands>
Must ask before: <install, publish, deploy, credential, browser, cross-repo, or destructive command>
Reviewer:
Timestamp:
```

## Buy / skip trigger

- **Green:** use the free receipt and do not buy yet.
- **Yellow:** buy the [$7 starter pack](https://payhip.com/b/1nmxV) if the repo has package scripts, CI workflows, agent instructions, or secret-adjacent config and the team wants reusable handoff/report templates before rolling Tabby into more repos.
- **Red:** pause the rollout and use the paid command hook plus review template before any generated edits, install commands, deploy scripts, or credential-adjacent files enter scope.

## Why this proof matters

Self-hosted coding assistants can feel safer because they run under your own account or infrastructure. The checkout trigger is narrower: buy only when the repository scan says the assistant is about to see package/workflow/secret-adjacent surfaces where a reusable preflight receipt saves setup time.
