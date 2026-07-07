import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "BUILDWITHCLAUDE_MERGED_DISTRIBUTION_RECEIPT_2026_07_07"

class PublicDistributionReceiptTest(unittest.TestCase):
    def test_receipt_doc_has_buyer_trust_evidence(self):
        text = (ROOT / "docs" / "public-distribution-receipt.md").read_text(encoding="utf-8")
        self.assertIn(MARKER, text)
        self.assertIn("https://github.com/davepoon/buildwithclaude/pull/224", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("Buy / skip trigger", text)

    def test_readme_and_landing_link_receipt(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(MARKER, readme)
        self.assertIn("docs/public-distribution-receipt.md", readme)
        self.assertIn(MARKER, index)
        self.assertIn("public-distribution-receipt", index)

if __name__ == "__main__":
    unittest.main()
