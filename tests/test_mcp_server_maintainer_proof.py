from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_mcp_server_maintainer_proof_proof_markers():
    doc = (ROOT / "docs" / "mcp-server-maintainer-proof.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "MCP server maintainer proof" in doc
    assert "https://payhip.com/b/1nmxV" in doc
    assert "No private repository upload is required" in doc
    assert "docs/mcp-server-maintainer-proof.md" in readme
