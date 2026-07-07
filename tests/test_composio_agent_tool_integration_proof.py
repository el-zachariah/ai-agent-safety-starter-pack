import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "COMPOSIO_AGENT_TOOL_INTEGRATION_PROOF"
PAYHIP = "https://payhip.com/b/1nmxV"
TARGET = "ComposioHQ/composio"

class ComposioAgentToolIntegrationProofTest(unittest.TestCase):
    def test_doc_readme_and_landing_have_buyer_trigger(self):
        doc = (ROOT / "docs" / "composio-agent-tool-integration-proof.md").read_text()
        readme = (ROOT / "README.md").read_text()
        index = (ROOT / "index.html").read_text()
        for text in (doc, readme, index):
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)
            self.assertIn("Yellow", text)
            self.assertIn("Red", text)
        self.assertIn(TARGET, doc)
        self.assertIn("copy-paste handoff receipt", doc)

if __name__ == "__main__":
    unittest.main()
