from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MARKER = "CHECKOUT_FRICTION_HELP_2026_07_07"
HELP_DOC = ROOT / "docs" / "checkout-friction-help.md"


class CheckoutFrictionHelpTests(unittest.TestCase):
    def test_checkout_help_is_linked_before_the_proof_wall(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        trust = (ROOT / "docs" / "trust-and-support.md").read_text(encoding="utf-8")

        self.assertIn("docs/checkout-friction-help.md", readme)
        self.assertIn("docs/checkout-friction-help.md", index)
        self.assertIn("checkout-friction-help.md", trust)
        self.assertIn(MARKER, readme)
        self.assertIn(MARKER, index)
        self.assertIn(MARKER, trust)
        self.assertLess(readme.index("Checkout help without private details"), readme.index("## Recent buyer-specific proof links"))
        self.assertLess(index.index("Checkout help without private details"), index.index("deadline-github-mcp-server-workflows-proof:start"))

    def test_checkout_help_gives_public_safe_support_path(self):
        help_text = HELP_DOC.read_text(encoding="utf-8")

        self.assertIn(MARKER, help_text)
        self.assertIn("https://payhip.com/b/1nmxV", help_text)
        self.assertIn("issues/new?template=buyer-question.yml", help_text)
        self.assertIn("free scanner", help_text)
        self.assertIn("Green / Yellow / Red", help_text)
        self.assertIn("Do not paste private code", help_text)
        self.assertIn("card details", help_text)
        self.assertIn("order identifiers", help_text)
        self.assertIn("Buy the `$7` pack only when the free scan is Yellow/Red", help_text)


if __name__ == "__main__":
    unittest.main()
