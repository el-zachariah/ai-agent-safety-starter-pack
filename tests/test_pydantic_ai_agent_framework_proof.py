import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/preflight-before-pydantic-ai-agent-frameworks.md"
README = ROOT / "README.md"
INDEX = ROOT / "index.html"


class PydanticAiAgentFrameworksProofTest(unittest.TestCase):
    def test_customer_proof_markers_are_present(self):
        doc = DOC.read_text()
        readme = README.read_text()
        index = INDEX.read_text()
        for marker in [
            "PydanticAI agent-framework preflight proof",
            "PydanticAI / typed Python agent framework teams",
            "pydantic/pydantic-ai",
            "Buy the $7 pack when the free scan is Yellow/Red because your PydanticAI agent can read repo context, call tools, run package scripts, or operate near secret-adjacent files.",
            "https://payhip.com/b/1nmxV",
        ]:
            with self.subTest(marker=marker):
                self.assertIn(marker, doc)
        self.assertIn("docs/examples/preflight-before-pydantic-ai-agent-frameworks.md", readme)
        self.assertIn("PydanticAI agent-framework preflight proof", index)
        self.assertIn("Yellow/Red", doc)


if __name__ == "__main__":
    unittest.main()
