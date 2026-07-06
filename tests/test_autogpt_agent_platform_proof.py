import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AutoGPTAgentPlatformProofTest(unittest.TestCase):
    def test_autogpt_proof_is_customer_specific_and_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-autogpt-agent-platform.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")

        self.assertIn("AutoGPT agent platform preflight proof", doc)
        self.assertIn("Significant-Gravitas/AutoGPT", doc)
        self.assertIn("AUTOGPT_AGENT_PLATFORM_PROOF", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("docs/examples/preflight-before-autogpt-agent-platform.md", readme)
        self.assertIn("AUTOGPT_AGENT_PLATFORM_PROOF", readme)
        self.assertIn("autogpt-agent-platform-proof", index)
        self.assertIn("AUTOGPT_AGENT_PLATFORM_PROOF", index)


if __name__ == "__main__":
    unittest.main()
