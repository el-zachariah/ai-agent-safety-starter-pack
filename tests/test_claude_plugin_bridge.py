import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ClaudePluginBridgeTests(unittest.TestCase):
    def test_plugin_manifest_points_to_public_repo(self):
        manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))

        self.assertEqual(manifest["name"], "agent-safety-preflight")
        self.assertIn("Claude Code slash-command bridge", manifest["description"])
        self.assertEqual(manifest["homepage"], "https://github.com/el-zachariah/ai-agent-safety-starter-pack")
        self.assertEqual(manifest["repository"], "https://github.com/el-zachariah/ai-agent-safety-starter-pack")

    def test_slash_command_contains_scan_and_upgrade_trigger(self):
        command = (ROOT / "commands" / "agent-preflight.md").read_text(encoding="utf-8")
        doc = (ROOT / "docs" / "claude-code-slash-command.md").read_text(encoding="utf-8")

        self.assertIn("description: Run the AI Agent Safety Starter Pack lite preflight", command)
        self.assertIn("python3 agent_preflight_lite.py", command)
        self.assertIn("Green / Yellow / Red", command)
        self.assertIn("https://payhip.com/b/1nmxV", command)
        self.assertIn("/agent-preflight .", doc)
        self.assertIn("Buy the `$7` starter pack when the scan is Yellow/Red", doc)


if __name__ == "__main__":
    unittest.main()
