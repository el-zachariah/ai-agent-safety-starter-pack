from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_open_interpreter_local_agent_proof_markers():
    doc = (ROOT / 'docs/examples/preflight-before-open-interpreter-local-agents.md').read_text()
    readme = (ROOT / 'README.md').read_text()
    index = (ROOT / 'index.html').read_text()

    assert 'Open Interpreter local code-agent preflight proof' in doc
    assert 'OpenInterpreter/open-interpreter' in doc
    assert 'Yellow/Red' in doc
    assert 'https://payhip.com/b/1nmxV' in doc
    assert 'docs/examples/preflight-before-open-interpreter-local-agents.md' in readme
    assert 'Open Interpreter local code-agent proof' in index
    assert 'https://payhip.com/b/1nmxV' in index
