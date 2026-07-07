from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "expense-reimbursement-note.md"
README = ROOT / "README.md"
LANDING = ROOT / "index.html"
MARKER = "EXPENSE_REIMBURSEMENT_NOTE_2026_07_07"
DOC_LINK = "docs/expense-reimbursement-note.md"
PUBLIC_DOC_URL = "https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/expense-reimbursement-note.md"


class ExpenseReimbursementNoteTests(unittest.TestCase):
    def test_note_has_public_safe_expense_logic(self):
        text = DOC.read_text(encoding="utf-8")

        self.assertIn(MARKER, text)
        self.assertIn("AI-agent repo preflight expense note", text)
        self.assertIn("approve or reimburse a $7 purchase", text)
        self.assertIn("Trigger: the free scanner result is Yellow / Red", text)
        self.assertIn("Green: no purchase requested", text)
        self.assertIn("Yellow: buy when the team needs", text)
        self.assertIn("Red: pause broad agent tool access", text)
        self.assertIn("keep private code, secrets, credentials", text)
        self.assertIn("https://payhip.com/b/1nmxV", text)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack", text)

    def test_note_is_linked_before_proof_wall(self):
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
            "revenue",
            "dollars earned",
            "goal is to make",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()
