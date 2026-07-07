from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-vibe-kanban-coding-agent-task-boards.md'
README = ROOT / 'README.md'
INDEX = ROOT / 'index.html'

class VibeKanbanCodingAgentTaskBoardsProofTest(unittest.TestCase):
    def test_segment_proof_markers_are_linked(self):
        doc = DOC.read_text()
        readme = README.read_text()
        index = INDEX.read_text()
        self.assertIn('VIBE_KANBAN_CODING_AGENT_TASK_BOARD_PROOF', doc)
        self.assertIn('BloopAI/vibe-kanban', doc)
        self.assertIn('https://payhip.com/b/1nmxV', doc)
        self.assertIn('docs/examples/preflight-before-vibe-kanban-coding-agent-task-boards.md', readme)
        self.assertIn('docs/examples/preflight-before-vibe-kanban-coding-agent-task-boards.md', index)
        self.assertIn('VIBE_KANBAN_CODING_AGENT_TASK_BOARD_PROOF', readme + index)

if __name__ == '__main__':
    unittest.main()
