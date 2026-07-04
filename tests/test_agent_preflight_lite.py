import json
import subprocess
import sys
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
        self.assertIn("Next steps", result.stdout)


if __name__ == "__main__":
    unittest.main()
