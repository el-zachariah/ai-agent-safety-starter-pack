from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-a2a-agent-protocol-workflows.md'


class A2aAgentProtocolWorkflowsProofTests(unittest.TestCase):
    def test_named_proof_doc_has_segment_and_buy_trigger(self):
        text = DOC.read_text(encoding='utf-8')
        self.assertIn('Preflight before Agent2Agent protocol workflow runs', text)
        self.assertIn('a2aproject/A2A', text)
        self.assertIn('A2A_AGENT_PROTOCOL_WORKFLOW_PROOF', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)
        for word in ('Green', 'Yellow', 'Red'):
            self.assertIn(word, text)

    def test_named_proof_linked_from_readme_and_landing_page(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('docs/examples/preflight-before-a2a-agent-protocol-workflows.md', readme)
        self.assertIn('Agent2Agent protocol workflow preflight proof', readme)
        self.assertIn('docs/examples/preflight-before-a2a-agent-protocol-workflows.md', index)
        self.assertIn('A2A_AGENT_PROTOCOL_WORKFLOW_PROOF', index)


if __name__ == '__main__':
    unittest.main()
