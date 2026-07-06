from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-qdrant-vector-rag-agent-workflows.md"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"


class QdrantVectorRagAgentWorkflowsProofTest(unittest.TestCase):
    def test_qdrant_vector_rag_proof_markers(self):
        doc = DOC.read_text(encoding="utf-8")
        readme = README.read_text(encoding="utf-8")
        index = INDEX.read_text(encoding="utf-8")

        self.assertIn("Qdrant vector/RAG agent workflow preflight proof", doc)
        self.assertIn("qdrant/qdrant", doc)
        self.assertIn("QDRANT_VECTOR_RAG_AGENT_WORKFLOW_PROOF", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("docs/examples/preflight-before-qdrant-vector-rag-agent-workflows.md", readme)
        self.assertIn("QDRANT_VECTOR_RAG_AGENT_WORKFLOW_PROOF", readme)
        self.assertIn("Qdrant vector/RAG agent workflow preflight proof", index)
        self.assertIn("docs/examples/preflight-before-qdrant-vector-rag-agent-workflows.md", index)
        self.assertIn("QDRANT_VECTOR_RAG_AGENT_WORKFLOW_PROOF", index)


if __name__ == "__main__":
    unittest.main()
