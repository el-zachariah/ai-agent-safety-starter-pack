from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-openai-agents-sdk-builders.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'

class OpenaiAgentsSdkBuildersProofTest(unittest.TestCase):
    def test_segment_proof_markers_are_linked(self):
        doc = DOC.read_text()
        readme = README.read_text()
        index = INDEX.read_text()
        self.assertIn('OPENAI_AGENTS_SDK_BUILDERS_PROOF', doc)
        self.assertIn('openai/openai-agents-python', doc)
        self.assertIn('https://payhip.com/b/1nmxV', doc)
        self.assertIn('docs/examples/preflight-before-openai-agents-sdk-builders.md', readme)
        self.assertIn('docs/examples/preflight-before-openai-agents-sdk-builders.md', index)
        self.assertIn('OPENAI_AGENTS_SDK_BUILDERS_PROOF', readme + index)

if __name__ == '__main__':
    unittest.main()
