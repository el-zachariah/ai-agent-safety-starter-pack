from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PrAgentReviewBotProofTest(unittest.TestCase):
    def test_pr_agent_proof_is_linked_to_purchase_trigger(self):
        doc = ROOT / "docs" / "examples" / "preflight-before-pr-agent-review-bots.md"
        readme = ROOT / "README.md"
        index = ROOT / "index.html"
        self.assertTrue(doc.exists())
        doc_text = doc.read_text(encoding="utf-8")
        self.assertIn("The-PR-Agent/pr-agent", doc_text)
        self.assertIn("PR-Agent review bot preflight", doc_text)
        self.assertIn("https://payhip.com/b/1nmxV", doc_text)
        self.assertIn("Yellow or Red", doc_text)
        self.assertIn("preflight-before-pr-agent-review-bots.md", readme.read_text(encoding="utf-8"))
        self.assertIn("PR-Agent review bot preflight proof", index.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
