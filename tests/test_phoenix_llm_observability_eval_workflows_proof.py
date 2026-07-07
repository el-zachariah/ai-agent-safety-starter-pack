from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REL = "docs/examples/preflight-before-phoenix-llm-observability-eval-workflows.md"
MARKER = "PHOENIX_LLM_OBSERVABILITY_EVAL_WORKFLOW_PROOF"
TARGET = "Arize-ai/phoenix"
PAYHIP = "https://payhip.com/b/1nmxV"


class TestPhoenixLlmObservabilityEvalWorkflowsProof(unittest.TestCase):
    def test_proof_doc_maps_to_named_segment_and_buy_trigger(self):
        doc = (ROOT / REL).read_text(encoding="utf-8")
        for needle in [TARGET, MARKER, "Green / Yellow / Red buy trigger", PAYHIP, "No affiliation"]:
            self.assertIn(needle, doc)

    def test_readme_and_landing_link_the_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        for text in [readme, landing]:
            self.assertIn(REL, text)
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)


if __name__ == "__main__":
    unittest.main()
