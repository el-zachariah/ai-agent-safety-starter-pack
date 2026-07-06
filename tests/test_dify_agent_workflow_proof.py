import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-dify-agent-workflow-apps.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'

class DifyAgentWorkflowProofTest(unittest.TestCase):
    def test_doc_has_named_buyer_and_buy_trigger(self):
        text = DOC.read_text(encoding='utf-8')
        self.assertIn('Dify agent/workflow app preflight proof', text)
        self.assertIn('langgenius/dify', text)
        self.assertIn('DIFY_AGENT_WORKFLOW_PROOF', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)
        self.assertIn('Yellow/Red', text)
        self.assertIn('provider keys', text)

    def test_readme_links_dify_proof(self):
        text = README.read_text(encoding='utf-8')
        self.assertIn('docs/examples/preflight-before-dify-agent-workflow-apps.md', text)
        self.assertIn('DIFY_AGENT_WORKFLOW_PROOF', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)

    def test_landing_links_dify_proof(self):
        text = INDEX.read_text(encoding='utf-8')
        self.assertIn('docs/examples/preflight-before-dify-agent-workflow-apps.md', text)
        self.assertIn('DIFY_AGENT_WORKFLOW_PROOF', text)
        self.assertIn('Buy the $7 starter pack', text)

if __name__ == '__main__':
    unittest.main()
