import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "SKYVERN_BROWSER_AGENT_WORKFLOW_PROOF"
DOC = "docs/examples/preflight-before-skyvern-browser-agent-workflows.md"
CANONICAL = "Skyvern-AI/skyvern"

class SkyvernBrowserAgentWorkflowsProofTest(unittest.TestCase):
    def test_doc_readme_and_landing_include_buyer_trigger(self):
        doc_text = (ROOT / DOC).read_text()
        readme_text = (ROOT / "README.md").read_text()
        index_text = (ROOT / "index.html").read_text()
        for text in (doc_text, readme_text, index_text):
            self.assertIn(MARKER, text)
            self.assertIn(CANONICAL, text)
            self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("Yellow", doc_text)
        self.assertIn("Red", doc_text)
        self.assertIn(DOC, readme_text)
        self.assertIn(DOC, index_text)

if __name__ == "__main__":
    unittest.main()
