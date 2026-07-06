import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class TestMagenticUiMultiAgentWebAssistant(unittest.TestCase):
    def test_doc_contains_segment_receipt_and_buy_trigger(self):
        text=(ROOT/'docs/examples/preflight-before-magentic-ui-multi-agent-web-assistants.md').read_text(encoding='utf-8')
        self.assertIn('microsoft/magentic-ui', text)
        self.assertIn('Magentic-UI multi-agent web assistant', text)
        self.assertIn('Yellow/Red buy trigger', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)
        self.assertIn('Approval gate', text)
    def test_readme_and_landing_link_the_named_proof(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        index=(ROOT/'index.html').read_text(encoding='utf-8')
        self.assertIn('docs/examples/preflight-before-magentic-ui-multi-agent-web-assistants.md', readme)
        self.assertIn('docs/examples/preflight-before-magentic-ui-multi-agent-web-assistants.md', index)
        self.assertIn('Magentic-UI multi-agent web assistant', readme)
        self.assertIn('Magentic-UI multi-agent web assistant', index)
if __name__ == '__main__': unittest.main()
