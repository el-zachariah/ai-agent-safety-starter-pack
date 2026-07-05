from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
LANDING = ROOT / "index.html"


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.in_title = False
        self.title_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)


class LandingPageTests(unittest.TestCase):
    def test_landing_page_has_purchase_and_free_preview_paths(self):
        html = LANDING.read_text(encoding="utf-8")
        parser = LinkParser()
        parser.feed(html)

        self.assertIn("AI Agent Safety Starter Pack", "".join(parser.title_text))
        self.assertIn("https://payhip.com/b/1nmxV", parser.links)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack", parser.links)
        self.assertIn('property="og:title"', html)
        self.assertIn('name="twitter:card" content="summary_large_image"', html)
        self.assertIn('"@type": "Product"', html)
        self.assertIn('"price": "7.00"', html)
        self.assertIn('"priceCurrency": "USD"', html)
        self.assertIn("destructive-command hook", html)
        self.assertIn("python3 agent_preflight_lite.py /path/to/repo", html)
        self.assertIn("python3 agent_preflight_lite.py examples/sample-risky-repo", html)
        self.assertIn("Try the included risky sample", html)
        self.assertIn("one-minute repo risk scorecard", html)
        self.assertIn("Green / Yellow / Red", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/one-minute-risk-scorecard.md", parser.links)
        self.assertIn("red-flag to action matrix", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/red-flag-to-action-matrix.md", parser.links)
        self.assertIn("Claude Code slash-command bridge", html)
        self.assertIn("/agent-preflight", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/claude-code-slash-command.md", parser.links)
        self.assertIn("free agent handoff playbook", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/agent-handoff-playbook.md", parser.links)
        self.assertIn("5-minute upgrade checklist", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/upgrade-decision-checklist.md", parser.links)
        self.assertIn("Copy-paste prompt for the agent task", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/copy-paste-agent-task-prompt.md", parser.links)
        self.assertIn("Free scan first, then upgrade only when it saves setup time", html)
        self.assertIn("If it flags work, use the $7 pack", html)
        self.assertIn("30-second buy / skip decision", html)
        self.assertIn("Buy the $7 pack if the scan is Yellow/Red", html)
        self.assertIn("Skip it for now if the scan is Green", html)
        self.assertIn("MCP config preflight receipt example", html)
        self.assertIn("before the agent can read tokens", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/mcp-config-preflight-receipt-example.md", parser.links)
        self.assertIn("maintainer preflight receipt example", html)
        self.assertIn("AI-agent PRs", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/maintainer-preflight-receipt-example.md", parser.links)
        self.assertIn("Continuous Claude-style loop proof", html)
        self.assertIn("before long-running state, shell commands, and tool access begin", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/examples/preflight-before-continuous-claude.md", parser.links)


if __name__ == "__main__":
    unittest.main()


def test_live_distribution_proof_is_linked_and_specific():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    readme = (root / 'README.md').read_text(encoding='utf-8')
    index = (root / 'index.html').read_text(encoding='utf-8')
    proof = (root / 'docs/live-distribution-proof.md').read_text(encoding='utf-8')

    assert 'docs/live-distribution-proof.md' in readme
    assert 'live-distribution-proof' in index
    assert 'payhip.com/b/1nmxV' in proof
    assert 'github.com/e2b-dev/awesome-ai-sdks/pull/261' in proof
    assert 'CodeRabbit success' in proof
