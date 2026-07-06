import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class AgentopsObservabilityEvalWorkflowsProofTest(unittest.TestCase):
    def test_public_markers(self):
        doc = (ROOT / "docs/examples/preflight-before-agentops-observability-eval-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in [
            "AgentOps observability/eval preflight proof",
            "AgentOps-AI/agentops",
            "Yellow/Red",
            "buy the $7 AI Agent Safety Starter Pack",
        ]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-agentops-observability-eval-workflows.md", readme)
        self.assertIn("docs/examples/preflight-before-agentops-observability-eval-workflows.md", index)
        self.assertIn("Get the $7 pack", index)

if __name__ == "__main__":
    unittest.main()
