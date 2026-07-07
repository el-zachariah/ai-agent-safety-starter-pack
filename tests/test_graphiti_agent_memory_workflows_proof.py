from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GraphitiAgentMemoryWorkflowsProofTest(unittest.TestCase):
    def test_customer_proof_markers(self):
        doc = (ROOT / 'docs/examples/preflight-before-graphiti-agent-memory-workflows.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        required_doc = [
            'Graphiti agent-memory workflow preflight proof',
            'GRAPHITI_AGENT_MEMORY_WORKFLOW_PROOF',
            'getzep/graphiti',
            'Green / Yellow / Red',
            'https://payhip.com/b/1nmxV',
        ]
        for marker in required_doc:
            self.assertIn(marker, doc)
        self.assertIn('docs/examples/preflight-before-graphiti-agent-memory-workflows.md', readme)
        self.assertIn('GRAPHITI_AGENT_MEMORY_WORKFLOW_PROOF', readme)
        self.assertIn('docs/examples/preflight-before-graphiti-agent-memory-workflows.md', index)
        self.assertIn('GRAPHITI_AGENT_MEMORY_WORKFLOW_PROOF', index)
        self.assertIn('Get the $7 pack', index)


if __name__ == '__main__':
    unittest.main()
