import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-langflow-agentic-flow-builders.md'
README = ROOT / "README.md"
INDEX = ROOT / "index.html"


class LangflowAgenticFlowBuilderProofTest(unittest.TestCase):
    def test_customer_proof_markers_are_present(self):
        doc = DOC.read_text()
        readme = README.read_text()
        index = INDEX.read_text()
        for marker in [
            'Langflow agentic-flow builder preflight proof',
            'Langflow visual agent/flow-builder teams',
            'langflow-ai/langflow',
            'LANGFLOW_AGENTIC_FLOW_BUILDER_PROOF',
            'https://payhip.com/b/1nmxV',
            'Buy the $7 pack when the free scan is Yellow/Red because',
        ]:
            with self.subTest(marker=marker):
                self.assertIn(marker, doc)
        self.assertIn('docs/examples/preflight-before-langflow-agentic-flow-builders.md', readme)
        self.assertIn('Langflow agentic-flow builder preflight proof', index)
        self.assertIn('Yellow/Red', doc)


if __name__ == "__main__":
    unittest.main()
