from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "post-purchase-verification.md"
DOC_REL = "docs/post-purchase-verification.md"
MARKER = "POST_PURCHASE_ZIP_VERIFICATION_2026_07_07"
PAYHIP = "https://payhip.com/b/1nmxV"
SUPPORT = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml"


class PostPurchaseVerificationTests(unittest.TestCase):
    def test_doc_sets_local_zip_verification_and_privacy_expectations(self):
        text = DOC.read_text(encoding="utf-8")

        for needle in [
            MARKER,
            "90-second post-purchase ZIP verification",
            "Run the included verifier",
            "Pass / pause rule",
            "Do not paste private material",
            "card details",
            SUPPORT,
            PAYHIP,
        ]:
            self.assertIn(needle, text)

    def test_public_copy_links_the_zip_verification_path(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        trust = (ROOT / "docs" / "trust-and-support.md").read_text(encoding="utf-8")

        for text in [readme, landing]:
            self.assertIn(DOC_REL, text)
            self.assertIn(MARKER, text)

        self.assertIn("post-purchase-verification.md", trust)
        self.assertIn(MARKER, trust)

        self.assertIn("Check the ZIP after purchase", landing)
        self.assertIn("90-second post-purchase ZIP verification", readme)
        self.assertIn("post-purchase ZIP verification", trust)


if __name__ == "__main__":
    unittest.main()
