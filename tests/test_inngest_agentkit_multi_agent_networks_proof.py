import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "INNGEST_AGENTKIT_MULTI_AGENT_NETWORK_PROOF"
PAYHIP = "https://payhip.com/b/1nmxV"
TARGET = "inngest/agent-kit"
DOC = "docs/examples/preflight-before-inngest-agentkit-multi-agent-networks.md"

class InngestAgentKitMultiAgentNetworkProofTest(unittest.TestCase):
    def test_doc_readme_and_landing_have_buyer_trigger(self):
        doc = (ROOT / DOC).read_text()
        readme = (ROOT / "README.md").read_text()
        index = (ROOT / "index.html").read_text()
        for text in (doc, readme, index):
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)
            self.assertIn("Yellow", text)
            self.assertIn("Red", text)
        self.assertIn(TARGET, doc)
        self.assertIn("copy-paste handoff receipt", doc.lower())
        self.assertIn(DOC, readme)
        self.assertIn(DOC, index)

if __name__ == "__main__":
    unittest.main()
