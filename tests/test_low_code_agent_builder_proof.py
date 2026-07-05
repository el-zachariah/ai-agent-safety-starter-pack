from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_low_code_agent_builder_proof_is_linked():
    doc = ROOT / "docs/examples/preflight-before-low-code-agent-builders.md"
    readme = ROOT / "README.md"
    index = ROOT / "index.html"

    assert doc.exists()
    doc_text = doc.read_text(encoding="utf-8")
    assert "Dify / Flowise low-code agent builder proof" in doc_text
    assert "Buy the $7 pack" in doc_text
    assert "https://payhip.com/b/1nmxV" in doc_text

    assert "preflight-before-low-code-agent-builders.md" in readme.read_text(encoding="utf-8")
    assert "low-code agent builder preflight proof" in index.read_text(encoding="utf-8")
