import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class AgentServiceToolkitProductionAgentsProofTest(unittest.TestCase):
    def test_customer_proof_markers_exist(self):
        doc = (ROOT / "docs/examples/preflight-before-agent-service-toolkit-production-agents.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("AGENT_SERVICE_TOOLKIT_PRODUCTION_AGENT_PROOF", doc)
        self.assertIn("JoshuaC215/agent-service-toolkit", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)
        self.assertIn("docs/examples/preflight-before-agent-service-toolkit-production-agents.md", readme)
        self.assertIn("AGENT_SERVICE_TOOLKIT_PRODUCTION_AGENT_PROOF", index)
        self.assertIn("https://payhip.com/b/1nmxV", index)

if __name__ == "__main__":
    unittest.main()
