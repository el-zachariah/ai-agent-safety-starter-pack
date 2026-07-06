from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CrewAIMultiAgentWorkflowProofTest(unittest.TestCase):
    def test_crewai_proof_markers_are_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-crewai-multi-agent-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("CrewAI multi-agent workflow preflight proof", doc)
        self.assertIn("crewAIInc/crewAI", doc)
        self.assertIn("Yellow or Red", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("CrewAI multi-agent workflow preflight proof", readme)
        self.assertIn("docs/examples/preflight-before-crewai-multi-agent-workflows.md", readme)
        self.assertIn("crewai-multi-agent-workflow-proof", index)
        self.assertIn("Buy the $7 starter pack when the receipt is Yellow/Red", index)

if __name__ == "__main__":
    unittest.main()
