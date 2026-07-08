import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "BUILDWITHCLAUDE_MERGED_DISTRIBUTION_RECEIPT_2026_07_07"
CLOSURE_MARKER = "ROUTE_CLOSURE_HYGIENE_2026_07_07_1551"
STRICT_PLUGIN_MARKER = "STRICT_PLUGIN_ROUTE_MERGEABLE_READBACK_2026_07_07_1937"
STRICT_PLUGIN_CURRENT_HEAD_MARKER = "STRICT_PLUGIN_ROUTE_GREEN_RECHECK_2026_07_08_0142"
LIVE_DISTRIBUTION_CURRENT_MARKER = "LIVE_DISTRIBUTION_TRUST_REFRESH_2026_07_08_0412"

class PublicDistributionReceiptTest(unittest.TestCase):
    def test_receipt_doc_has_buyer_trust_evidence(self):
        text = (ROOT / "docs" / "public-distribution-receipt.md").read_text(encoding="utf-8")
        self.assertIn(MARKER, text)
        self.assertIn("https://github.com/davepoon/buildwithclaude/pull/224", text)
        self.assertIn("BUILDWITHCLAUDE_MERGED_DISTRIBUTION_RECEIPT_READBACK_2026_07_07_1501", text)
        self.assertIn("Reviewed the command content, catalog updates", text)
        self.assertIn("366e45bc3606f7fb2c5fab34f33a9dbda5878847", text)
        self.assertIn("https://github.com/trailofbits/skills-curated/pull/37", text)
        self.assertIn("license/cla", text)
        self.assertIn("https://github.com/jeremylongshore/claude-code-plugins-plus-skills/pull/964", text)
        self.assertIn("prescreen-grade", text)
        self.assertIn(STRICT_PLUGIN_MARKER, text)
        self.assertIn(STRICT_PLUGIN_CURRENT_HEAD_MARKER, text)
        self.assertIn("head `7a4239`", text)
        self.assertIn("CHANGES_REQUESTED", text)
        self.assertIn("review-progress evidence rather than an endorsement claim", text)
        self.assertIn(CLOSURE_MARKER, text)
        self.assertIn("https://github.com/wshobson/agents/pull/606", text)
        self.assertIn("closed after maintainer review", text)
        self.assertIn("no longer counted as active proof", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("Buy / skip trigger", text)

    def test_live_distribution_proof_has_current_buyer_trust_readback(self):
        text = (ROOT / "docs" / "live-distribution-proof.md").read_text(encoding="utf-8")

        self.assertIn(LIVE_DISTRIBUTION_CURRENT_MARKER, text)
        self.assertIn("2026-07-08T04:10:54-05:00", text)
        self.assertIn("fifteen tracked routes remain `OPEN` + `MERGEABLE`", text)
        self.assertIn("license/CLA status contexts", text)
        self.assertIn("7a4239ff0e3073f767cb13c5b6b2f1185780c488", text)
        self.assertIn("review-progress evidence rather than endorsement", text)

    def test_readme_and_landing_link_receipt(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(MARKER, readme)
        self.assertIn(CLOSURE_MARKER, readme)
        self.assertIn(STRICT_PLUGIN_MARKER, readme)
        self.assertIn(STRICT_PLUGIN_CURRENT_HEAD_MARKER, readme)
        self.assertIn(LIVE_DISTRIBUTION_CURRENT_MARKER, readme)
        self.assertIn("docs/public-distribution-receipt.md", readme)
        self.assertIn(MARKER, index)
        self.assertIn(CLOSURE_MARKER, index)
        self.assertIn(STRICT_PLUGIN_MARKER, index)
        self.assertIn(STRICT_PLUGIN_CURRENT_HEAD_MARKER, index)
        self.assertIn(LIVE_DISTRIBUTION_CURRENT_MARKER, index)
        self.assertIn("public-distribution-receipt", index)

    def test_parked_route_is_not_presented_as_top_buyer_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        multi_harness = (ROOT / "docs" / "proofs" / "wshobson-agents-multi-harness-preflight.md").read_text(encoding="utf-8")

        self.assertIn("Closed-route hygiene", readme)
        self.assertIn("park the closed `wshobson/agents` route as non-fit", readme)
        self.assertNotIn("**Named buyer proof:** [`docs/proofs/wshobson-agents-multi-harness-preflight.md`", readme)
        self.assertIn("parked as non-fit after maintainer review", multi_harness)
        self.assertIn("not active distribution proof", multi_harness)

if __name__ == "__main__":
    unittest.main()
