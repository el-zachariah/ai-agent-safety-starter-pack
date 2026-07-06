from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-voltagent-typescript-agent-workflows.md'


def test_named_agent_workflow_proof_doc_has_segment_and_buy_trigger():
    text = DOC.read_text()
    assert 'Preflight before VoltAgent agent workflows' in text
    assert 'VoltAgent/voltagent' in text
    assert 'VoltAgent agent preflight receipt' in text
    assert 'https://payhip.com/b/1nmxV' in text
    assert 'Yellow' in text and 'Red' in text and 'Green' in text


def test_named_agent_workflow_proof_linked_from_readme_and_landing_page():
    readme = (ROOT / 'README.md').read_text()
    index = (ROOT / 'index.html').read_text()
    marker = 'docs/examples/preflight-before-voltagent-typescript-agent-workflows.md'
    assert marker in readme
    assert 'VoltAgent agent workflow preflight proof' in readme
    assert marker in index
    assert 'VoltAgent agent workflow proof' in index
