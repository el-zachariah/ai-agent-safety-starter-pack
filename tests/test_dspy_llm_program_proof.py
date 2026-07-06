import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class DspyLlmProgramProofTest(unittest.TestCase):
    def test_dspy_proof_has_buyer_trigger_and_target_evidence(self):
        proof = (ROOT / "docs/examples/preflight-before-dspy-llm-programs.md").read_text(encoding="utf-8")
        self.assertIn("stanfordnlp/dspy", proof)
        self.assertIn("DSPy LLM program preflight receipt", proof)
        self.assertIn("DSPY_LLM_PROGRAM_PROOF", proof)
        self.assertIn("Yellow/Red", proof)
        self.assertIn("https://payhip.com/b/1nmxV", proof)

    def test_dspy_proof_is_linked_from_buyer_surfaces(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("preflight-before-dspy-llm-programs.md", readme)
        self.assertIn("DSPy LLM program/eval preflight proof", index)
        self.assertIn("dspy-llm-program-proof", index)

if __name__ == "__main__":
    unittest.main()
