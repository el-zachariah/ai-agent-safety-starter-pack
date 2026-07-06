import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PromptfooLlmEvalWorkflowsProofTest(unittest.TestCase):
    def test_public_markers(self):
        doc = (ROOT / "docs/examples/preflight-before-promptfoo-llm-eval-workflows.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in [
            "Promptfoo LLM eval/red-team workflow preflight proof",
            "promptfoo/promptfoo",
            "Green / Yellow / Red buy trigger",
            "buy the $7 AI Agent Safety Starter Pack",
            "promptfoo-agent-eval-preflight-receipt.md",
        ]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-promptfoo-llm-eval-workflows.md", readme)
        self.assertIn("PROMPTFOO_LLM_EVAL_WORKFLOW_PROOF", readme)
        self.assertIn("docs/examples/preflight-before-promptfoo-llm-eval-workflows.md", index)
        self.assertIn("Get the $7 pack", index)

if __name__ == "__main__":
    unittest.main()
