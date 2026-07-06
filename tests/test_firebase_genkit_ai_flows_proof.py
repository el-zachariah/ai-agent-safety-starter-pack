import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class FirebaseGenkitAiFlowsProofTest(unittest.TestCase):
    def test_named_segment_doc_and_links_exist(self):
        doc = (ROOT / "docs/examples/preflight-before-firebase-genkit-ai-flows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in ["Firebase Genkit AI flows", "`genkit-ai/genkit`", "Stars at verification:", "defineFlow", "defineTool", "https://payhip.com/b/1nmxV", "Yellow or Red"]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-firebase-genkit-ai-flows.md", readme)
        self.assertIn("Firebase Genkit AI flows preflight", index)

if __name__ == "__main__":
    unittest.main()
