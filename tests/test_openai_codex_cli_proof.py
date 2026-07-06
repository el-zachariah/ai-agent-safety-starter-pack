from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_openai_codex_cli_proof_markers():
    doc = (ROOT / 'docs/examples/preflight-before-openai-codex-cli.md').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    index = (ROOT / 'index.html').read_text(encoding='utf-8')

    required = [
        'OpenAI Codex CLI preflight proof',
        'openai/codex',
        'Yellow/Red',
        'buy the $7 AI Agent Safety Starter Pack',
    ]
    for marker in required:
        assert marker in doc
    assert 'docs/examples/preflight-before-openai-codex-cli.md' in readme
    assert 'docs/examples/preflight-before-openai-codex-cli.md' in index
    assert 'Get the $7 pack' in index
