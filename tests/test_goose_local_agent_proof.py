import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MARKER = "deadline-proof:goose-local-agent-proof"
class CodingAgentBuyerProofTest(unittest.TestCase):
    def test_customer_proof_is_public_funnel_ready(self):
        doc=(ROOT/"docs/customer-proofs/goose-local-agent-proof.md").read_text(); readme=(ROOT/"README.md").read_text(); index=(ROOT/"index.html").read_text()
        self.assertIn(MARKER, doc); self.assertIn("aaif-goose/goose", doc); self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("Yellow", doc); self.assertIn("Red", doc); self.assertIn("docs/customer-proofs/goose-local-agent-proof.md", readme)
        self.assertIn(MARKER, index); self.assertIn("Buy the $7 starter pack", index)
if __name__ == "__main__": unittest.main()
