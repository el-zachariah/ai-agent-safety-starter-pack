import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ActivepiecesAiAutomationWorkflowsProofTest(unittest.TestCase):
    def test_segment_doc_has_paid_trigger(self):
        text = (ROOT / "docs/examples/preflight-before-activepieces-ai-automation-workflows.md").read_text(encoding="utf-8")
        self.assertIn("ACTIVEPIECES_AI_AUTOMATION_PROOF", text)
        self.assertIn("activepieces/activepieces", text)
        self.assertIn("Green", text)
        self.assertIn("Yellow", text)
        self.assertIn("Red", text)
        self.assertIn("buy the $7 AI Agent Safety Starter Pack only after a Yellow/Red receipt", text)
    def test_readme_and_landing_link_segment_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        for text in (readme, landing):
            self.assertIn("ACTIVEPIECES_AI_AUTOMATION_PROOF", text)
            self.assertIn("docs/examples/preflight-before-activepieces-ai-automation-workflows.md", text)
if __name__ == "__main__": unittest.main()
