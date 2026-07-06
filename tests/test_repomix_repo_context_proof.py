from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepomixRepoContextProofTest(unittest.TestCase):
    def test_doc_has_verified_target_and_buy_trigger(self):
        doc = (ROOT / "docs/examples/preflight-before-repomix-repo-context-packs.md").read_text(encoding="utf-8")
        self.assertIn("yamadashy/repomix", doc)
        self.assertIn("Repomix repo-context", doc)
        self.assertIn("Yellow/Red buy trigger", doc)
        self.assertIn("https://payhip.com/b/1nmxV", doc)

    def test_readme_links_named_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/examples/preflight-before-repomix-repo-context-packs.md", readme)
        self.assertIn("Repomix repo-context proof", readme)

    def test_landing_links_named_proof(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("docs/examples/preflight-before-repomix-repo-context-packs.md", index)
        self.assertIn("Repomix repo-context proof", index)


if __name__ == "__main__":
    unittest.main()
