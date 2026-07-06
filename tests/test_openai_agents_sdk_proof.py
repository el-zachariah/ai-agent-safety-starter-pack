from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_openai_agents_sdk_proof_markers():
    doc = (ROOT / 'docs/examples/preflight-before-openai-agents-sdk.md').read_text()
    readme = (ROOT / 'README.md').read_text()
    index = (ROOT / 'index.html').read_text()

    assert 'OpenAI Agents SDK tool-agent preflight proof' in doc
    assert 'openai/openai-agents-python' in doc
    assert 'Yellow/Red' in doc
    assert 'https://payhip.com/b/1nmxV' in doc
    assert 'docs/examples/preflight-before-openai-agents-sdk.md' in readme
    assert 'OpenAI Agents SDK tool-agent preflight proof' in index
    assert 'https://payhip.com/b/1nmxV' in index
