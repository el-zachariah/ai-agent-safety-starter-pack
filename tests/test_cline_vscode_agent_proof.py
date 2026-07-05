from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-cline-autonomous-vscode-agents.md"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"


def test_cline_proof_doc_names_segment_and_buy_trigger():
    text = DOC.read_text()
    assert "Cline autonomous VS Code agents" in text
    assert "repo-write and command-execution" in text
    assert "https://payhip.com/b/1nmxV" in text
    assert "Buy" in text and "Skip" in text


def test_cline_proof_is_linked_from_funnel():
    rel = "docs/examples/preflight-before-cline-autonomous-vscode-agents.md"
    assert rel in README.read_text()
    assert rel in INDEX.read_text()
