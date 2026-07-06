from pathlib import Path

from agent_preflight_lite import scan

ROOT = Path(__file__).resolve().parents[1]


def test_skills_curated_marketplace_proof_markers():
    doc = (ROOT / 'docs/examples/preflight-before-skills-curated-marketplace-review.md').read_text()
    readme = (ROOT / 'README.md').read_text()
    index = (ROOT / 'index.html').read_text()

    assert 'Skills-curated marketplace reviewer preflight proof' in doc
    assert 'trailofbits/skills-curated' in doc
    assert '.claude-plugin/' in doc
    assert 'https://payhip.com/b/1nmxV' in doc
    assert 'docs/examples/preflight-before-skills-curated-marketplace-review.md' in readme
    assert 'Skills-curated marketplace reviewer preflight proof' in index
    assert 'https://payhip.com/b/1nmxV' in index


def test_claude_plugin_package_files_are_scanned(tmp_path):
    plugin_file = tmp_path / '.claude-plugin' / 'marketplace.json'
    plugin_file.parent.mkdir()
    plugin_file.write_text('{"name":"candidate-plugin"}')

    findings = scan(tmp_path)

    assert any(f.kind == 'agent-or-workflow-file' and f.path == '.claude-plugin/marketplace.json' for f in findings)
