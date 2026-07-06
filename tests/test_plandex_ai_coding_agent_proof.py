from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_plandex_ai_coding_agent_proof_markers():
    doc = (ROOT / 'docs/examples/preflight-before-plandex-ai-coding-agents.md').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    index = (ROOT / 'index.html').read_text(encoding='utf-8')

    required = [
        'Plandex AI coding-agent preflight proof',
        'plandex-ai/plandex',
        'Yellow/Red',
        'buy the $7 AI Agent Safety Starter Pack',
    ]
    for marker in required:
        assert marker in doc
    assert 'preflight-before-plandex-ai-coding-agents.md' in readme
    assert 'preflight-before-plandex-ai-coding-agents.md' in index
    assert 'Get the $7 pack' in index
