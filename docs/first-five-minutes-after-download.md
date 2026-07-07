# First five minutes after download

Marker: FIRST_FIVE_MINUTES_AFTER_DOWNLOAD_2026_07_07

Use this page before checkout if you want to know exactly what happens after the Payhip ZIP lands on your machine. The workflow stays local: no private repository, secrets, billing details, order IDs, screenshots, or account access need to be sent to Signal Loom Works.

## The short path

After downloading the paid ZIP, work from a safe local copy of the repository you plan to scan:

```bash
unzip ai-agent-safety-starter-pack-v0.4.zip
cd ai-agent-safety-starter-pack
python3 VERIFY-BUNDLE.py
python3 RUN-PREFLIGHT.py /path/to/repo > preflight-report.md
python3 RUN-PREFLIGHT.py /path/to/repo --fail-on high
```

## What each command proves

1. `python3 VERIFY-BUNDLE.py` checks that the extracted files match the expected bundle shape and that the bundled scanner, destructive-command hook tests, demo scan, and top-level runner smoke tests pass in a normal Python 3 environment.
2. `python3 RUN-PREFLIGHT.py /path/to/repo > preflight-report.md` creates a local Markdown receipt you can paste into an issue, PR, task note, or internal handoff before an AI coding agent gets repo or shell access.
3. `python3 RUN-PREFLIGHT.py /path/to/repo --fail-on high` gives a simple stop signal for high-risk findings before the agent continues.

## How to decide after the first run

- **Green:** keep the generated report as a lightweight receipt and continue with normal review discipline.
- **Yellow:** use the paid report template and destructive-command hook if the agent will run commands, edit workflow files, or touch MCP/Cursor/Claude configuration.
- **Red:** pause the agent run, review the flagged files manually, and do not hand shell access back to the agent until the risky surfaces are handled.

## If anything does not match

If the verifier fails, the ZIP contents differ from the public preview, or the first local run is confusing, use the public-safe buyer question / checkout help form and share only:

- the free scan color or paid verifier step that stalled,
- the public page you were following,
- the non-secret error text.

Do **not** post private code, secrets, credentials, customer data, billing data, card details, account screenshots, payment-provider screenshots, or order identifiers in public issues.

Checkout: <https://payhip.com/b/1nmxV>

Public-safe help: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>

Related previews:

- Contents preview: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/paid-bundle-contents-preview.md>
- Report shape preview: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/paid-report-sample-preview.md>
- Post-purchase ZIP verification: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/post-purchase-verification.md>
