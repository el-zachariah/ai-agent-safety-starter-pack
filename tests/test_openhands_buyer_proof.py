import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class OpenHandsBuyerProofTest(unittest.TestCase):
    def test_named_buyer_proof_is_linked(self):
        doc_rel = 'docs/examples/preflight-before-openhands-autonomous-swe-agents.md'
        doc = (ROOT / doc_rel).read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')

        self.assertIn('OpenHands autonomous SWE agents', doc)
        self.assertIn('Green / Yellow / Red', doc)
        self.assertIn('Buy / skip trigger for the $7 pack', doc)
        self.assertIn('https://payhip.com/b/1nmxV', doc)
        self.assertIn(doc_rel, readme)
        self.assertIn(doc_rel, index)


if __name__ == '__main__':
    unittest.main()
