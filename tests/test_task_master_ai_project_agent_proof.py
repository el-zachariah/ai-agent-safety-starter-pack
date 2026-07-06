import unittest
from pathlib import Path


class TestTaskMasterAIProjectAgentProof(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.doc = (cls.root / "docs/examples/preflight-before-task-master-ai-project-agents.md").read_text()
        cls.readme = (cls.root / "README.md").read_text()
        cls.index = (cls.root / "index.html").read_text()

    def test_doc_has_customer_and_buy_trigger(self):
        for marker in ["TASK_MASTER_AI_PROJECT_AGENT_PROOF", "eyaltoledano/claude-task-master", ".taskmaster/", "https://payhip.com/b/1nmxV", "Yellow", "Red"]:
            self.assertIn(marker, self.doc)

    def test_readme_links_named_proof(self):
        self.assertIn("docs/examples/preflight-before-task-master-ai-project-agents.md", self.readme)
        self.assertIn("TASK_MASTER_AI_PROJECT_AGENT_PROOF", self.readme)
        self.assertIn("Task Master AI", self.readme)

    def test_landing_page_links_named_proof(self):
        self.assertIn("docs/examples/preflight-before-task-master-ai-project-agents.md", self.index)
        self.assertIn("TASK_MASTER_AI_PROJECT_AGENT_PROOF", self.index)
        self.assertIn("Get the reusable $7 workflow", self.index)


if __name__ == "__main__":
    unittest.main()
