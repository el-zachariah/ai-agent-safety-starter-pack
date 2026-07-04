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
        self.assertIn("destructive-command hook", html)
        self.assertIn("python3 agent_preflight_lite.py /path/to/repo", html)
        self.assertIn("python3 agent_preflight_lite.py examples/sample-risky-repo", html)
        self.assertIn("Try the included risky sample", html)
        self.assertIn("Free scan first, then upgrade only when it saves setup time", html)
        self.assertIn("If it flags work, use the $7 pack", html)


if __name__ == "__main__":
    unittest.main()
