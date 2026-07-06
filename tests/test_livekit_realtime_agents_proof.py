import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LiveKitRealtimeAgentsProofTest(unittest.TestCase):
    def test_livekit_doc_has_checkout_trigger_and_segment_markers(self):
        text = (ROOT / "docs/examples/preflight-before-livekit-realtime-agents.md").read_text()
        for marker in [
            "LiveKit realtime agent preflight receipt",
            "livekit/agents",
            "room/session credential paths",
            "worker process files",
            "Buy the $7 pack",
            "https://payhip.com/b/1nmxV",
        ]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_livekit_proof(self):
        readme = (ROOT / "README.md").read_text()
        index = (ROOT / "index.html").read_text()
        self.assertIn("docs/examples/preflight-before-livekit-realtime-agents.md", readme)
        self.assertIn("LiveKit realtime agent teams", readme)
        self.assertIn("docs/examples/preflight-before-livekit-realtime-agents.md", index)
        self.assertIn("LiveKit realtime agent preflight receipt", index)

if __name__ == "__main__":
    unittest.main()
