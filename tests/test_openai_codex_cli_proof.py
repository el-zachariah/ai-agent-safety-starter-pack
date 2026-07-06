import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class OpenAICodexCLIProofTest(unittest.TestCase):
    def test_openai_codex_cli_proof_markers(self):
        doc = (ROOT / 'docs/examples/preflight-before-openai-codex-cli.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')

        required = [
            'OpenAI Codex CLI preflight proof',
            'openai/codex',
            'Yellow/Red',
            'buy the $7 AI Agent Safety Starter Pack',
        ]
        for marker in required:
            self.assertIn(marker, doc)
        self.assertIn('docs/examples/preflight-before-openai-codex-cli.md', readme)
        self.assertIn('docs/examples/preflight-before-openai-codex-cli.md', index)
        self.assertIn('Get the $7 pack', index)


if __name__ == '__main__':
    unittest.main()
