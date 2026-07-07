from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class ReadmePurchasePathTests(unittest.TestCase):
    def test_purchase_path_appears_before_proof_wall(self):
        readme = README.read_text(encoding="utf-8")

        self.assertTrue(
            readme.startswith("# AI Agent Safety Starter Pack — free lite preflight"),
            "README should open with the buyer-facing product path, not the proof wall.",
        )
        hero_pos = readme.index("**Buy the full bundle:** https://payhip.com/b/1nmxV")
        decision_pos = readme.index("README_PURCHASE_PATH_FIRST_2026_07_07")
        proof_heading_pos = readme.index("## Recent buyer-specific proof links")
        first_proof_pos = readme.index("deadline-github-mcp-server-workflows-proof:start")
        scanner_pos = readme.index("## What the free lite scanner catches")

        self.assertLess(hero_pos, proof_heading_pos)
        self.assertLess(decision_pos, proof_heading_pos)
        self.assertLess(proof_heading_pos, first_proof_pos)
        self.assertLess(first_proof_pos, scanner_pos)
        self.assertIn("run the free scan first", readme[:proof_heading_pos].lower())
        self.assertIn("Yellow/Red", readme[:proof_heading_pos])
        self.assertEqual(readme.count("# AI Agent Safety Starter Pack"), 1)
        self.assertEqual(readme.count("README_PURCHASE_PATH_FIRST_2026_07_07"), 2)


if __name__ == "__main__":
    unittest.main()
