from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "privacy-before-checkout.md"
MARKER = "LOCAL_ONLY_PRIVACY_RECEIPT_2026_07_07"
DOC_LINK = "docs/privacy-before-checkout.md"
PUBLIC_DOC_LINK = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/privacy-before-checkout.md"


class PrivacyBeforeCheckoutTests(unittest.TestCase):
    def test_privacy_receipt_sets_local_only_boundary(self):
        text = DOC.read_text(encoding="utf-8")

        for expected in [
            MARKER,
            "Run the free scanner against your own checkout from your terminal.",
            "unzip the bundle locally and run the included verifier",
            "does not need your private repository",
            "Do **not** paste private source code",
            "card details",
            "billing data",
            "order identifiers",
            "https://payhip.com/b/1nmxV",
        ]:
            self.assertIn(expected, text)

    def test_privacy_receipt_is_linked_from_public_buyer_copy(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        trust = (ROOT / "docs" / "trust-and-support.md").read_text(encoding="utf-8")

        self.assertIn(DOC_LINK, readme)
        self.assertIn(PUBLIC_DOC_LINK, landing)
        self.assertIn("privacy-before-checkout.md", trust)
        self.assertIn(MARKER, readme)
        self.assertIn(MARKER, landing)
        self.assertIn(MARKER, trust)
        self.assertIn("Local-only privacy receipt before checkout", landing)
        self.assertIn("Private repo contents", landing)
        self.assertIn("Keep private repo details local", landing)


if __name__ == "__main__":
    unittest.main()
