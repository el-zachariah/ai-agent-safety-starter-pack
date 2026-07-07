# 90-second post-purchase ZIP verification

POST_PURCHASE_ZIP_VERIFICATION_2026_07_07

Use this page before relying on the paid bundle in a real repository. The bundle is designed to stay local: you do not need to send private code, secrets, logs, billing data, or repository contents to Signal Loom Works.

## What to check after downloading

1. Download the ZIP from Payhip and place it outside the repository you plan to scan.
2. Unzip it into a temporary folder.
3. Read the included buyer quickstart before copying any files into a work repo.
4. Run the included verifier from inside the extracted bundle.
5. Run the free public scanner against the sample risky repo or your own local repo to confirm the Green / Yellow / Red result makes sense before you hand tool access to an AI agent.

## Pass / pause rule

- **Pass:** the verifier runs, the quickstart is readable, and the files match the public description: repo preflight mini, destructive-command hook examples, report templates, demo risky repo/report, buyer quickstart, limitations/support notes, and verification scripts.
- **Pause and ask:** the ZIP contents do not match the public description, the verifier does not run on a normal Python 3 environment, or the checkout/download page is confusing.
- **Do not paste private material:** support questions should describe the public page, operating system, non-secret error text, and which step failed. Do not include private source code, secrets, credentials, card details, billing data, payment-provider screenshots, or order identifiers in public issues.

Support form: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>

Payhip bundle: <https://payhip.com/b/1nmxV>
