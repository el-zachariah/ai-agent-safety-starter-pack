import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestBoltBrowserAppBuilderProof(unittest.TestCase):
    def test_doc_has_named_segment_and_buy_trigger(self):
        text = (ROOT / "docs/examples/preflight-before-bolt-browser-app-builders.md").read_text(encoding="utf-8")
        self.assertIn("stackblitz-labs/bolt.diy", text)
        self.assertIn("Bolt-style browser app builders", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("package.json", text)
        self.assertIn("Green / Yellow / Red", text)

    def test_readme_and_landing_link_public_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("docs/examples/preflight-before-bolt-browser-app-builders.md", readme)
        self.assertIn("Bolt-style browser app builder preflight proof", readme)
        self.assertIn("docs/examples/preflight-before-bolt-browser-app-builders.md", index)
        self.assertIn("Bolt-style browser app-builder preflight proof", index)
        self.assertIn("https://payhip.com/b/1nmxV", index)


if __name__ == "__main__":
    unittest.main()
