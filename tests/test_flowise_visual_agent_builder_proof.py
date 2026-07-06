import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-flowise-visual-agent-builder-workflows.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'


class FlowiseVisualAgentBuilderProofTest(unittest.TestCase):
    def test_customer_proof_markers_are_present(self):
        doc = DOC.read_text()
        readme = README.read_text()
        index = INDEX.read_text()
        for marker in [
            'Flowise visual agent-builder workflow preflight proof',
            'FlowiseAI/Flowise',
            'FLOWISE_VISUAL_AGENT_BUILDER_PROOF',
            'https://payhip.com/b/1nmxV',
            'Public target verified',
            'custom tool/function nodes',
            'Buy the $7 pack when the free scan is Yellow/Red because',
        ]:
            with self.subTest(marker=marker):
                self.assertIn(marker, doc)
        self.assertIn('docs/examples/preflight-before-flowise-visual-agent-builder-workflows.md', readme)
        self.assertIn('Flowise visual agent-builder workflow preflight proof', index)
        self.assertIn('FlowiseAI/Flowise', index)
        self.assertIn('FLOWISE_VISUAL_AGENT_BUILDER_PROOF', index)


if __name__ == '__main__':
    unittest.main()
