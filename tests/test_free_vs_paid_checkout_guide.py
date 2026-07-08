from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MARKER = "FREE_VS_PAID_CHECKOUT_GUIDE_2026_07_07_2242"
GUIDE = ROOT / "docs" / "free-vs-paid-checkout-guide.md"
README = ROOT / "README.md"
LANDING = ROOT / "index.html"


class FreeVsPaidCheckoutGuideTests(unittest.TestCase):
    def test_guide_is_linked_above_proof_wall(self):
        readme = README.read_text(encoding="utf-8")
        landing = LANDING.read_text(encoding="utf-8")
        guide = GUIDE.read_text(encoding="utf-8")

        for text in (readme, landing, guide):
            self.assertIn(MARKER, text)
            self.assertIn("Yellow/Red", text)
            self.assertIn("$7", text)

        self.assertIn("docs/free-vs-paid-checkout-guide.md", readme)
        self.assertIn("docs/free-vs-paid-checkout-guide.md", landing)
        self.assertLess(readme.index(MARKER), readme.index("## Recent buyer-specific proof links"))
        self.assertLess(landing.index(MARKER), landing.index("deadline-github-mcp-server-workflows-proof:start"))

    def test_guide_answers_free_vs_paid_without_private_details(self):
        guide = GUIDE.read_text(encoding="utf-8")

        required_phrases = [
            "Lite scanner and public docs",
            "Reusable repo preflight report template",
            "Destructive-command hook starter",
            "Demo risky repo/report plus local ZIP verifier",
            "No private repository, secrets, billing data, account details, or order identifiers",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, guide)

    def test_touched_public_copy_avoids_internal_money_ops_language(self):
        forbidden = [
            "Wealth Hunter",
            "wealth-hunter",
            "first-dollar",
            "first dollar",
            "make money",
            "revenue",
            "Dollars earned",
            "goal is to make",
        ]
        for path in (README, LANDING, GUIDE):
            text = path.read_text(encoding="utf-8")
            for phrase in forbidden:
                self.assertNotIn(phrase, text, f"{phrase!r} leaked into {path.relative_to(ROOT)}")


if __name__ == "__main__":
    unittest.main()
