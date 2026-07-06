from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ContinueAICodeAssistantProofTest(unittest.TestCase):
    def test_continue_proof_markers_are_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-continue-ai-code-assistant.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("Continue AI code assistant preflight proof", doc)
        self.assertIn("continuedev/continue", doc)
        self.assertIn("Yellow or Red", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("Continue AI code assistant preflight proof", readme)
        self.assertIn("docs/examples/preflight-before-continue-ai-code-assistant.md", readme)
        self.assertIn("continue-ai-code-assistant-proof", index)
        self.assertIn("Buy the $7 starter pack when the receipt is Yellow/Red", index)

if __name__ == "__main__":
    unittest.main()
