from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-stagehand-browser-agent-workflows.md"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"

class StagehandBrowserAgentWorkflowProofTest(unittest.TestCase):
    def test_doc_contains_buyer_specific_markers(self):
        text = DOC.read_text()
        for marker in [
            "Stagehand browser-agent workflow preflight proof",
            "browserbase/stagehand",
            "STAGEHAND_BROWSER_AGENT_WORKFLOW_PROOF",
            "logged-in state",
            "agent-preflight-stagehand.md",
            "https://payhip.com/b/1nmxV",
            "Green receipt",
            "Yellow receipt",
            "Red receipt",
        ]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_the_proof(self):
        readme = README.read_text()
        index = INDEX.read_text()
        self.assertIn("docs/examples/preflight-before-stagehand-browser-agent-workflows.md", readme)
        self.assertIn("STAGEHAND_BROWSER_AGENT_WORKFLOW_PROOF", readme)
        self.assertIn("docs/examples/preflight-before-stagehand-browser-agent-workflows.md", index)
        self.assertIn("Stagehand browser-agent workflow preflight proof", index)

if __name__ == "__main__":
    unittest.main()
