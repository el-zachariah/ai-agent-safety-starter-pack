import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PlaywrightMcpBrowserAgentProofTest(unittest.TestCase):
    def test_playwright_mcp_doc_has_checkout_trigger_and_segment_markers(self):
        text = (ROOT / 'docs/examples/preflight-before-playwright-mcp-browser-agents.md').read_text()
        for marker in [
            'Playwright MCP browser-agent preflight receipt',
            'microsoft/playwright-mcp',
            'PLAYWRIGHT_MCP_BROWSER_AGENT_PROOF',
            'Browser/session scope',
            'Buy the $7 pack',
            'https://payhip.com/b/1nmxV',
        ]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_playwright_mcp_proof(self):
        readme = (ROOT / 'README.md').read_text()
        index = (ROOT / 'index.html').read_text()
        self.assertIn('docs/examples/preflight-before-playwright-mcp-browser-agents.md', readme)
        self.assertIn('Playwright MCP browser-agent teams', readme)
        self.assertIn('docs/examples/preflight-before-playwright-mcp-browser-agents.md', index)
        self.assertIn('Playwright MCP browser-agent preflight receipt', index)

if __name__ == '__main__':
    unittest.main()
