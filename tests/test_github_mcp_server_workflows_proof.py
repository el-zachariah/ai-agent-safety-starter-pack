import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs' / 'examples' / 'preflight-before-github-mcp-server-workflows.md'

class GitHubMcpServerWorkflowProofTest(unittest.TestCase):
    def test_customer_proof_doc_and_funnel_links_exist(self):
        doc = DOC.read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        for text in (doc, readme, index):
            self.assertIn('GITHUB_MCP_SERVER_WORKFLOW_PROOF', text)
            self.assertIn('https://payhip.com/b/1nmxV', text)
        self.assertIn('github/github-mcp-server', doc)
        self.assertIn('repo, issue, PR, branch, workflow', index)
        self.assertIn('preflight-before-github-mcp-server-workflows.md', readme)

if __name__ == '__main__':
    unittest.main()
