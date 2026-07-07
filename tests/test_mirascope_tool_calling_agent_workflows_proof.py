from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MirascopeToolCallingAgentWorkflowsProofTest(unittest.TestCase):
    def test_customer_specific_proof_is_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-mirascope-tool-calling-agent-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")

        self.assertIn("Mirascope/mirascope", doc)
        self.assertIn("MIRASCOPE_TOOL_CALLING_AGENT_WORKFLOW_PROOF", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("Yellow", doc)
        self.assertIn("Red", doc)
        self.assertIn("docs/examples/preflight-before-mirascope-tool-calling-agent-workflows.md", readme)
        self.assertIn("MIRASCOPE_TOOL_CALLING_AGENT_WORKFLOW_PROOF", readme)
        self.assertIn("mirascope-tool-calling-agent-workflow-proof", index)
        self.assertIn("docs/examples/preflight-before-mirascope-tool-calling-agent-workflows.md", index)
        self.assertIn("MIRASCOPE_TOOL_CALLING_AGENT_WORKFLOW_PROOF", index)


if __name__ == "__main__":
    unittest.main()
