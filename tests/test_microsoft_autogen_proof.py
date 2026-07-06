from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-microsoft-autogen-multi-agent-workflows.md"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"


def test_microsoft_autogen_multi_agent_workflows_proof_markers():
    doc = DOC.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    index = INDEX.read_text(encoding="utf-8")
    assert "Microsoft AutoGen multi-agent preflight proof" in doc
    assert "microsoft/autogen" in doc
    assert "agent-preflight-autogen.md" in doc or "agent-preflight-microsoft-autogen-multi-agent-workflows.md" in doc
    assert "https://payhip.com/b/1nmxV" in doc
    assert "Microsoft AutoGen" in readme
    assert "docs/examples/preflight-before-microsoft-autogen-multi-agent-workflows.md" in readme
    assert "Microsoft AutoGen" in index
    assert "docs/examples/preflight-before-microsoft-autogen-multi-agent-workflows.md" in index
