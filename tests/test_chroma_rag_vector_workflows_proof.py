import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ChromaRagVectorWorkflowsProofTest(unittest.TestCase):
    def test_chroma_rag_vector_workflows_proof_is_linked_and_has_buy_trigger(self):
        doc = ROOT / "docs/examples/preflight-before-chroma-rag-vector-workflows.md"
        readme = ROOT / "README.md"
        index = ROOT / "index.html"
        for path in (doc, readme, index):
            self.assertTrue(path.exists(), path)
        doc_text = doc.read_text()
        self.assertIn("chroma-core/chroma", doc_text)
        self.assertIn("Chroma-specific risk map", doc_text)
        self.assertIn("https://payhip.com/b/1nmxV", doc_text)
        self.assertIn("Yellow", doc_text)
        self.assertIn("Red", doc_text)
        self.assertIn("docs/examples/preflight-before-chroma-rag-vector-workflows.md", readme.read_text())
        self.assertIn("chroma-rag-vector-workflows-proof", index.read_text())
        self.assertIn("CHROMA_RAG_VECTOR_WORKFLOW_PROOF", index.read_text())

if __name__ == "__main__":
    unittest.main()
