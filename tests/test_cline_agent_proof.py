from pathlib import Path
import tempfile
import unittest

import agent_preflight_lite as scanner

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-cline-vscode-autonomous-agents.md"


class NamedAgentProofTest(unittest.TestCase):
    def test_public_buyer_proof_markers(self):
        doc = DOC.read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in ["Cline", "Yellow", "Red", "https://payhip.com/b/1nmxV", ".clinerules"]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-cline-vscode-autonomous-agents.md", readme)
        self.assertIn("docs/examples/preflight-before-cline-vscode-autonomous-agents.md", index)

    def test_scanner_flags_named_agent_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".clinerules").write_text("Ask before deploys\n", encoding="utf-8")
            nested = root / ".cline" / "rules"
            nested.mkdir(parents=True, exist_ok=True)
            (nested / "agent.md").write_text("Do not expose secrets\n", encoding="utf-8")
            findings = scanner.scan(root)
        paths = {finding.path for finding in findings if finding.kind == "agent-or-workflow-file"}
        self.assertIn(".clinerules", paths)
        self.assertIn(".cline/rules/agent.md", paths)


if __name__ == "__main__":
    unittest.main()
