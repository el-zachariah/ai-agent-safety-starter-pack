import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AnythingllmAgentWorkspacesProofTest(unittest.TestCase):
    def test_public_buyer_proof_markers(self):
        doc = (ROOT / "docs/examples/preflight-before-anythingllm-agent-workspaces.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        for expected in ["ANYTHINGLLM_AGENT_WORKSPACE_PROOF", "Mintplex-Labs/anything-llm", "Yellow", "Red", "https://payhip.com/b/1nmxV"]:
            self.assertIn(expected, doc)
        self.assertIn("docs/examples/preflight-before-anythingllm-agent-workspaces.md", readme)
        self.assertIn("ANYTHINGLLM_AGENT_WORKSPACE_PROOF", readme)
        self.assertIn("docs/examples/preflight-before-anythingllm-agent-workspaces.md", landing)
        self.assertIn("ANYTHINGLLM_AGENT_WORKSPACE_PROOF", landing)


if __name__ == "__main__":
    unittest.main()
