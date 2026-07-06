from pathlib import Path
import unittest
class ProofTest(unittest.TestCase):
    def setUp(self):
        self.root=Path(__file__).resolve().parents[1]; self.marker="guardrails-llm-validation-workflows-proof"; self.doc_rel="docs/examples/preflight-before-guardrails-llm-validation-workflows.md"
    def test_doc_buy_trigger(self):
        doc=(self.root/self.doc_rel).read_text(encoding="utf-8")
        self.assertIn(self.marker, doc); self.assertIn("guardrails-ai/guardrails", doc); self.assertIn("Yellow/Red", doc); self.assertIn("https://payhip.com/b/1nmxV", doc)
    def test_readme_landing_links(self):
        readme=(self.root/"README.md").read_text(encoding="utf-8"); landing=(self.root/"index.html").read_text(encoding="utf-8")
        self.assertIn(self.doc_rel, readme); self.assertIn(self.marker, readme); self.assertIn(self.doc_rel, landing); self.assertIn(self.marker, landing)
if __name__=="__main__": unittest.main()
