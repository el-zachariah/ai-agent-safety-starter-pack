from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "paid-bundle-contents-preview.md"
DOC_REL = "docs/paid-bundle-contents-preview.md"
MARKER = "PAID_BUNDLE_CONTENTS_PREVIEW_2026_07_07"
PAYHIP = "https://payhip.com/b/1nmxV"
SUPPORT = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml"
SHA = "0b5ec15f3b45613ad4ca6f5263916e2c79d8300406c0c50db79e65b0937b945e"


class PaidBundleContentsPreviewTests(unittest.TestCase):
    def test_doc_shows_expected_paid_zip_contents_before_checkout(self):
        text = DOC.read_text(encoding="utf-8")

        for needle in [
            MARKER,
            "ai-agent-safety-starter-pack-v0.4.zip",
            SHA,
            "File count: `32`",
            "BUYER-QUICKSTART.md",
            "AGENT-RUN-PREFLIGHT-CHECKLIST.md",
            "PREFLIGHT-REPORT-TEMPLATE.md",
            "RUN-PREFLIGHT.py",
            "VERIFY-BUNDLE.py",
            "agent-repo-preflight-mini/agent_repo_preflight.py",
            "ai-coding-safety-hook-kit/destructive_command_hook.py",
            "demo/DEMO-REPORT.md",
            "demo/sample-risky-repo/.env.example",
            "What is not included",
            "not a SaaS connection",
            "does not require uploading private repositories",
            PAYHIP,
            SUPPORT,
        ]:
            self.assertIn(needle, text)

    def test_public_funnel_links_contents_preview_before_long_proof_wall(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        trust = (ROOT / "docs" / "trust-and-support.md").read_text(encoding="utf-8")

        for text in [readme, landing, trust]:
            self.assertIn(MARKER, text)

        self.assertIn(DOC_REL, readme)
        self.assertIn(DOC_REL, landing)
        self.assertIn(DOC.name, trust)

        readme_preview_pos = readme.index(DOC_REL)
        readme_proof_pos = readme.index("## Recent buyer-specific proof links")
        landing_preview_pos = landing.index(MARKER)
        landing_proof_pos = landing.index("deadline-github-mcp-server-workflows-proof:start")

        self.assertLess(readme_preview_pos, readme_proof_pos)
        self.assertLess(landing_preview_pos, landing_proof_pos)
        self.assertIn("See ZIP contents before checkout", landing)
        self.assertIn("Bundle contents before checkout", readme)
        self.assertIn("paid bundle contents preview", trust)


if __name__ == "__main__":
    unittest.main()
