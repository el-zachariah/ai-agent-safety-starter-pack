from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class LangGraphAgentWorkflowProofTest(unittest.TestCase):
    def test_named_proof_markers_are_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-langgraph-agent-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("LangGraph graph-agent workflow preflight proof", doc)
        self.assertIn("langchain-ai/langgraph", doc)
        self.assertIn("Yellow/Red", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("docs/examples/preflight-before-langgraph-agent-workflows.md", readme)
        self.assertIn("langgraph-agent-workflow-proof", index)
        self.assertIn("Get the $7 pack", index)

if __name__ == "__main__":
    unittest.main()
