from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class N8nAIWorkflowProofTest(unittest.TestCase):
    def test_n8n_ai_workflow_proof_markers_are_public_assets(self):
        doc = (ROOT / 'docs/examples/preflight-before-n8n-ai-workflows.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        required_doc = [
            'n8n',
            'workflow automation',
            'webhook',
            'Yellow/Red',
            'https://payhip.com/b/1nmxV',
            'Buy the $7 pack',
        ]
        for marker in required_doc:
            self.assertIn(marker, doc)
        self.assertIn('docs/examples/preflight-before-n8n-ai-workflows.md', readme)
        self.assertIn('n8n AI workflow automation', readme)
        self.assertIn('n8n-ai-workflow-proof', index)
        self.assertIn('Buy the $7 starter pack', index)

if __name__ == '__main__':
    unittest.main()
