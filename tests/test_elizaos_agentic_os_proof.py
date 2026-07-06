import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ElizaOsAgenticOsProofTest(unittest.TestCase):
    def test_public_markers(self):
        doc = (ROOT / "docs/examples/preflight-before-elizaos-agentic-os-plugin-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in [
            "ElizaOS agentic OS/plugin workflow preflight proof",
            "elizaOS/eliza",
            "ELIZAOS_AGENTIC_OS_PLUGIN_PROOF",
            "buy the $7 AI Agent Safety Starter Pack",
        ]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-elizaos-agentic-os-plugin-workflows.md", readme)
        self.assertIn("docs/examples/preflight-before-elizaos-agentic-os-plugin-workflows.md", index)
        self.assertIn("Get the reusable $7 workflow", index)

if __name__ == "__main__":
    unittest.main()
