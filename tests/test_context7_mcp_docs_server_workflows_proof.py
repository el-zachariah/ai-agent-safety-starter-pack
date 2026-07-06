import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class TestContext7McpDocsServerWorkflowsProof(unittest.TestCase):
    def test_named_buyer_proof_markers_are_present(self):
        doc = (ROOT / 'docs/examples/preflight-before-context7-mcp-docs-server-workflows.md').read_text()
        readme = (ROOT / "README.md").read_text()
        landing = (ROOT / "index.html").read_text()

        for marker in [
            "Preflight before Context7 MCP docs-server workflows",
            "upstash/context7",
            "Green / Yellow / Red",
            "https://payhip.com/b/1nmxV",
        ]:
            self.assertIn(marker, doc)

        self.assertIn("Context7 MCP docs-server preflight", readme)
        self.assertIn("docs/examples/preflight-before-context7-mcp-docs-server-workflows.md", readme)
        self.assertIn("Context7 MCP docs-server preflight", landing)
        self.assertIn("docs/examples/preflight-before-context7-mcp-docs-server-workflows.md", landing)


if __name__ == "__main__":
    unittest.main()
