import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "CLINE_AGENT_WORKFLOW_PREFLIGHT_PROOF"
PAYHIP = "https://payhip.com/b/1nmxV"
TARGET = "cline/cline"


class ClineAgentPreflightProofTest(unittest.TestCase):
    def test_doc_readme_and_landing_have_buyer_trigger(self):
        doc = (ROOT / "docs" / "cline-agent-preflight-proof.md").read_text()
        readme = (ROOT / "README.md").read_text()
        index = (ROOT / "index.html").read_text()
        for text in (doc, readme, index):
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)
        self.assertIn(TARGET, doc)
        self.assertIn("Green", doc)
        self.assertIn("Yellow", doc)
        self.assertIn("Red", doc)


if __name__ == "__main__":
    unittest.main()
