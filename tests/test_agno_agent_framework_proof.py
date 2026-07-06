import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAYHIP = 'https://payhip.com/b/1nmxV'
MARKER = 'AGNO_AGENT_FRAMEWORK_PROOF'
BUY_MARKER = 'YELLOW_RED_BUY_TRIGGER_AGNO'
DOC = ROOT / 'docs/examples/preflight-before-agno-agent-frameworks.md'


class AgnoAgentFrameworkProofTest(unittest.TestCase):
    def test_agno_proof_doc_has_buy_trigger_and_run_ticket(self):
        text = DOC.read_text(encoding='utf-8')
        self.assertIn(MARKER, text)
        self.assertIn('Agno run-ticket receipt', text)
        self.assertIn(BUY_MARKER, text)
        self.assertIn(PAYHIP, text)
        self.assertIn('agno-agi/agno', text)

    def test_agno_proof_linked_from_readme_and_landing(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('docs/examples/preflight-before-agno-agent-frameworks.md', readme)
        self.assertIn('docs/examples/preflight-before-agno-agent-frameworks.md', index)
        self.assertIn(MARKER, readme)
        self.assertIn(MARKER, index)
        self.assertIn(PAYHIP, readme)
        self.assertIn(PAYHIP, index)


if __name__ == '__main__':
    unittest.main()
