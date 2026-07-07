import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_REL = "docs/examples/preflight-before-claude-squad-terminal-agent-fleets.md"
MARKER = "CLAUDE_SQUAD_TERMINAL_AGENT_FLEET_PROOF"

class ClaudeSquadTerminalAgentFleetProofTest(unittest.TestCase):
    def test_doc_names_public_target_and_buy_trigger(self):
        text = (ROOT / DOC_REL).read_text(encoding="utf-8")
        for needle in [
            "smtg-ai/claude-squad",
            "terminal-agent fleets",
            MARKER,
            "https://payhip.com/b/1nmxV",
            "Yellow",
            "Red",
            "Claude Code / Codex / OpenCode / Amp",
            "Must ask before",
        ]:
            self.assertIn(needle, text)

    def test_funnel_links_the_new_proof(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        landing = (ROOT / "index.html").read_text(encoding="utf-8")
        for text in [readme, landing]:
            self.assertIn(DOC_REL, text)
            self.assertIn(MARKER, text)
            self.assertIn("Claude Squad", text)

if __name__ == "__main__":
    unittest.main()
