import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-copilotkit-in-app-ai-copilots.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'


class CopilotKitInAppAICopilotProofTest(unittest.TestCase):
    def test_doc_has_customer_specific_buy_trigger(self):
        text = DOC.read_text(encoding='utf-8')
        for marker in [
            'CopilotKit in-app AI copilot proof',
            'CopilotKit/CopilotKit',
            'COPILOTKIT_IN_APP_AI_COPILOT_PROOF',
            'Yellow/Red',
            'https://payhip.com/b/1nmxV',
            'Buy the $7 pack',
        ]:
            self.assertIn(marker, text)

    def test_funnel_links_customer_proof(self):
        readme = README.read_text(encoding='utf-8')
        index = INDEX.read_text(encoding='utf-8')
        for text in (readme, index):
            self.assertIn('CopilotKit in-app AI copilot preflight proof', text)
            self.assertIn('docs/examples/preflight-before-copilotkit-in-app-ai-copilots.md', text)
            self.assertIn('COPILOTKIT_IN_APP_AI_COPILOT_PROOF', text)


if __name__ == '__main__':
    unittest.main()
