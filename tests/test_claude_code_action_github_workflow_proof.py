import json
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC_REL = 'docs/examples/preflight-before-claude-code-github-action.md'
MARKER = 'CLAUDE_CODE_ACTION_GITHUB_WORKFLOW_PROOF'
PAYHIP = 'https://payhip.com/b/1nmxV'


class ClaudeCodeActionGithubWorkflowProofTest(unittest.TestCase):
    def test_doc_has_specific_buyer_trigger(self):
        text = (ROOT / DOC_REL).read_text(encoding='utf-8')
        for marker in [MARKER, 'anthropics/claude-code-action', 'Claude Code Action handoff receipt', 'Yellow/Red', PAYHIP]:
            self.assertIn(marker, text)

    def test_readme_and_landing_link_the_proof(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        landing = (ROOT / 'index.html').read_text(encoding='utf-8')
        for text in [readme, landing]:
            self.assertIn(DOC_REL, text)
            self.assertIn(MARKER, text)
            self.assertIn(PAYHIP, text)
        self.assertIn('Claude Code GitHub Action preflight proof', readme)
        self.assertIn('New: Claude Code GitHub Action preflight proof', landing)

    def test_lite_scanner_flags_claude_action_workflow_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            workflow = root / '.github' / 'workflows' / 'claude.yml'
            workflow.parent.mkdir(parents=True)
            workflow.write_text('''name: claude
on: [pull_request]
permissions:
  contents: write
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
''', encoding='utf-8')
            (root / '.env').write_text('ANTHROPIC_API_KEY=***\n', encoding='utf-8')
            (root / 'package.json').write_text('{"scripts":{"deploy":"npm publish"}}\n', encoding='utf-8')
            result = subprocess.run(['python3', str(ROOT / 'agent_preflight_lite.py'), str(root), '--json'], text=True, capture_output=True)
        self.assertNotEqual(result.stdout, '')
        data = json.loads(result.stdout)
        data_text = json.dumps(data, sort_keys=True)
        self.assertEqual(data['decision']['level'], 'YELLOW')
        self.assertIn('agent/workflow config', data['decision']['risk_buckets'])
        self.assertIn('secret-adjacent files', data['decision']['risk_buckets'])
        self.assertIn('package scripts', data['decision']['risk_buckets'])
        self.assertIn('.github/workflows/claude.yml', data_text)
        self.assertIn('.env', data_text)


if __name__ == '__main__':
    unittest.main()
