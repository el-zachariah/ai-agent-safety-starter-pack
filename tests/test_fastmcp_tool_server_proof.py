import json
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC_REL = 'docs/examples/preflight-before-fastmcp-tool-servers.md'
MARKER = 'FASTMCP_TOOL_SERVER_PROOF'
PAYHIP = 'https://payhip.com/b/1nmxV'


class FastMcpToolServerProofTest(unittest.TestCase):
    def test_doc_is_specific_and_has_checkout_trigger(self):
        text = (ROOT / DOC_REL).read_text(encoding='utf-8')
        for marker in [MARKER, 'PrefectHQ/fastmcp', 'FastMCP tool-server handoff receipt', 'Yellow/Red', PAYHIP]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_the_proof(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        landing = (ROOT / 'index.html').read_text(encoding='utf-8')
        for text in [readme, landing]:
            self.assertIn(DOC_REL, text)
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)
        self.assertIn('FastMCP tool-server preflight proof', readme)
        self.assertIn('New: FastMCP tool-server preflight proof', landing)

    def test_lite_scanner_flags_fastmcp_dependency_and_mcp_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / 'pyproject.toml').write_text('[project]\ndependencies = ["fastmcp>=2"]\n', encoding='utf-8')
            (root / '.mcp.json').write_text('{"mcpServers":{"local-fastmcp":{"command":"python","args":["server.py"]}}}\n', encoding='utf-8')
            output = subprocess.check_output([
                'python3', str(ROOT / 'agent_preflight_lite.py'), str(root), '--json'
            ], text=True)
        data = json.loads(output)
        data_text = json.dumps(data, sort_keys=True)
        self.assertEqual(data['decision']['level'], 'YELLOW')
        self.assertIn('agent framework dependency', data['decision']['risk_buckets'])
        self.assertIn('agent/workflow config', data['decision']['risk_buckets'])
        self.assertIn('fastmcp', data_text.lower())
        self.assertIn('.mcp.json', data_text)


if __name__ == '__main__':
    unittest.main()
