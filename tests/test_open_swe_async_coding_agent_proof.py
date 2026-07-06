import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class OpenSweAsyncCodingAgentProofTest(unittest.TestCase):
    def test_public_markers(self):
        doc = (ROOT / "docs/examples/preflight-before-open-swe-async-coding-agents.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in [
            "Open SWE async coding-agent preflight proof",
            "langchain-ai/open-swe",
            "OPEN_SWE_ASYNC_CODING_AGENT_PROOF",
            "buy the $7 AI Agent Safety Starter Pack",
        ]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-open-swe-async-coding-agents.md", readme)
        self.assertIn("docs/examples/preflight-before-open-swe-async-coding-agents.md", index)
        self.assertIn("Get the reusable $7 workflow", index)

if __name__ == "__main__":
    unittest.main()
