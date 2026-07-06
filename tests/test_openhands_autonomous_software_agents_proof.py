from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class OpenhandsAutonomousSoftwareAgentsProofTest(unittest.TestCase):
    def test_named_segment_markers_are_linked(self):
        doc = (ROOT / "docs/examples/preflight-before-openhands-autonomous-software-agents.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        for marker in ["Preflight before OpenHands autonomous software-agent runs", "OpenHands/OpenHands", "https://payhip.com/b/1nmxV", "Yellow/Red"]:
            self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-openhands-autonomous-software-agents.md", readme)
        self.assertIn("Preflight before OpenHands autonomous software-agent runs", readme)
        self.assertIn("Preflight before OpenHands autonomous software-agent runs", index)
        self.assertIn("docs/examples/preflight-before-openhands-autonomous-software-agents.md", index)

if __name__ == "__main__":
    unittest.main()
