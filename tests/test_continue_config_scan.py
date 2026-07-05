from pathlib import Path
import tempfile
import unittest

from agent_preflight_lite import scan, classify_decision


class ContinueConfigScanTests(unittest.TestCase):
    def test_continue_config_counts_as_agent_workflow_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cfg = root / ".continue" / "config.json"
            cfg.parent.mkdir()
            cfg.write_text("{}", encoding="utf-8")

            findings = scan(root)
            decision = classify_decision(findings)

        self.assertTrue(any(f.kind == "agent-or-workflow-file" and f.path == ".continue/config.json" for f in findings))
        self.assertIn("agent/workflow config", decision["risk_buckets"])


if __name__ == "__main__":
    unittest.main()
