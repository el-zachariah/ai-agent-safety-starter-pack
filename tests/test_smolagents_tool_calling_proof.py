import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class SmolagentsToolCallingAgentsProofTest(unittest.TestCase):
    def test_named_segment_proof_and_ctas_are_present(self):
        doc = (ROOT / 'docs/examples/preflight-before-smolagents-tool-calling-agents.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')

        for marker in [
            'smolagents tool-calling preflight proof',
            'huggingface/smolagents',
            'Yellow/Red',
            'https://payhip.com/b/1nmxV',
            'No-private-code assurance',
        ]:
            self.assertIn(marker, doc)

        self.assertIn('docs/examples/preflight-before-smolagents-tool-calling-agents.md', readme)
        self.assertIn('docs/examples/preflight-before-smolagents-tool-calling-agents.md', index)
        self.assertIn('Buy trigger', index)


if __name__ == '__main__':
    unittest.main()
