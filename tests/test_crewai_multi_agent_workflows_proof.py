import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "CREWAI_MULTI_AGENT_WORKFLOW_PROOF"
DOC = ROOT / "docs/customer-proofs/crewai-multi-agent-workflows-proof.md"


class TestCrewaiMultiAgentWorkflowsProof(unittest.TestCase):
    def test_customer_proof_doc_has_checkout_trigger(self):
        text = DOC.read_text(encoding="utf-8")
        self.assertIn(MARKER, text)
        self.assertIn("crewAIInc/crewAI", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("Green / Yellow / Red", text)

    def test_readme_and_landing_link_customer_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("docs/customer-proofs/crewai-multi-agent-workflows-proof.md", readme)
        self.assertIn(MARKER + "_README", readme)
        self.assertIn("docs/customer-proofs/crewai-multi-agent-workflows-proof.md", index)
        self.assertIn(MARKER, index)


if __name__ == "__main__":
    unittest.main()
