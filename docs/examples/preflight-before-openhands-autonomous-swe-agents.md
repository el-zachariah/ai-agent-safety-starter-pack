# Preflight before OpenHands autonomous SWE agents

Use this when a team is about to let **OpenHands/OpenHands**-style agents work in a real repository. The free scanner gives a buyer a visible go/no-go receipt before the agent receives repo, shell, package-script, browser, MCP, or API-backed scope.

Target evidence checked in this pulse:

- Public repo: <https://github.com/OpenHands/OpenHands>
- Stars observed via GitHub API: `79553`
- Last updated: `2026-07-06T05:50:16Z`
- Public description: 🙌 OpenHands: AI-Driven Development

## Why this segment needs a preflight

Teams letting openhands clone, edit, run shell/package scripts, browse, or use api-backed tools inside real repos. That is exactly where a cheap preflight receipt removes the trust objection: the buyer can show what was checked, why the run is Green/Yellow/Red, and what should be approved before the agent starts changing files.

## 2-minute buyer receipt

Copy this into the issue, PR, or internal approval note before running the agent:

```text
Agent/run: OpenHands autonomous SWE agents
Repo: <repo URL>
Requested scope: repo edit + shell/package commands + optional browser/MCP/API tools
Preflight command: python3 tools/agent_preflight_lite.py --repo . --format markdown --out preflight-report.md
Decision: Green / Yellow / Red
Owner approval: <name/date or ticket>
Do not proceed if: secrets, deploy credentials, unreviewed package scripts, MCP/API tokens, browser session cookies, or destructive commands are present without explicit approval.
```

## Buy / skip trigger for the $7 pack

- **Green:** keep using the free scanner and skip the paid pack for now.
- **Yellow:** buy the $7 pack if the repo has package scripts, generated shell commands, Docker/devcontainer files, CI changes, MCP/API tool config, browser automation, or secret-adjacent files and the team needs a repeatable approval template.
- **Red:** buy or require a stronger preflight before the agent receives credentials, write access, deploy rights, production data, or long-running automation.

Paid bundle: <https://payhip.com/b/1nmxV>

## What this proof gives the buyer

- A named, relevant example for OpenHands autonomous SWE agents instead of generic safety copy.
- A copy-paste approval receipt that can be attached before the agent starts.
- A clear free-first path, with the paid bundle positioned only when the scan is Yellow/Red.
