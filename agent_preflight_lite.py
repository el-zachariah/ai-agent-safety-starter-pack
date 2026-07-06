#!/usr/bin/env python3
"""Lite AI-agent repo preflight scanner.

This public preview flags common files and command patterns worth checking before
letting an AI coding agent run tools in a repository. It is not a sandbox, secret
scanner, malware scanner, or security audit.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, TypedDict

AGENT_FILE_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "copilot-instructions.md",
    ".cursorrules",
    ".clineignore",
    ".clinerules",
    ".cursorignore",
    ".mcp.json",
    "mcp.json",
    "settings.json",
    "devcontainer.json",
    ".replit",
    "replit.nix",
}

SECRET_ADJACENT_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".npmrc",
    ".pypirc",
    ".netrc",
    "id_rsa",
    "id_ed25519",
}

INTERESTING_SUFFIXES = {".sh", ".bash", ".zsh", ".fish", ".ps1", ".yml", ".yaml", ".json", ".toml", ".nix"}
MAX_FILE_BYTES = 250_000

RISK_PATTERNS = [
    ("destructive-delete", re.compile(r"\brm\s+-[rfRF]*\s+[\"']?(/|\$\{|\$HOME|~|\.\.)")),
    ("force-push", re.compile(r"\bgit\s+push\b[^\n]*\s--force(?:-with-lease)?\b")),
    ("curl-pipe-shell", re.compile(r"\b(curl|wget)\b[^\n]*(\||>)\s*(sudo\s+)?(sh|bash)\b")),
    ("chmod-777", re.compile(r"\bchmod\s+-?R?\s*777\b")),
    ("docker-socket", re.compile(r"/var/run/docker\.sock")),
    ("disk-format", re.compile(r"\b(mkfs|fdisk|parted|dd\s+if=)\b")),
    ("sudo-install-or-script", re.compile(r"\bsudo\b[^\n]*(install|bash|sh|python|node|npm|pip)\b")),
]

KIND_TO_BUCKET = {
    "agent-or-workflow-file": "agent/workflow config",
    "secret-adjacent-file": "secret-adjacent files",
    "package-scripts": "package scripts",
}
for risk_kind, _pattern in RISK_PATTERNS:
    KIND_TO_BUCKET[risk_kind] = "risky shell commands"

DECISION_SUMMARIES = {
    "GREEN": "No matched lite-scan risk buckets; continue with normal review discipline.",
    "YELLOW": "Write a short run / ask / avoid handoff before giving the agent tools.",
    "RED": "Stop and add a pre-agent handoff/guardrail pass before tool access.",
}

@dataclass
class Finding:
    severity: str
    kind: str
    path: str
    line: int | None
    detail: str


class Decision(TypedDict):
    level: str
    risk_buckets: list[str]
    summary: str


def iter_files(root: Path) -> Iterable[Path]:
    skip_dirs = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
    for path in root.rglob("*"):
        if any(part in skip_dirs for part in path.parts):
            continue
        if path.is_file():
            yield path


def is_agent_related(path: Path) -> bool:
    parts = set(path.parts)
    return (
        path.name in AGENT_FILE_NAMES
        or ".cursor" in parts
        or ".cline" in parts
        or ".claude" in parts
        or ".claude-plugin" in parts
        or ".continue" in parts
        or ".kilocode" in parts
        or ".devcontainer" in parts
        or (".github" in parts and path.name == "copilot-instructions.md")
        or path.match(".github/workflows/*")
    )


def scan(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        if is_agent_related(path):
            findings.append(Finding("medium", "agent-or-workflow-file", rel, None, "Review before agent execution."))
        if path.name in SECRET_ADJACENT_NAMES or ".env" in path.name.lower():
            findings.append(Finding("high", "secret-adjacent-file", rel, None, "Do not expose this to an agent unless intentionally sanitized."))
        if path.name == "package.json":
            findings.append(Finding("medium", "package-scripts", rel, None, "Review scripts before an agent runs install/test/build commands."))
        if path.suffix.lower() not in INTERESTING_SUFFIXES and path.name not in AGENT_FILE_NAMES:
            continue
        try:
            if path.stat().st_size > MAX_FILE_BYTES:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            for kind, pattern in RISK_PATTERNS:
                if pattern.search(line):
                    findings.append(Finding("high", kind, rel, idx, line.strip()[:240]))
    return findings


def classify_decision(findings: list[Finding]) -> Decision:
    """Turn raw findings into the README's Green / Yellow / Red buy-skip signal."""
    risk_buckets: list[str] = []
    seen_buckets: set[str] = set()
    high_count = 0
    risky_shell_count = 0
    for finding in findings:
        bucket = KIND_TO_BUCKET.get(finding.kind, finding.kind)
        if bucket not in seen_buckets:
            seen_buckets.add(bucket)
            risk_buckets.append(bucket)
        if finding.severity == "high":
            high_count += 1
        if bucket == "risky shell commands":
            risky_shell_count += 1

    if not findings:
        level = "GREEN"
    elif len(risk_buckets) >= 4 or high_count >= 3 or risky_shell_count >= 2:
        level = "RED"
    elif len(risk_buckets) >= 2 or high_count >= 1:
        level = "YELLOW"
    else:
        level = "GREEN"

    return {
        "level": level,
        "risk_buckets": risk_buckets,
        "summary": DECISION_SUMMARIES[level],
    }


def render_markdown(root: Path, findings: list[Finding]) -> str:
    decision = classify_decision(findings)
    lines = [
        f"# Lite AI-agent preflight report: `{root}`",
        "",
        f"Findings: **{len(findings)}**",
        f"Decision: **{decision['level']}** — {decision['summary']}",
        "",
    ]
    if decision["risk_buckets"]:
        lines.extend([
            "Risk buckets: " + ", ".join(f"`{bucket}`" for bucket in decision["risk_buckets"]),
            "",
        ])
    if not findings:
        lines.append("No lite-scan findings. This does not mean the repo is safe; it only means these simple checks did not match.")
        return "\n".join(lines) + "\n"
    for finding in findings:
        loc = finding.path if finding.line is None else f"{finding.path}:{finding.line}"
        lines.append(f"- **{finding.severity.upper()}** `{finding.kind}` at `{loc}` — {finding.detail}")
    lines.extend([
        "",
        "## Next steps",
        "",
        "- Review high-severity findings before giving an agent tool access.",
        "- Exclude or sanitize secret-adjacent files.",
        "- Read agent instruction/config files yourself before relying on them.",
        "- Treat this as a first-pass checklist, not a security audit.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Lite preflight scanner for AI-agent repo runs.")
    parser.add_argument("path", nargs="?", default=".", help="Repository/workspace path to scan")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    args = parser.parse_args()
    root = Path(args.path)
    if not root.exists():
        parser.error(f"path does not exist: {root}")
    findings = scan(root)
    display_path = str(root)
    if args.json:
        print(json.dumps({"path": display_path, "decision": classify_decision(findings), "findings": [asdict(f) for f in findings]}, indent=2))
    else:
        print(render_markdown(Path(display_path), findings))
    return 1 if any(f.severity == "high" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
