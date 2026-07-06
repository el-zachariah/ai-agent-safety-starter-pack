from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REL = "docs/examples/preflight-before-agentic-radar-security-scans.md"


class AgenticRadarSecurityScanProofTests(unittest.TestCase):
    def test_agentic_radar_proof_has_segment_and_buy_trigger(self):
        doc = (ROOT / REL).read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")

        self.assertIn("splx-ai/agentic-radar", doc)
        self.assertIn("agentic-radar-preflight.json", doc)
        self.assertIn("Yellow/Red", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn(REL, readme)
        self.assertIn("Agentic Radar security-scan preflight", index)
        self.assertIn("Get the reusable $7 workflow", index)


if __name__ == "__main__":
    unittest.main()
