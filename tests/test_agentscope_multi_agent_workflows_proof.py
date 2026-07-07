import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AgentscopeMultiAgentWorkflowsProofTest(unittest.TestCase):
    def test_public_buyer_proof_markers(self):
        doc = (ROOT / "docs/examples/preflight-before-agentscope-multi-agent-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")

        for expected in [
            "AGENTSCOPE_MULTI_AGENT_WORKFLOW_PROOF",
            "agentscope-ai/agentscope",
            "Yellow",
            "Red",
            "https://payhip.com/b/1nmxV",
        ]:
            self.assertIn(expected, doc)

        self.assertIn("docs/examples/preflight-before-agentscope-multi-agent-workflows.md", readme)
        self.assertIn("AGENTSCOPE_MULTI_AGENT_WORKFLOW_PROOF", readme)
        self.assertIn("AGENTSCOPE_MULTI_AGENT_WORKFLOW_PROOF", landing)
        self.assertIn("docs/examples/preflight-before-agentscope-multi-agent-workflows.md", landing)


if __name__ == "__main__":
    unittest.main()
