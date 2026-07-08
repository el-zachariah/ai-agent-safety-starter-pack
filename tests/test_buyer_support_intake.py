from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ISSUE_TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "buyer-question.yml"
SUPPORT_LINK = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml"
STANDING_HELP_THREAD = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/1"
PAYMENT_MARKER = "PAYMENT_FRICTION_PUBLIC_SAFE_HELP_2026_07_07_2316"


class BuyerSupportIntakeTests(unittest.TestCase):
    def test_buyer_support_intake_is_linked_from_public_copy(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        trust = (ROOT / "docs" / "trust-and-support.md").read_text(encoding="utf-8")

        self.assertIn(SUPPORT_LINK, readme)
        self.assertIn(SUPPORT_LINK, landing)
        self.assertIn(SUPPORT_LINK, trust)
        self.assertIn(STANDING_HELP_THREAD, readme)
        self.assertIn(STANDING_HELP_THREAD, landing)
        self.assertIn(STANDING_HELP_THREAD, trust)
        self.assertIn("Public-safe help thread", landing)
        self.assertIn("Buyer question / checkout help", landing)
        self.assertIn("checkout-page friction", trust)
        self.assertIn("payment-step friction", trust)
        self.assertIn(PAYMENT_MARKER, trust)
        self.assertIn("do not paste private code", trust.lower())
        self.assertIn("card details", trust)

    def test_issue_template_collects_public_safe_buyer_questions(self):
        raw = ISSUE_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("name: Buyer question or checkout help", raw)
        self.assertIn('title: "[buyer question] "', raw)
        self.assertIn("Checkout page is unavailable or confusing", raw)
        self.assertIn("Payment step will not complete (no private details)", raw)
        self.assertIn("Free scan result, if you ran it", raw)
        self.assertIn(PAYMENT_MARKER, raw)
        self.assertIn("Do not paste private repository code", raw)
        self.assertIn("card details", raw)
        self.assertIn("billing data", raw)
        self.assertIn("payment-provider screenshots", raw)
        self.assertIn("order identifiers", raw)


if __name__ == "__main__":
    unittest.main()
