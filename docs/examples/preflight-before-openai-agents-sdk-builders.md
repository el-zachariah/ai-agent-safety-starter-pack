# Preflight before OpenAI Agents SDK builders let agents touch a repo

Marker: `OPENAI_AGENTS_SDK_BUILDERS_PROOF`

Verified public target: [openai/openai-agents-python](https://github.com/openai/openai-agents-python) — 27703 GitHub stars, updated 2026-07-07T04:38:45Z. A lightweight, powerful framework for multi-agent workflows

This proof is for teams adopting OpenAI Agents SDK builders who are close enough to agentic development to care about a cheap, concrete preflight receipt before the first unsafe command lands in a real repository.

## Why this segment should care

The risk is not the framework itself. The risk is tool-calling agents that run repository commands before a human can inspect the exact shell plan. A preflight receipt gives the maintainer a small, inspectable artifact before the agent proceeds.

## 4-minute preflight shape

1. Snapshot the exact branch, dirty files, and intended agent command.
2. Block obvious private material: `.env`, tokens, SSH keys, browser profiles, production database URLs, and customer exports.
3. Classify the command as Green / Yellow / Red.
4. Save the receipt next to the PR, issue, or handoff note so a reviewer can approve the next step without re-running the whole agent session.

## Copy-paste receipt for OpenAI Agents SDK builders

```text
OPENAI_AGENTS_SDK_BUILDERS_PROOF
Framework: openai/openai-agents-python
Agent lane: <tool-calling / multi-agent / repo-writing / deploy-hook>
Target branch: <branch>
Planned command: <exact command>
Files the agent may touch: <paths>
Secrets scan: <pass/fail + redacted reason>
Network/payment/KYC action: <none / human approval required>
Decision: Green / Yellow / Red
Reviewer: <handle>
```

## Buy / skip trigger

- Green: use the free scanner and this receipt template.
- Yellow: buy the paid bundle when OpenAI Agents SDK work moves from toy examples into CI hooks, repository writes, or customer data handling.
- Red: do not buy; stop until the command no longer touches secrets, payments, KYC, production data, or legal identity.

Paid upgrade: <https://payhip.com/b/1nmxV>
Free repo: <https://github.com/el-zachariah/ai-agent-safety-starter-pack>
