from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAYHIP = 'https://payhip.com/b/1nmxV'
MARKER = 'AIDER_LOCAL_AI_PAIR_PROGRAMMING_PROOF'
DOC = ROOT / 'docs' / 'examples' / 'preflight-before-aider-local-ai-pair-programming.md'


def test_aider_proof_doc_has_buy_trigger_and_run_ticket():
    text = DOC.read_text(encoding='utf-8')
    assert MARKER in text
    assert 'Aider run-ticket receipt' in text
    assert 'YELLOW_RED_BUY_TRIGGER_AIDER' in text
    assert PAYHIP in text


def test_aider_proof_linked_from_readme_and_landing():
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    index = (ROOT / 'index.html').read_text(encoding='utf-8')
    assert 'preflight-before-aider-local-ai-pair-programming.md' in readme
    assert 'preflight-before-aider-local-ai-pair-programming.md' in index
    assert MARKER in readme
    assert MARKER in index
    assert PAYHIP in readme
    assert PAYHIP in index
