import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROOF = ROOT / 'docs/examples/preflight-before-opik-observability-eval-workflows.md'


class OpikObservabilityEvalWorkflowsTest(unittest.TestCase):
    def test_proof_doc_has_named_buyer_trigger(self):
        text = PROOF.read_text(encoding='utf-8')
        self.assertIn('Opik observability/eval workflow preflight proof', text)
        self.assertIn('comet-ml/opik', text)
        self.assertIn('OPIK_OBSERVABILITY_EVAL_WORKFLOW_PROOF', text)
        self.assertIn('Yellow/Red', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)

    def test_readme_and_landing_page_expose_proof(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('Opik observability/eval workflow preflight proof', readme)
        self.assertIn('docs/examples/preflight-before-opik-observability-eval-workflows.md', readme)
        self.assertIn('OPIK_OBSERVABILITY_EVAL_WORKFLOW_PROOF', readme)
        self.assertIn('Opik observability/eval workflow preflight proof', index)
        self.assertIn('OPIK_OBSERVABILITY_EVAL_WORKFLOW_PROOF', index)
        self.assertIn('https://payhip.com/b/1nmxV', index)


if __name__ == '__main__':
    unittest.main()
