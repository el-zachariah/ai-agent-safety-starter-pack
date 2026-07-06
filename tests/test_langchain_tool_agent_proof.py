from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class LangChainToolAgentProofTest(unittest.TestCase):
    def test_langchain_tool_agent_proof_markers_are_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-langchain-tool-agents.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("LangChain tool-agent preflight proof", doc)
        self.assertIn("langchain-ai/langchain", doc)
        self.assertIn("Yellow/Red", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("docs/examples/preflight-before-langchain-tool-agents.md", readme)
        self.assertIn("langchain-tool-agent-proof", index)
        self.assertIn("Get the $7 pack", index)

if __name__ == "__main__":
    unittest.main()
