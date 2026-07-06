from pathlib import Path
import tempfile
import unittest

from agent_preflight_lite import classify_decision, scan

ROOT = Path(__file__).resolve().parents[1]


class ReplitAgentWorkspaceProofTests(unittest.TestCase):
    def test_replit_workspace_config_is_scanned(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / ".replit").write_text('run = "npm start"\n', encoding="utf-8")
            (repo / "replit.nix").write_text('{ pkgs }: { deps = [ pkgs.nodejs ]; }\n', encoding="utf-8")
            (repo / "package.json").write_text('{"scripts":{"start":"node server.js"}}\n', encoding="utf-8")

            findings = scan(repo)
            paths = {finding.path for finding in findings}
            kinds = {finding.kind for finding in findings}
            decision = classify_decision(findings)

        self.assertIn(".replit", paths)
        self.assertIn("replit.nix", paths)
        self.assertIn("package.json", paths)
        self.assertIn("agent-or-workflow-file", kinds)
        self.assertIn("package-scripts", kinds)
        self.assertIn("agent/workflow config", decision["risk_buckets"])

    def test_replit_proof_is_public_funnel_linked(self):
        proof = ROOT / "docs/examples/preflight-before-replit-agent-workspaces.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-replit-agent-workspaces.md", readme)
        self.assertIn("Replit Agent workspace preflight proof", index)
        self.assertIn(".replit", proof_text)
        self.assertIn("replit.nix", proof_text)
        self.assertIn("agent-preflight-replit", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", index)


if __name__ == "__main__":
    unittest.main()
