import tempfile
import unittest
from pathlib import Path

from agent_preflight_lite import scan

ROOT = Path(__file__).resolve().parents[1]
PAYHIP = 'https://payhip.com/b/1nmxV'
MARKER = 'KILO_CODE_AGENTIC_ENGINEERING_PROOF'
DOC = ROOT / 'docs' / 'examples' / 'preflight-before-kilo-code-agentic-engineering.md'


class KiloCodeAgenticEngineeringProofTest(unittest.TestCase):
    def test_kilo_code_proof_doc_has_buy_trigger_and_run_ticket(self):
        text = DOC.read_text(encoding='utf-8')
        self.assertIn(MARKER, text)
        self.assertIn('Kilo Code run-ticket receipt', text)
        self.assertIn('YELLOW_RED_BUY_TRIGGER_KILO_CODE', text)
        self.assertIn(PAYHIP, text)

    def test_kilo_code_proof_linked_from_readme_and_landing(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('preflight-before-kilo-code-agentic-engineering.md', readme)
        self.assertIn('preflight-before-kilo-code-agentic-engineering.md', index)
        self.assertIn(MARKER, readme)
        self.assertIn(MARKER, index)
        self.assertIn(PAYHIP, readme)
        self.assertIn(PAYHIP, index)

    def test_kilo_code_config_is_flagged_as_agent_workflow_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / '.kilocode' / 'settings.json'
            config.parent.mkdir()
            config.write_text('{"mcpServers": {}}\n', encoding='utf-8')
            findings = scan(root)
        self.assertTrue(
            any(f.kind == 'agent-or-workflow-file' and f.path == '.kilocode/settings.json' for f in findings),
            findings,
        )


if __name__ == '__main__':
    unittest.main()
