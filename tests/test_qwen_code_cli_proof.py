import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class QwenCodeCliProofTest(unittest.TestCase):
    def test_qwen_code_proof_markers_are_public_funnel_ready(self):
        doc = (ROOT / 'docs/examples/preflight-before-qwen-code-cli.md').read_text()
        readme = (ROOT / 'README.md').read_text()
        index = (ROOT / 'index.html').read_text()
        for text in (doc, readme, index):
            self.assertIn('Qwen Code CLI preflight proof', text)
        self.assertIn('QwenLM/qwen-code', doc)
        self.assertIn('https://payhip.com/b/1nmxV', doc)
        self.assertIn('Yellow/Red', doc)
        self.assertIn('docs/examples/preflight-before-qwen-code-cli.md', readme)
        self.assertIn('qwen-code-cli-proof', index)

if __name__ == '__main__':
    unittest.main()
