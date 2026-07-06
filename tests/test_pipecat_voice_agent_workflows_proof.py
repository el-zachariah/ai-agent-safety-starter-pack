import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class PipecatVoiceAgentWorkflowsProofTest(unittest.TestCase):
    def test_public_buyer_proof_markers(self):
        doc = (ROOT / 'docs/examples/preflight-before-pipecat-voice-agent-workflows.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        landing = (ROOT / 'index.html').read_text(encoding='utf-8')
        for text in (doc, readme, landing):
            self.assertIn('PIPECAT_VOICE_AGENT_PROOF', text)
            self.assertIn('https://payhip.com/b/1nmxV', text)
        self.assertIn('pipecat-ai/pipecat', doc)
        self.assertIn('https://github.com/pipecat-ai/pipecat', doc)
        self.assertIn('docs/examples/preflight-before-pipecat-voice-agent-workflows.md', readme)
        self.assertIn('docs/examples/preflight-before-pipecat-voice-agent-workflows.md', landing)
        self.assertIn('Yellow/Red', doc)
        self.assertIn('secret-adjacent', doc)
if __name__ == '__main__':
    unittest.main()
