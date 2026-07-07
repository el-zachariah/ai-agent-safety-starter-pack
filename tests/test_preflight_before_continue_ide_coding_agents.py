import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "CONTINUE_IDE_CODING_AGENT_PROOF"
DOC = ROOT / "docs/examples/preflight-before-continue-ide-coding-agents.md"


class BuyerProofTest(unittest.TestCase):
    def test_proof_doc_contains_segment_and_buy_rule(self):
        text = DOC.read_text(encoding="utf-8")
        self.assertIn(MARKER, text)
        self.assertIn("continuedev/continue", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("Yellow/Red", text)

    def test_public_entry_points_link_the_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for text in (readme, index):
            self.assertIn(MARKER, text)
            self.assertIn("docs/examples/preflight-before-continue-ide-coding-agents.md", text)


if __name__ == "__main__":
    unittest.main()
