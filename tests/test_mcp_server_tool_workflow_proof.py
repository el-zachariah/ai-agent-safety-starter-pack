from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class McpServerToolWorkflowProofTest(unittest.TestCase):
    def test_mcp_proof_markers_are_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-mcp-server-tool-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("Model Context Protocol server preflight proof", doc)
        self.assertIn("modelcontextprotocol/servers", doc)
        self.assertIn("Yellow/Red", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("docs/examples/preflight-before-mcp-server-tool-workflows.md", readme)
        self.assertIn("mcp-server-tool-workflow-proof", index)
        self.assertIn("Get the $7 pack", index)

if __name__ == "__main__":
    unittest.main()
