from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "approval-packet-before-checkout.md"
README = ROOT / "README.md"
LANDING = ROOT / "index.html"
MARKER = "APPROVAL_PACKET_BEFORE_CHECKOUT_2026_07_08"
DOC_LINK = "docs/approval-packet-before-checkout.md"
PUBLIC_DOC_URL = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/approval-packet-before-checkout.md"


class ApprovalPacketBeforeCheckoutTests(unittest.TestCase):
    def test_doc_is_public_safe_approval_packet(self):
        text = DOC.read_text(encoding="utf-8")

        self.assertIn(MARKER, text)
        self.assertIn("Approval packet before checkout", text)
        self.assertIn("Public source and free scanner: https://github.com/el-zachariah/ai-agent-safety-starter-pack", text)
        self.assertIn("Checkout link: https://payhip.com/b/1nmxV", text)
        self.assertIn("Seller/public project: Signal Loom Works", text)
        self.assertIn("Free scan result: <Green / Yellow / Red>", text)
        self.assertIn("Decision: <skip for now / buy before this agent run continues>", text)
        self.assertIn("**Green:** skip the paid ZIP", text)
        self.assertIn("**Yellow:** buy only when", text)
        self.assertIn("**Red:** buy before continuing", text)
        self.assertIn("value-check-before-checkout.md", text)
        self.assertIn("team-purchase-note.md", text)
        self.assertIn("expense-reimbursement-note.md", text)
        self.assertIn("security-review-factsheet.md", text)
        self.assertIn("paid-bundle-contents-preview.md", text)
        self.assertIn("privacy-before-checkout.md", text)

    def test_packet_is_linked_before_proof_wall(self):
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
            "revenue",
            "dollars earned",
            "goal is to make",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()

