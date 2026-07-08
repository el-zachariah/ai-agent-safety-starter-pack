from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "security-review-factsheet.md"
README = ROOT / "README.md"
LANDING = ROOT / "index.html"
MARKER = "SECURITY_REVIEW_FACTSHEET_2026_07_07"
DOC_LINK = "docs/security-review-factsheet.md"
PUBLIC_DOC_URL = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/security-review-factsheet.md"


class SecurityReviewFactsheetTests(unittest.TestCase):
    def test_factsheet_answers_security_reviewer_questions(self):
        text = DOC.read_text(encoding="utf-8")

        self.assertIn(MARKER, text)
        self.assertIn("AI-agent repo preflight security-review factsheet", text)
        self.assertIn("run locally", text)
        self.assertIn("does not need private source", text)
        self.assertIn("not a formal security audit", text)
        self.assertIn("not a formal security audit, compliance product, sandbox", text)
        self.assertIn("Purchase trigger: buy only when the free scanner is Yellow/Red", text)
        self.assertIn("SHA-256 `0b5ec15f3b45613ad4ca6f5263916e2c79d8300406c0c50db79e65b0937b945e`", text)
        self.assertIn("`32` files", text)
        self.assertIn("VERIFY-BUNDLE.py", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack", text)

    def test_factsheet_is_linked_before_proof_wall(self):
        readme = README.read_text(encoding="utf-8")
        html = LANDING.read_text(encoding="utf-8")

        self.assertIn(DOC_LINK, readme)
        self.assertIn(PUBLIC_DOC_URL, html)
        self.assertIn(MARKER, readme)
        self.assertIn(MARKER, html)
        self.assertLess(readme.index(DOC_LINK), readme.index("## Recent buyer-specific proof links"))
        self.assertLess(html.index(PUBLIC_DOC_URL), html.index("deadline-github-mcp-server-workflows-proof:start"))

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
            "dollars earned",
            "goal is to make",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()
