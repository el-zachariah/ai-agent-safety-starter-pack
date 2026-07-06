from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CloudflareWorkersAgentProofTests(unittest.TestCase):
    def test_cloudflare_workers_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-cloudflare-workers-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-cloudflare-workers-agents.md", readme)
        self.assertIn("Cloudflare Workers AI Agents preflight proof", index)
        self.assertIn("cloudflare/agents", proof_text)
        self.assertIn("wrangler", proof_text)
        self.assertIn(".dev.vars", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


if __name__ == "__main__":
    unittest.main()
