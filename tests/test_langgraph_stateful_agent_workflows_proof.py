import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class TestLanggraphStatefulAgentWorkflowsProof(unittest.TestCase):
    def test_named_buyer_proof_markers_are_present(self):
        doc = (ROOT / 'docs/examples/preflight-before-langgraph-stateful-agent-workflows.md').read_text()
        readme = (ROOT / "README.md").read_text()
        landing = (ROOT / "index.html").read_text()

        for marker in [
            "Preflight before LangGraph stateful agent workflows",
            "langchain-ai/langgraph",
            "Green / Yellow / Red",
            "https://payhip.com/b/1nmxV",
        ]:
            self.assertIn(marker, doc)

        self.assertIn("LangGraph stateful agent preflight", readme)
        self.assertIn("docs/examples/preflight-before-langgraph-stateful-agent-workflows.md", readme)
        self.assertIn("LangGraph stateful agent preflight", landing)
        self.assertIn("docs/examples/preflight-before-langgraph-stateful-agent-workflows.md", landing)


if __name__ == "__main__":
    unittest.main()
