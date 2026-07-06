import json
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC_REL = 'docs/examples/preflight-before-amazon-q-developer-cli.md'
MARKER = 'AMAZON_Q_DEVELOPER_CLI_PROOF'
PAYHIP = 'https://payhip.com/b/1nmxV'

class AmazonQDeveloperCliProofTest(unittest.TestCase):
    def test_doc_is_specific_and_has_checkout_trigger(self):
        text = (ROOT / DOC_REL).read_text(encoding='utf-8')
        for marker in [MARKER, 'aws/amazon-q-developer-cli', 'Amazon Q Developer CLI', '60-second Amazon Q handoff receipt', 'Yellow/Red', PAYHIP]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_the_proof(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        landing = (ROOT / 'index.html').read_text(encoding='utf-8')
        for text in [readme, landing]:
            self.assertIn(DOC_REL, text)
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)
        self.assertIn('Amazon Q Developer CLI preflight proof', readme)
        self.assertIn('New: Amazon Q Developer CLI preflight proof', landing)

    def test_lite_scanner_flags_amazonq_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            cfg = root / '.amazonq'
            cfg.mkdir()
            (cfg / 'rules.md').write_text('Ask before deploys or AWS account changes.\n', encoding='utf-8')
            output = subprocess.check_output([
                'python3', str(ROOT / 'agent_preflight_lite.py'), str(root), '--json'
            ], text=True)
        data_text = json.dumps(json.loads(output), sort_keys=True)
        self.assertIn('.amazonq/rules.md', data_text)
        self.assertIn('agent/workflow config', data_text)

if __name__ == '__main__':
    unittest.main()
