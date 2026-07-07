from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HeliconeLlmObservabilityProxyProofTest(unittest.TestCase):
    def test_proof_doc_and_funnel_markers(self):
        doc = (ROOT / 'docs/examples/preflight-before-helicone-llm-observability-proxy-workflows.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        for marker in [
            'Helicone LLM observability/proxy workflow preflight proof',
            'Helicone/helicone',
            'HELICONE_LLM_OBSERVABILITY_PROXY_PROOF',
            'Yellow',
            'Red',
            'buy the $7 AI Agent Safety Starter Pack',
        ]:
            self.assertIn(marker, doc)
        self.assertIn('docs/examples/preflight-before-helicone-llm-observability-proxy-workflows.md', readme)
        self.assertIn('docs/examples/preflight-before-helicone-llm-observability-proxy-workflows.md', index)
        self.assertIn('HELICONE_LLM_OBSERVABILITY_PROXY_PROOF', readme)
        self.assertIn('Get the $7 pack', index)

if __name__ == '__main__':
    unittest.main()
