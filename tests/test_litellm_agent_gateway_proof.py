import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-litellm-agent-gateway.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'


class LiteLLMAgentGatewayProofTest(unittest.TestCase):
    def test_doc_has_customer_specific_buy_trigger(self):
        text = DOC.read_text()
        for marker in [
            'LiteLLM agent gateway runs',
            'BerriAI/litellm',
            'litellm_config.yaml',
            'provider routing',
            'Yellow/Red',
            'https://payhip.com/b/1nmxV',
        ]:
            self.assertIn(marker, text)

    def test_funnel_links_litellm_proof(self):
        readme = README.read_text()
        index = INDEX.read_text()
        for text in (readme, index):
            self.assertIn('LiteLLM agent gateway proof', text)
            self.assertIn('docs/examples/preflight-before-litellm-agent-gateway.md', text)


if __name__ == '__main__':
    unittest.main()
