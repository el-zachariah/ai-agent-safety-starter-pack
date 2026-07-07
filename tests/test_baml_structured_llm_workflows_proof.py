import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestFreshNamedBuyerProof(unittest.TestCase):
    def test_baml_structured_llm_workflows_deadline_markers(self):
        doc = (ROOT / 'docs/examples/preflight-before-baml-structured-llm-workflows.md').read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('baml-structured-llm-workflows-deadline-proof', doc)
        self.assertIn('BoundaryML/baml', doc)
        self.assertIn("Green / Yellow / Red", doc)
        self.assertIn('https://payhip.com/b/1nmxV', doc)
        self.assertIn('docs/examples/preflight-before-baml-structured-llm-workflows.md', readme)
        self.assertIn('BoundaryML/baml', readme)
        self.assertIn('baml-structured-llm-workflows', index)
        self.assertIn('https://payhip.com/b/1nmxV', index)

if __name__ == "__main__":
    unittest.main()
