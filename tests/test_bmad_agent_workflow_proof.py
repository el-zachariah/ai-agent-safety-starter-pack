import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
REL = "docs/examples/preflight-before-bmad-agent-workflows.md"


class BmadAgentWorkflowProofTest(unittest.TestCase):
    def test_doc_has_checkout_trigger_and_target_evidence(self):
        text = (ROOT / REL).read_text(encoding="utf-8")
        for marker in [
            "bmad-code-org/BMAD-METHOD",
            "BMAD agent preflight receipt",
            "Yellow",
            "Red",
            "https://payhip.com/b/1nmxV",
            "python3 agent_preflight_lite.py",
            "Must ask first",
            "Must not touch",
        ]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_the_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(REL, readme)
        self.assertIn("BMAD agent workflow preflight proof", readme)
        self.assertIn("BMAD agent workflow preflight proof", landing)
        self.assertIn("preflight-before-bmad-agent-workflows.md", landing)


if __name__ == "__main__":
    unittest.main()
