import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC_REL = 'docs/examples/preflight-before-crush-terminal-agents.md'
MARKER = 'CRUSH_TERMINAL_AGENT_PROOF'
PAYHIP = 'https://payhip.com/b/1nmxV'

class CrushTerminalAgentProofTest(unittest.TestCase):
    def test_doc_is_specific_and_has_checkout_trigger(self):
        text = (ROOT / DOC_REL).read_text(encoding='utf-8')
        for marker in [MARKER, 'charmbracelet/crush', 'Crush terminal coding agents', '60-second Crush handoff receipt', 'Yellow or Red', PAYHIP]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_the_proof(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        landing = (ROOT / 'index.html').read_text(encoding='utf-8')
        for text in [readme, landing]:
            self.assertIn(DOC_REL, text)
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)
        self.assertIn('Crush terminal coding-agent preflight proof', readme)
        self.assertIn('New: Crush terminal coding-agent preflight proof', landing)

if __name__ == '__main__':
    unittest.main()
