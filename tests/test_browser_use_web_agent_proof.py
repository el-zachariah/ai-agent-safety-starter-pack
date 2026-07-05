import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class BrowserUseWebAgentProofTest(unittest.TestCase):
    def test_browser_use_proof_is_linked_to_purchase_trigger(self):
        doc = ROOT / "docs" / "examples" / "preflight-before-browser-use-web-agents.md"
        readme = ROOT / "README.md"
        index = ROOT / "index.html"
        self.assertTrue(doc.exists())
        doc_text = doc.read_text()
        self.assertIn("browser-use/browser-use", doc_text)
        self.assertIn("Browser-use preflight receipt", doc_text)
        self.assertIn("https://payhip.com/b/1nmxV", doc_text)
        self.assertIn("Yellow/Red", doc_text)
        self.assertIn("preflight-before-browser-use-web-agents.md", readme.read_text())
        self.assertIn("Browser-use web-agent preflight proof", index.read_text())


if __name__ == "__main__":
    unittest.main()
