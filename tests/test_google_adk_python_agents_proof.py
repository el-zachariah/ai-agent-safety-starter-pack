from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_google_adk_python_agents_proof_markers():
    doc = (ROOT / 'docs/examples/preflight-before-google-adk-python-agents.md').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    index = (ROOT / 'index.html').read_text(encoding='utf-8')
    required = [
        'Google ADK Python agent preflight proof',
        'google/adk-python',
        'Yellow/Red',
        'buy the $7 AI Agent Safety Starter Pack',
        'GOOGLE_ADK_PYTHON_AGENT_PROOF',
    ]
    for item in required:
        assert item in doc
    assert 'preflight-before-google-adk-python-agents.md' in readme
    assert 'preflight-before-google-adk-python-agents.md' in index
    assert 'GOOGLE_ADK_PYTHON_AGENT_PROOF' in readme
    assert 'GOOGLE_ADK_PYTHON_AGENT_PROOF' in index
