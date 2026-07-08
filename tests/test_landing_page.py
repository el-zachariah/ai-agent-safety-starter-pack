from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
LANDING = ROOT / "index.html"


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.in_title = False
        self.title_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)


class LandingPageTests(unittest.TestCase):
    def test_free_scan_command_is_above_proof_wall(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        html = LANDING.read_text(encoding="utf-8")
        marker = "FREE_SCAN_FIRST_COMMAND_2026_07_07_2230"

        for text in (readme, html):
            self.assertEqual(text.count(marker), 1)
            self.assertIn("git clone https://github.com/el-zachariah/ai-agent-safety-starter-pack.git", text)
            self.assertIn("python3 agent_preflight_lite.py /path/to/repo", text)
            self.assertIn("Green", text)
            self.assertIn("Yellow/Red", text)

        self.assertLess(readme.index(marker), readme.index("## Recent buyer-specific proof links"))
        self.assertLess(html.index(marker), html.index("deadline-github-mcp-server-workflows-proof:start"))

    def test_purchase_decision_is_above_proof_wall(self):
        html = LANDING.read_text(encoding="utf-8")

        body_pos = html.index("<body>")
        header_pos = html.index("<header>")
        decision_pos = html.index('aria-label="30-second buy or skip decision"')
        first_proof_pos = html.index("deadline-github-mcp-server-workflows-proof:start")

        self.assertLess(body_pos, header_pos)
        self.assertLess(header_pos, decision_pos)
        public_verification_pos = html.index("TOP_OF_FUNNEL_PUBLIC_VERIFICATION_2026_07_07")

        self.assertLess(decision_pos, first_proof_pos)
        self.assertLess(public_verification_pos, first_proof_pos)
        self.assertLess(html.index("Buy the $7 starter pack"), first_proof_pos)
        self.assertEqual(html.count("<header>"), 1)
        self.assertEqual(html.count('aria-label="30-second buy or skip decision"'), 1)
        self.assertEqual(html.count("TOP_OF_FUNNEL_PUBLIC_VERIFICATION_2026_07_07"), 1)

    def test_landing_page_has_purchase_and_free_preview_paths(self):
        html = LANDING.read_text(encoding="utf-8")
        parser = LinkParser()
        parser.feed(html)

        self.assertIn("AI Agent Safety Starter Pack", "".join(parser.title_text))

    def test_public_copy_uses_live_payhip_price(self):
        public_paths = [ROOT / "README.md", ROOT / "index.html"] + sorted((ROOT / "docs").glob("**/*.md"))
        stale = []
        for path in public_paths:
            if "$5" in path.read_text(encoding="utf-8"):
                stale.append(str(path.relative_to(ROOT)))

        self.assertEqual([], stale, "Public buyer copy must not advertise stale $5 pricing; Payhip/listing copy uses $7.")

    def test_landing_page_has_purchase_and_free_preview_paths_continued(self):
        html = LANDING.read_text(encoding="utf-8")
        parser = LinkParser()
        parser.feed(html)

        self.assertIn("https://payhip.com/b/1nmxV", parser.links)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack", parser.links)
        self.assertIn('property="og:title"', html)
        self.assertIn('name="twitter:card" content="summary_large_image"', html)
        self.assertIn('"@type": "Product"', html)
        self.assertIn('"price": "7.00"', html)
        self.assertIn('"priceCurrency": "USD"', html)
        self.assertIn("destructive-command hook", html)
        self.assertIn("python3 agent_preflight_lite.py /path/to/repo", html)
        self.assertIn("python3 agent_preflight_lite.py examples/sample-risky-repo", html)
        self.assertIn("Try the included risky sample", html)
        self.assertIn("one-minute repo risk scorecard", html)
        self.assertIn("Green / Yellow / Red", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/one-minute-risk-scorecard.md", parser.links)
        self.assertIn("red-flag to action matrix", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/red-flag-to-action-matrix.md", parser.links)
        self.assertIn("Claude Code slash-command bridge", html)
        self.assertIn("/agent-preflight", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/claude-code-slash-command.md", parser.links)
        self.assertIn("free agent handoff playbook", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/agent-handoff-playbook.md", parser.links)
        self.assertIn("5-minute upgrade checklist", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/upgrade-decision-checklist.md", parser.links)
        self.assertIn("Copy-paste prompt for the agent task", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/copy-paste-agent-task-prompt.md", parser.links)
        self.assertIn("Free scan first, then upgrade only when it saves setup time", html)
        self.assertIn("If it flags work, use the $7 pack", html)
        self.assertIn("30-second buy / skip decision", html)
        self.assertIn("Buy the $7 pack if the scan is Yellow/Red", html)
        self.assertIn("Skip it for now if the scan is Green", html)
        self.assertIn("Verify the public trail before paying", html)
        self.assertIn("60-second public verification path", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/live-distribution-proof.md", parser.links)
        self.assertIn("MCP config preflight receipt example", html)
        self.assertIn("before the agent can read tokens", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/mcp-config-preflight-receipt-example.md", parser.links)
        self.assertIn("maintainer preflight receipt example", html)
        self.assertIn("AI-agent PRs", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/maintainer-preflight-receipt-example.md", parser.links)
        self.assertIn("Continuous Claude-style loop proof", html)
        self.assertIn("before long-running state, shell commands, and tool access begin", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/examples/preflight-before-continuous-claude.md", parser.links)
        self.assertIn("multi-harness agent marketplace preflight", html)
        self.assertIn("https://github.com/el-zachariah/ai-agent-safety-starter-pack/blob/main/docs/examples/preflight-before-multi-harness-agent-marketplaces.md", parser.links)

    def test_claude_code_action_ci_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-claude-code-action-ci.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-claude-code-action-ci.md", readme)
        self.assertIn("Claude Code GitHub Action preflight", index)
        self.assertIn("anthropics/claude-code-action", proof_text)
        self.assertIn("pull_request_target", proof_text)

    def test_vscode_agent_extension_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-vscode-agent-extensions.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-vscode-agent-extensions.md", readme)
        self.assertIn("VS Code agent extension preflight proof", index)
        self.assertIn("cline/cline", proof_text)
        self.assertIn("RooCodeInc/Roo-Code", proof_text)
        self.assertIn("MCP/tool config", proof_text)


    def test_swe_agent_autonomous_patch_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-swe-agent-autonomous-patches.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-swe-agent-autonomous-patches.md", readme)
        self.assertIn("SWE-agent autonomous patch preflight", index)
        self.assertIn("SWE-agent/SWE-agent", proof_text)
        self.assertIn("autonomous issue-to-patch", proof_text)
        self.assertIn("agent-preflight-swe-agent", proof_text)



    def test_opencode_terminal_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-opencode-terminal-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-opencode-terminal-agents.md", readme)
        self.assertIn("OpenCode terminal-agent preflight proof", index)
        self.assertIn("anomalyco/opencode", proof_text)
        self.assertIn("agent-preflight-opencode", proof_text)
        self.assertIn("The open source coding agent.", proof_text)


    def test_e2b_code_interpreter_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-e2b-code-interpreter-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-e2b-code-interpreter-agents.md", readme)
        self.assertIn("E2B code-interpreter agent preflight proof", index)
        self.assertIn("e2b-dev/", proof_text)
        self.assertIn("E2B_API_KEY", proof_text)
        self.assertIn("agent-preflight", proof_text)

    def test_continue_ide_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-continue-ide-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-continue-ide-agents.md", readme)
        self.assertIn("Continue.dev IDE agent preflight proof", index)
        self.assertIn("continuedev/continue", proof_text)
        self.assertIn(".continue/", proof_text)
        self.assertIn("MCP/context providers", proof_text)



class LangGraphStatefulAgentProofTests(unittest.TestCase):
    def test_langgraph_stateful_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-langgraph-stateful-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-langgraph-stateful-agents.md", readme)
        self.assertIn("LangGraph stateful-agent preflight proof", index)
        self.assertIn("langchain-ai/langgraph", proof_text)
        self.assertIn("checkpoint stores", proof_text)
        self.assertIn("agent-preflight-langgraph", proof_text)



class OpenHandsTaskBranchProofTests(unittest.TestCase):
    def test_openhands_task_branch_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-openhands-task-branches.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-openhands-task-branches.md", readme)
        self.assertIn("OpenHands task-branch preflight proof", index)
        self.assertIn("OpenHands/OpenHands", proof_text)
        self.assertIn("preflight-openhands", proof_text)
        self.assertIn("package-script", proof_text)


if __name__ == "__main__":
    unittest.main()


class LiveDistributionProofTests(unittest.TestCase):
    def test_live_distribution_proof_is_linked_and_specific(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        proof = (ROOT / "docs/live-distribution-proof.md").read_text(encoding="utf-8")

        self.assertIn("docs/live-distribution-proof.md", readme)
        self.assertIn("live-distribution-proof", index)
        marker = "LIVE_DISTRIBUTION_PROOF_REFRESH_2026_07_07_SENTINEL_1759"
        strict_plugin_marker = "STRICT_PLUGIN_ROUTE_MERGEABLE_READBACK_2026_07_07_1937"
        strict_plugin_current_head_marker = "STRICT_PLUGIN_ROUTE_GREEN_RECHECK_2026_07_08_0142"
        current_marker = "LIVE_DISTRIBUTION_TRUST_REFRESH_2026_07_08_0412"
        harness_clean_marker = "HARNESS_ROUTE_CLEAN_RECHECK_2026_07_08_0735"
        strict_plugin_public_api_marker = "STRICT_PLUGIN_ROUTE_PUBLIC_API_GREEN_RECHECK_2026_07_08_0843"
        jqueryscript_public_api_marker = "JQUERYSCRIPT_ROUTE_CLEAN_RECHECK_2026_07_08_1053"
        self.assertIn(marker, readme)
        self.assertIn(marker, index)
        self.assertIn(marker, proof)
        self.assertIn(strict_plugin_marker, readme)
        self.assertIn(strict_plugin_marker, index)
        self.assertIn(strict_plugin_marker, proof)
        self.assertIn(strict_plugin_current_head_marker, readme)
        self.assertIn(strict_plugin_current_head_marker, index)
        self.assertIn(strict_plugin_current_head_marker, proof)
        self.assertIn(current_marker, readme)
        self.assertIn(current_marker, index)
        self.assertIn(current_marker, proof)
        self.assertIn(harness_clean_marker, readme)
        self.assertIn(harness_clean_marker, index)
        self.assertIn(harness_clean_marker, proof)
        self.assertIn(strict_plugin_public_api_marker, readme)
        self.assertIn(strict_plugin_public_api_marker, index)
        self.assertIn(strict_plugin_public_api_marker, proof)
        self.assertIn(jqueryscript_public_api_marker, readme)
        self.assertIn(jqueryscript_public_api_marker, index)
        self.assertIn(jqueryscript_public_api_marker, proof)
        self.assertIn("Live public distribution proof", readme)
        self.assertLess(readme.index("Live public distribution proof"), readme.index("## Recent buyer-specific proof links"))
        self.assertIn("Three checks before checkout", proof)
        self.assertIn("60-second public verification path", proof)
        self.assertIn("top README points cautious buyers toward the merged, CLA-green, harness-clean, jqueryscript-clean, and strict-plugin proof routes", index)
        self.assertIn("above the long proof wall", proof)
        self.assertIn("merged Claude Code directory route", proof)
        self.assertIn("CLA-green security-org skill marketplace route", proof)
        self.assertIn("One route is merged after maintainer review", proof)
        self.assertIn("fifteen tracked routes are open and mergeable", proof)
        self.assertIn("PUBLIC_ROUTE_READBACK_2026_07_07_1801", proof)
        self.assertIn("2026-07-08T04:12:35-05:00", proof)
        self.assertIn("fifteen tracked routes remain `OPEN` + `MERGEABLE`", proof)
        self.assertIn("harness-engineering route was rechecked clean after a transient unknown state", proof)
        self.assertIn("mergeable clean after the 07:33 sentinel unknown-mergeability alert", proof)
        self.assertIn("c24639cc881bce5242df137f40c31529d363bde6", proof)
        self.assertIn("jqueryscript route was rechecked clean at head `07a8f07fc12f`", proof)
        self.assertIn("2026-07-08T10:53:14-05:00", proof)
        self.assertIn("public GitHub API `mergeable=true` with `mergeable_state` `clean`", proof)
        self.assertIn("stricter plugin marketplace route is `OPEN`, GitHub API `mergeable=true`", proof)
        self.assertIn("head `7a4239ff0e30`", proof)
        self.assertIn("public checks include `prescreen`, `prescreen-grade`, and `Greptile Review` success", proof)
        self.assertIn("GitHub API `mergeable=true`", proof)
        self.assertIn("mergeable_state` `unstable`", proof)
        self.assertIn("latest owner maintainer-ready readback comment at `2026-07-08T02:52:12Z`", proof)
        self.assertIn("PASS: 1 skill(s) inspected", proof)
        self.assertIn("`CHANGES_REQUESTED` until maintainer re-review", proof)
        self.assertIn("CLOSED after review comment at `2026-07-07T15:39:45Z`", proof)
        self.assertIn("no longer counted as active buyer proof", proof)

        self.assertIn("Greptile Review", proof)
        self.assertIn("payhip.com/b/1nmxV", proof)
        self.assertIn("github.com/e2b-dev/awesome-ai-sdks/pull/261", proof)
        self.assertIn("github.com/davepoon/buildwithclaude/pull/224", proof)
        self.assertIn("CodeRabbit success", proof)


class AutoGenAgentWorkflowProofTests(unittest.TestCase):
    def test_autogen_agent_workflow_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-autogen-agent-workflows.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-autogen-agent-workflows.md", readme)
        self.assertIn("AutoGen multi-agent workflow preflight proof", index)
        self.assertIn("microsoft/autogen", proof_text)
        self.assertIn("function-calling agents", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", index)



class SmolagentsToolAgentProofTests(unittest.TestCase):
    def test_smolagents_tool_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-smolagents-tool-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-smolagents-tool-agents.md", readme)
        self.assertIn("smolagents tool-running agent preflight proof", index)
        self.assertIn("huggingface/smolagents", proof_text)
        self.assertIn("CodeAgent", proof_text)
        self.assertIn("agent-preflight-smolagents", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


class PydanticAIAgentProofTests(unittest.TestCase):
    def test_pydantic_ai_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-pydantic-ai-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-pydantic-ai-agents.md", readme)
        self.assertIn("Pydantic AI production-agent preflight proof", index)
        self.assertIn("pydantic/pydantic-ai", proof_text)
        self.assertIn("agent-preflight-pydantic-ai", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


class MastraTypeScriptAgentProofTests(unittest.TestCase):
    def test_mastra_typescript_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-mastra-typescript-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-mastra-typescript-agents.md", readme)
        self.assertIn("Mastra TypeScript agent preflight proof", index)
        self.assertIn("mastra-ai/mastra", proof_text)
        self.assertIn("agent-preflight-mastra", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


class DevContainerCodespacesAgentProofTests(unittest.TestCase):
    def test_devcontainer_codespaces_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-devcontainer-codespaces-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-devcontainer-codespaces-agents.md", readme)
        self.assertIn("Dev Containers / Codespaces agent preflight proof", index)
        self.assertIn("devcontainers/spec", proof_text)
        self.assertIn("postCreateCommand", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)
class MarketplacePrReviewerProofTests(unittest.TestCase):
    def test_marketplace_pr_reviewer_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-marketplace-pr-reviewers.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-marketplace-pr-reviewers.md", readme)
        self.assertIn("marketplace PR reviewer preflight proof", index)
        self.assertIn("wshobson/agents", proof_text)
        self.assertIn("numman-ali/n-skills", proof_text)
        self.assertIn("Marketplace PR preflight receipt", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


class CursorRulesBackgroundAgentProofTests(unittest.TestCase):
    def test_cursor_rules_background_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-cursor-rules-background-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-cursor-rules-background-agents.md", readme)
        self.assertIn("Cursor rules / background-agent preflight proof", index)
        self.assertIn("cursor/cursor", proof_text)
        self.assertIn("PatrickJS/awesome-cursorrules", proof_text)
        self.assertIn("agent-preflight-cursor-rules", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)

class CuratedClaudeSkillMarketplaceProofTests(unittest.TestCase):
    def test_curated_claude_skill_marketplace_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-curated-claude-skill-marketplaces.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-curated-claude-skill-marketplaces.md", readme)
        self.assertIn("Curated Claude skill marketplace preflight proof", index)
        self.assertIn("trailofbits/skills-curated", proof_text)
        self.assertIn("numman-ali/n-skills", proof_text)
        self.assertIn("agent-preflight-curated-skills", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)

class RufloAgentSwarmProofTests(unittest.TestCase):
    def test_ruflo_agent_swarm_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-ruflo-agent-swarms.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-ruflo-agent-swarms.md", readme)
        self.assertIn("Ruflo / Claude Flow-style swarm preflight proof", index)
        self.assertIn("ruvnet/ruflo", proof_text)
        self.assertIn("agent-preflight-ruflo-swarm", proof_text)
        self.assertIn("multi-agent meta-harness", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)

class SemanticKernelAgentProofTests(unittest.TestCase):
    def test_semantic_kernel_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-semantic-kernel-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-semantic-kernel-agents.md", readme)
        self.assertIn("Semantic Kernel agent framework preflight proof", index)
        self.assertIn("microsoft/semantic-kernel", proof_text)
        self.assertIn("Kernel plugins/functions", proof_text)
        self.assertIn("agent-preflight-semantic-kernel", proof_text)


class ComposioToolAgentProofTests(unittest.TestCase):
    def test_composio_tool_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-composio-tool-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-composio-tool-agents.md", readme)
        self.assertIn("Composio tool-integration agent preflight proof", index)
        self.assertIn("ComposioHQ/composio", proof_text)
        self.assertIn("agent-preflight-composio", proof_text)
        self.assertIn("1000+ toolkits", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


class RooCodeAgentTeamProofTests(unittest.TestCase):
    def test_roo_code_agent_team_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-roo-code-agent-teams.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-roo-code-agent-teams.md", readme)
        self.assertIn("Roo Code agent-team preflight proof", index)
        self.assertIn("RooCodeInc/Roo-Code", proof_text)
        self.assertIn("agent-preflight-roo-code", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)

class HumanLayerAgentApprovalProofTests(unittest.TestCase):
    def test_humanlayer_agent_approval_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-humanlayer-agent-approval-workflows.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-humanlayer-agent-approval-workflows.md", readme)
        self.assertIn("HumanLayer-style agent approval preflight proof", index)
        self.assertIn("humanlayer/humanlayer", proof_text)
        self.assertIn("human-in-the-loop", proof_text)
        self.assertIn("agent-preflight-humanlayer", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


class VercelAiSdkAgentProofTests(unittest.TestCase):
    def test_vercel_ai_sdk_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-vercel-ai-sdk-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-vercel-ai-sdk-agents.md", readme)
        self.assertIn("Vercel AI SDK tool-calling agent preflight proof", index)
        self.assertIn("vercel/ai", proof_text)
        self.assertIn("agent-preflight-vercel-ai-sdk", proof_text)
        self.assertIn("preview/deploy settings", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)


class AgentClientProtocolAgentProofTests(unittest.TestCase):
    def test_agent_client_protocol_agent_proof_is_linked(self):
        proof = ROOT / "docs/examples/preflight-before-agent-client-protocol-agents.md"
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = LANDING.read_text(encoding="utf-8")
        proof_text = proof.read_text(encoding="utf-8")

        self.assertIn("preflight-before-agent-client-protocol-agents.md", readme)
        self.assertIn("Agent Client Protocol agent preflight proof", index)
        self.assertIn("agentclientprotocol/agent-client-protocol", proof_text)
        self.assertIn("ACP agent preflight receipt", proof_text)
        self.assertIn("https://payhip.com/b/1nmxV", proof_text)
