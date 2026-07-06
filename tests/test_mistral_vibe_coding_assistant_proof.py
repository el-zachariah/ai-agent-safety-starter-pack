import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-mistral-vibe-coding-assistant.md"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"

class MistralVibeCodingAssistantProofTest(unittest.TestCase):
    def test_customer_specific_markers_are_public(self):
        doc = DOC.read_text(encoding="utf-8")
        readme = README.read_text(encoding="utf-8")
        index = INDEX.read_text(encoding="utf-8")
        for marker in [
            "mistralai/mistral-vibe",
            "Mistral Vibe coding assistant",
            "Yellow/Red",
            "https://payhip.com/b/1nmxV",
            "mistral-vibe-coding-assistant-preflight.md",
        ]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-mistral-vibe-coding-assistant.md", readme)
        self.assertIn("deadline-mistral-vibe-proof", readme)
        self.assertIn("docs/examples/preflight-before-mistral-vibe-coding-assistant.md", index)
        self.assertIn("deadline-mistral-vibe-proof", index)

if __name__ == "__main__":
    unittest.main()
