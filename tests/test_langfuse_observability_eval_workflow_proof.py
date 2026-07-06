import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LangfuseObservabilityEvalProofTest(unittest.TestCase):
    def test_langfuse_proof_doc_and_ctas_are_present(self):
        doc = (ROOT / "docs/examples/preflight-before-langfuse-observability-eval-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in ['Langfuse observability/eval pipeline preflight proof', 'Target verified: https://github.com/langfuse/langfuse', 'Buy the $7 starter pack', 'payhip.com/b/1nmxV', 'Green / Yellow / Red']:
            self.assertIn(marker, doc)
        self.assertIn("preflight-before-langfuse-observability-eval-workflows.md", readme)
        self.assertIn("langfuse-observability-proof", index)
        self.assertIn("Buy the $7 starter pack", index)

if __name__ == "__main__":
    unittest.main()
