import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-coze-studio-agent-builders.md"

class CozeStudioAgentBuilderProofTest(unittest.TestCase):
    def test_doc_has_target_marker_and_paid_trigger(self):
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("coze-dev/coze-studio", text)
        self.assertIn("COZE_STUDIO_AGENT_BUILDER_PROOF", text)
        self.assertIn("Yellow/Red", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)

    def test_readme_and_landing_link_the_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("docs/examples/preflight-before-coze-studio-agent-builders.md", readme)
        self.assertIn("docs/examples/preflight-before-coze-studio-agent-builders.md", index)
        self.assertIn("COZE_STUDIO_AGENT_BUILDER_PROOF", index)

if __name__ == "__main__":
    unittest.main()
