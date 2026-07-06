import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-mastra-typescript-agent-frameworks.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'


class MastraTypescriptAgentFrameworksTest(unittest.TestCase):
    def test_doc_has_customer_specific_buy_trigger(self):
        text = DOC.read_text(encoding='utf-8')
        for marker in [
            'Mastra TypeScript agent framework preflight proof',
            'mastra-ai/mastra',
            'MASTRA_TYPESCRIPT_AGENT_FRAMEWORK_PROOF',
            'Yellow/Red',
            'https://payhip.com/b/1nmxV',
            'Buy the $7 pack',
        ]:
            self.assertIn(marker, text)

    def test_funnel_links_customer_proof(self):
        readme = README.read_text(encoding='utf-8')
        index = INDEX.read_text(encoding='utf-8')
        for text in (readme, index):
            self.assertIn('Mastra TypeScript agent framework preflight proof', text)
            self.assertIn('docs/examples/preflight-before-mastra-typescript-agent-frameworks.md', text)
            self.assertIn('MASTRA_TYPESCRIPT_AGENT_FRAMEWORK_PROOF', text)


if __name__ == '__main__':
    unittest.main()
