from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-voltagent-typescript-agent-workflows.md'


class VoltAgentWorkflowProofTests(unittest.TestCase):
    def test_named_agent_workflow_proof_doc_has_segment_and_buy_trigger(self):
        text = DOC.read_text()
        self.assertIn('Preflight before VoltAgent agent workflows', text)
        self.assertIn('VoltAgent/voltagent', text)
        self.assertIn('VoltAgent agent preflight receipt', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)
        self.assertIn('Yellow', text)
        self.assertIn('Red', text)
        self.assertIn('Green', text)

    def test_named_agent_workflow_proof_linked_from_readme_and_landing_page(self):
        readme = (ROOT / 'README.md').read_text()
        index = (ROOT / 'index.html').read_text()
        marker = 'docs/examples/preflight-before-voltagent-typescript-agent-workflows.md'
        self.assertIn(marker, readme)
        self.assertIn('VoltAgent agent workflow preflight proof', readme)
        self.assertIn(marker, index)
        self.assertIn('VoltAgent agent workflow proof', index)


if __name__ == '__main__':
    unittest.main()
