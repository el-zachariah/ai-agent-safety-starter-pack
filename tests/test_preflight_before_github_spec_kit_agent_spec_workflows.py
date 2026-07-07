import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "GITHUB_SPEC_KIT_AGENT_SPEC_WORKFLOW_PROOF"
SLUG = "preflight-before-github-spec-kit-agent-spec-workflows"
TARGET = "github/spec-kit"
PAYHIP = "https://payhip.com/b/1nmxV"

class PreflightBeforeGithubSpecKitAgentSpecWorkflowsTest(unittest.TestCase):
    def test_named_buyer_proof_surfaces_paid_trigger(self):
        doc = (ROOT / "docs" / "examples" / f"{SLUG}.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(MARKER, doc)
        self.assertIn(MARKER, readme)
        self.assertIn(MARKER, landing)
        self.assertIn(TARGET, doc)
        self.assertIn(TARGET, landing)
        self.assertIn(PAYHIP, doc)
        self.assertIn(PAYHIP, readme)
        self.assertIn(PAYHIP, landing)
        self.assertIn("Yellow", doc)
        self.assertIn("Red", doc)

if __name__ == "__main__":
    unittest.main()
