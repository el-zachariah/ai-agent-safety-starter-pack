from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "value-check-before-checkout.md"
README = ROOT / "README.md"
LANDING = ROOT / "index.html"
MARKER = "VALUE_CHECK_BEFORE_CHECKOUT_2026_07_08"
DOC_LINK = "docs/value-check-before-checkout.md"
PUBLIC_DOC_URL = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/value-check-before-checkout.md"


class ValueCheckBeforeCheckoutTests(unittest.TestCase):
    def test_doc_gives_public_safe_purchase_threshold(self):
        text = DOC.read_text(encoding="utf-8")

        self.assertIn(MARKER, text)
        self.assertIn("Two-minute value check before checkout", text)
        self.assertIn("Run the free scan first", text)
        self.assertIn("Green: skip the paid ZIP", text)
        self.assertIn("Yellow: buy only if it saves one setup loop", text)
        self.assertIn("Red: buy if the agent run needs a reusable handoff", text)
        self.assertIn("Do not share private repository contents", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)

    def test_doc_is_linked_before_proof_wall(self):
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
