from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "ci-preflight-recipe.md"
README = ROOT / "README.md"
LANDING = ROOT / "index.html"
MARKER = "CI_PR_REVIEWER_RECEIPT_BEFORE_CHECKOUT_2026_07_08"
DOC_LINK = "docs/ci-preflight-recipe.md"
PUBLIC_DOC_URL = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/ci-preflight-recipe.md"


class CiPreflightRecipeBeforeCheckoutTests(unittest.TestCase):
    def test_recipe_has_public_safe_buyer_decision_path(self):
        text = DOC.read_text(encoding="utf-8")

        self.assertIn("CI preflight recipe for AI-agent pull requests", text)
        self.assertIn("Copy-paste GitHub Actions step", text)
        self.assertIn("python3 agent_preflight_lite.py . --json", text)
        self.assertIn("Green / Yellow / Red", text)
        self.assertIn("The `$7` starter pack", text)
        self.assertIn("Payhip bundle: https://payhip.com/b/1nmxV", text)

    def test_recipe_is_promoted_before_proof_wall(self):
        readme = README.read_text(encoding="utf-8")
        html = LANDING.read_text(encoding="utf-8")

        self.assertEqual(readme.count(MARKER), 1)
        self.assertEqual(html.count(MARKER), 1)
        self.assertIn(DOC_LINK, readme)
        self.assertIn(PUBLIC_DOC_URL, html)
        self.assertIn("Need a CI / PR reviewer receipt?", html)
        self.assertLess(readme.index(MARKER), readme.index("## Recent buyer-specific proof links"))
        self.assertLess(html.index(MARKER), html.index("deadline-github-mcp-server-workflows-proof:start"))

    def test_public_copy_avoids_internal_operator_language(self):
        combined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [DOC, README, LANDING]
        ).lower()
        forbidden = [
            "wealth hunter",
            "wealth-hunter",
            "first-dollar",
            "first dollar",
            "make money",
            "revenue",
            "dollars earned",
            "goal is to make",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()

