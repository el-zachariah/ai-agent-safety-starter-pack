from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-ragflow-rag-agent-pipelines.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'

class RagflowRagAgentPipelinesProofTest(unittest.TestCase):
    def test_doc_names_verified_target_and_buy_trigger(self):
        text = DOC.read_text(encoding='utf-8')
        self.assertIn('infiniflow/ragflow', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)
        self.assertIn('Green:', text)
        self.assertIn('Yellow:', text)
        self.assertIn('Red:', text)
        self.assertIn('Buy now', text)

    def test_readme_links_the_segment_proof(self):
        text = README.read_text(encoding='utf-8')
        self.assertIn('docs/examples/preflight-before-ragflow-rag-agent-pipelines.md', text)
        self.assertIn('ragflow-rag-agent-pipelines', text)
        self.assertIn('Yellow/Red', text)

    def test_landing_page_links_the_segment_proof_and_payhip(self):
        text = INDEX.read_text(encoding='utf-8')
        self.assertIn('ragflow-rag-agent-pipelines-proof', text)
        self.assertIn('docs/examples/preflight-before-ragflow-rag-agent-pipelines.md', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)

if __name__ == '__main__':
    unittest.main()
