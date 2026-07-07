from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "pre-checkout-decision-receipt.md"
README = ROOT / "README.md"
LANDING = ROOT / "index.html"
MARKER = "PRECHECKOUT_DECISION_RECEIPT_2026_07_07"
DOC_LINK = "docs/pre-checkout-decision-receipt.md"
PUBLIC_DOC_URL = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/pre-checkout-decision-receipt.md"


class PreCheckoutDecisionReceiptTests(unittest.TestCase):
    def test_receipt_doc_has_public_safe_buy_skip_logic(self):
        text = DOC.read_text(encoding="utf-8")

        self.assertIn(MARKER, text)
        self.assertIn("python3 agent_preflight_lite.py /path/to/repo", text)
        self.assertIn("Agent instructions or tool config: yes/no", text)
        self.assertIn("Green: keep using the free scanner", text)
        self.assertIn("Yellow: buy the $7 pack", text)
        self.assertIn("Red: pause the agent run", text)
        self.assertIn("do not paste private code", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)

    def test_receipt_is_linked_before_proof_wall(self):
        readme = README.read_text(encoding="utf-8")
        html = LANDING.read_text(encoding="utf-8")

        self.assertIn(DOC_LINK, readme)
        self.assertIn(PUBLIC_DOC_URL, html)
        self.assertIn(MARKER, readme)
        self.assertIn(MARKER, html)
        self.assertLess(readme.index(DOC_LINK), readme.index("## Recent buyer-specific proof links"))
        self.assertLess(html.index(PUBLIC_DOC_URL), html.index("deadline-github-mcp-server-workflows-proof:start"))

    def test_public_copy_avoids_internal_operator_language(self):
        combined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [DOC, README, LANDING]
        ).lower()
        forbidden = [
            "wealth hunter",
            "wealth-hunter",
            "first-dollar",
            "first dollar",
            "make money",
            "dollars earned",
            "goal is to make",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()
