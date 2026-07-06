import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class GoogleAdkAgentsProofTest(unittest.TestCase):
    def test_proof_is_linked_with_buy_trigger(self):
        doc = (ROOT / 'docs/examples/preflight-before-google-adk-agents.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('google/adk-python', doc)
        self.assertIn('deadline-google-adk-agents-proof', doc)
        self.assertIn('https://payhip.com/b/1nmxV', doc)
        self.assertIn('docs/examples/preflight-before-google-adk-agents.md', readme)
        self.assertIn('deadline-google-adk-agents-proof', readme)
        self.assertIn('google-adk-agents-proof', index)
        self.assertIn('docs/examples/preflight-before-google-adk-agents.md', index)
        self.assertIn('https://payhip.com/b/1nmxV', index)

if __name__ == '__main__':
    unittest.main()
