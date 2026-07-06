import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
REL = 'docs/examples/preflight-before-tabby-self-hosted-coding-assistant.md'

class TabbySelfHostedCodingAssistantProofTest(unittest.TestCase):
    def test_named_buyer_proof_is_public_funnel_ready(self):
        doc = (ROOT / REL).read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        for marker in [
            'TabbyML/tabby',
            'Self-hosted Tabby preflight receipt',
            'agent-preflight-tabby',
            'https://payhip.com/b/1nmxV',
        ]:
            self.assertIn(marker, doc)
        self.assertIn(REL, readme)
        self.assertIn('Tabby self-hosted coding assistant preflight proof', index)
        self.assertIn(REL, index)

if __name__ == '__main__':
    unittest.main()
