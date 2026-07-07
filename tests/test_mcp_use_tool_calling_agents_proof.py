import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-mcp-use-tool-calling-agents.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'


class TestNamedBuyerProof(unittest.TestCase):
    def test_doc_readme_and_landing_have_named_segment_markers(self):
        doc = DOC.read_text()
        readme = README.read_text()
        index = INDEX.read_text()
        self.assertIn('mcp-use-tool-calling-agents-proof', doc)
        self.assertIn('mcp-use/mcp-use', doc)
        self.assertIn('Yellow', doc)
        self.assertIn('Red', doc)
        self.assertIn('docs/examples/preflight-before-mcp-use-tool-calling-agents.md', readme)
        self.assertIn('mcp-use-tool-calling-agents-proof', readme)
        self.assertIn('mcp-use-tool-calling-agents-proof', index)
        self.assertIn('docs/examples/preflight-before-mcp-use-tool-calling-agents.md', index)


if __name__ == '__main__':
    unittest.main()
