from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class WeaveEvalTraceWorkflowsProofTest(unittest.TestCase):
    def test_proof_doc_and_funnel_markers(self):
        doc = (ROOT / 'docs/examples/preflight-before-weave-eval-trace-workflows.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        for marker in [
            'Weave eval/trace workflow preflight proof',
            'wandb/weave',
            'WEAVE_EVAL_TRACE_PROOF',
            'Yellow',
            'Red',
            'buy the $7 AI Agent Safety Starter Pack',
        ]:
            self.assertIn(marker, doc)
        self.assertIn('docs/examples/preflight-before-weave-eval-trace-workflows.md', readme)
        self.assertIn('docs/examples/preflight-before-weave-eval-trace-workflows.md', index)
        self.assertIn('WEAVE_EVAL_TRACE_PROOF', readme)
        self.assertIn('Get the $7 pack', index)

if __name__ == '__main__':
    unittest.main()
