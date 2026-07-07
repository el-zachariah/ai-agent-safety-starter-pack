import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DeepEvalProofTest(unittest.TestCase):
    def test_deepeval_proof_is_linked_and_has_buy_trigger(self):
        doc = ROOT / "docs/examples/preflight-before-deepeval-llm-evaluation-workflows.md"
        readme = ROOT / "README.md"
        index = ROOT / "index.html"
        for path in (doc, readme, index):
            self.assertTrue(path.exists(), path)
        doc_text = doc.read_text()
        self.assertIn("confident-ai/deepeval", doc_text)
        self.assertIn("DeepEval-specific risk map", doc_text)
        self.assertIn("https://payhip.com/b/1nmxV", doc_text)
        self.assertIn("Yellow", doc_text)
        self.assertIn("Red", doc_text)
        self.assertIn("preflight-before-deepeval-llm-evaluation-workflows.md", readme.read_text())
        self.assertIn("deepeval-llm-evaluation-proof", index.read_text())

if __name__ == "__main__":
    unittest.main()
