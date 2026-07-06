import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAYHIP = "https://payhip.com/b/1nmxV"
DOC_REL = "docs/examples/preflight-before-mcp-agent-app-workflows.md"
MARKER = "MCP_AGENT_APP_WORKFLOW_PROOF"
TARGET = "lastmile-ai/mcp-agent"

class McpAgentAppWorkflowsProofTest(unittest.TestCase):
    def test_proof_has_target_evidence_and_buy_trigger(self):
        proof = (ROOT / DOC_REL).read_text(encoding="utf-8")
        for marker in [TARGET, MARKER, "Yellow/Red", PAYHIP, "agent-preflight-mcp-agent.md"]:
            self.assertIn(marker, proof)

    def test_proof_is_linked_from_buyer_surfaces(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(DOC_REL, readme)
        self.assertIn(MARKER, readme)
        self.assertIn("mcp-agent-app-workflow-proof", index)
        self.assertIn(DOC_REL, index)
        self.assertIn(MARKER, index)

if __name__ == "__main__":
    unittest.main()
