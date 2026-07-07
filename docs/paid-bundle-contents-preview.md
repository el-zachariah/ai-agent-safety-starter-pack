# Paid bundle contents preview

Marker: PAID_BUNDLE_CONTENTS_PREVIEW_2026_07_07

Before checkout, use this page to see exactly what the `$7` download is meant to provide. The free scanner should still be run first; buy only when the free result is Yellow/Red or when you need a reusable handoff workflow for repeated AI-agent runs.

Reference build shown here: `ai-agent-safety-starter-pack-v0.4.zip`

- SHA-256: `0b5ec15f3b45613ad4ca6f5263916e2c79d8300406c0c50db79e65b0937b945e`
- Size: `336,050` bytes
- File count: `32`
- Checkout: <https://payhip.com/b/1nmxV>
- Support path: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>

## Top-level buyer files

These are the files a buyer should expect at the top of the extracted bundle:

- `BUYER-QUICKSTART.md` — the short setup path.
- `AGENT-RUN-PREFLIGHT-CHECKLIST.md` — repeatable checklist before an AI coding agent gets repo or shell access.
- `PREFLIGHT-REPORT-TEMPLATE.md` — copyable report structure for handoffs, PR notes, or internal review.
- `RUN-PREFLIGHT.py` — wrapper for the bundled preflight runner.
- `VERIFY-BUNDLE.py` — local verification script for the downloaded ZIP contents.
- `SUPPORT-FAQ.md` — public-safe support boundaries and expected questions.
- `RELEASE-NOTES.md`, `README.md`, `cover.png`, and `cover.svg`.

## Bundled scanner

The paid ZIP includes the reusable scanner source so the buyer does not have to reconstruct the workflow from the free preview:

- `agent-repo-preflight-mini/agent_repo_preflight.py`
- `agent-repo-preflight-mini/BUYER-QUICKSTART.md`
- `agent-repo-preflight-mini/examples/sample-report.md`
- `agent-repo-preflight-mini/tests/test_agent_repo_preflight.py`
- `agent-repo-preflight-mini/LICENSE` and `README.md`

## Destructive-command hook kit

For teams granting shell access to Claude Code, Cursor, Codex-style agents, MCP-backed workflows, or local automation, the ZIP includes a starter hook kit:

- `ai-coding-safety-hook-kit/destructive_command_hook.py`
- `ai-coding-safety-hook-kit/install.sh`
- `ai-coding-safety-hook-kit/examples/claude-hook-payload-allowed.json`
- `ai-coding-safety-hook-kit/examples/claude-hook-payload-blocked.json`
- `ai-coding-safety-hook-kit/examples/claude-settings-fragment.md`
- `ai-coding-safety-hook-kit/tests/test_destructive_command_hook.py`
- `ai-coding-safety-hook-kit/LICENSE` and `README.md`

## Demo material

The bundle includes a small risky sample so the buyer can verify the scanner behavior before relying on it in a real repo:

- `demo/DEMO-REPORT.md`
- `demo/DEMO-REPORT.json`
- `demo/DEMO-TRANSCRIPT.md`
- `demo/sample-risky-repo/.env.example`
- `demo/sample-risky-repo/.github/workflows/agent.yml`
- `demo/sample-risky-repo/.mcp.json`
- `demo/sample-risky-repo/package.json`
- `demo/sample-risky-repo/scripts/deploy.sh`

## What is not included

This is not a SaaS connection, sandbox, malware scanner, compliance product, insurance policy, full security audit, or replacement for human review. It does not require uploading private repositories, secrets, credentials, card details, billing data, or customer data to Signal Loom Works.

## Pass / pause rule after checkout

After downloading, unzip locally and run the included verifier before copying files into a work repo. If the ZIP contents differ materially from the list above, or if `VERIFY-BUNDLE.py` does not run in a normal Python 3 environment, pause and use the public-safe buyer question / checkout help form without posting private code, secrets, billing data, or order identifiers.
