import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class StrandsAgentsSdkWorkflowsProofTest(unittest.TestCase):
    def test_proof_has_target_evidence_and_buy_trigger(self):
        proof = (ROOT / "docs/examples/preflight-before-strands-agents-sdk-workflows.md").read_text(encoding="utf-8")
        self.assertIn("strands-agents/harness-sdk", proof)
        self.assertIn("STRANDS_AGENTS_SDK_WORKFLOW_PROOF", proof)
        self.assertIn("Yellow/Red", proof)
        self.assertIn("https://payhip.com/b/1nmxV", proof)

    def test_proof_is_linked_from_buyer_surfaces(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("docs/examples/preflight-before-strands-agents-sdk-workflows.md", readme)
        self.assertIn("Strands Agents SDK workflow preflight proof", index)
        self.assertIn("strands-agents-sdk-workflow-proof", index)

if __name__ == "__main__":
    unittest.main()
