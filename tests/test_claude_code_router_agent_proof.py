import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ClaudeCodeRouterAgentTest(unittest.TestCase):
    def test_segment_doc_has_public_target_and_paid_trigger(self):
        doc = (ROOT / "docs/examples/preflight-before-claude-code-router.md").read_text(encoding="utf-8")
        self.assertIn("musistudio/claude-code-router", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("Yellow/Red", doc)
        self.assertIn("Not affiliated", doc)

    def test_readme_and_landing_link_segment_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("docs/examples/preflight-before-claude-code-router.md", readme)
        self.assertIn("claude-code-router-agent-proof", index)
        self.assertIn("docs/examples/preflight-before-claude-code-router.md", index)


if __name__ == "__main__":
    unittest.main()
