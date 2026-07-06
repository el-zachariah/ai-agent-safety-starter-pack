from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class GeminiCLICodingAgentProofTest(unittest.TestCase):
    def test_gemini_cli_proof_markers_are_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-gemini-cli-coding-agents.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("Gemini CLI coding-agent preflight proof", doc)
        self.assertIn("google-gemini/gemini-cli", doc)
        self.assertIn("Yellow or Red", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("Gemini CLI coding-agent preflight proof", readme)
        self.assertIn("docs/examples/preflight-before-gemini-cli-coding-agents.md", readme)
        self.assertIn("gemini-cli-coding-agent-proof", index)
        self.assertIn("Buy the $7 starter pack when the receipt is Yellow/Red", index)

if __name__ == "__main__":
    unittest.main()
