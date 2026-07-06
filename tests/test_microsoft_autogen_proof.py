import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-microsoft-autogen-multi-agent-workflows.md"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"


class MicrosoftAutoGenProofTest(unittest.TestCase):
    def test_microsoft_autogen_proof_markers(self):
        doc = DOC.read_text(encoding="utf-8")
        readme = README.read_text(encoding="utf-8")
        index = INDEX.read_text(encoding="utf-8")
        self.assertIn("Microsoft AutoGen multi-agent preflight proof", doc)
        self.assertIn("microsoft/autogen", doc)
        self.assertIn("agent-preflight-autogen.md", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("Microsoft AutoGen", readme)
        self.assertIn("docs/examples/preflight-before-microsoft-autogen-multi-agent-workflows.md", readme)
        self.assertIn("Microsoft AutoGen", index)
        self.assertIn("docs/examples/preflight-before-microsoft-autogen-multi-agent-workflows.md", index)


if __name__ == "__main__":
    unittest.main()
