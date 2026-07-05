import tempfile
import unittest
from pathlib import Path

import agent_preflight_lite


class CopilotInstructionsScanTest(unittest.TestCase):
    def test_github_copilot_instructions_are_agent_workflow_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            github_dir = root / ".github"
            github_dir.mkdir()
            (github_dir / "copilot-instructions.md").write_text(
                "Always run npm test before opening a pull request.\n",
                encoding="utf-8",
            )

            findings = agent_preflight_lite.scan(root)
            decision = agent_preflight_lite.classify_decision(findings)

        self.assertTrue(
            any(
                finding.kind == "agent-or-workflow-file"
                and finding.path == ".github/copilot-instructions.md"
                for finding in findings
            ),
            findings,
        )
        self.assertIn("agent/workflow config", decision["risk_buckets"])


if __name__ == "__main__":
    unittest.main()
