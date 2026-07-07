import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = 'VERCEL_AI_SDK_TOOL_CALLING_APP_PROOF'
DOC = 'docs/examples/preflight-before-vercel-ai-sdk-tool-calling-apps.md'
CANONICAL = 'vercel/ai'

class VercelAiSdkToolCallingAppsTest(unittest.TestCase):
    def read(self, rel):
        return (ROOT / rel).read_text(encoding='utf-8')

    def test_proof_doc_has_verified_target_and_buy_trigger(self):
        text = self.read(DOC)
        self.assertIn(MARKER, text)
        self.assertIn(CANONICAL, text)
        self.assertIn('Green / Yellow / Red', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)

    def test_public_funnel_links_to_proof(self):
        for rel in ['README.md', 'index.html']:
            with self.subTest(rel=rel):
                text = self.read(rel)
                self.assertIn(MARKER, text)
                self.assertIn(DOC, text)

if __name__ == '__main__':
    unittest.main()
