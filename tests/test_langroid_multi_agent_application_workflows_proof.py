from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class LangroidMultiAgentApplicationWorkflowsProofTest(unittest.TestCase):
    def test_customer_proof_markers(self):
        doc = (ROOT / 'docs/examples/preflight-before-langroid-multi-agent-application-workflows.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        for value in ['Langroid multi-agent application workflow preflight proof', 'LANGROID_MULTI_AGENT_APPLICATION_WORKFLOW_PROOF', 'langroid/langroid', 'Green / Yellow / Red', 'https://payhip.com/b/1nmxV']:
            self.assertIn(value, doc)
        self.assertIn('docs/examples/preflight-before-langroid-multi-agent-application-workflows.md', readme)
        self.assertIn('LANGROID_MULTI_AGENT_APPLICATION_WORKFLOW_PROOF', readme)
        self.assertIn('docs/examples/preflight-before-langroid-multi-agent-application-workflows.md', index)
        self.assertIn('LANGROID_MULTI_AGENT_APPLICATION_WORKFLOW_PROOF', index)
        self.assertIn('Get the $7 pack', index)

if __name__ == '__main__':
    unittest.main()
