from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/examples/preflight-before-jetbrains-koog-jvm-agents.md'


class JetBrainsKoogJVMAgentProofTests(unittest.TestCase):
    def test_named_koog_proof_doc_has_segment_and_buy_trigger(self):
        text = DOC.read_text(encoding='utf-8')
        self.assertIn('Preflight before JetBrains Koog JVM/Kotlin agent workflows', text)
        self.assertIn('JetBrains/koog', text)
        self.assertIn('JETBRAINS_KOOG_JVM_AGENT_PROOF', text)
        self.assertIn('https://payhip.com/b/1nmxV', text)
        self.assertIn('Yellow', text)
        self.assertIn('Red', text)
        self.assertIn('Green', text)

    def test_named_koog_proof_linked_from_readme_and_landing_page(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        index = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn('docs/examples/preflight-before-jetbrains-koog-jvm-agents.md', readme)
        self.assertIn('JetBrains Koog JVM/Kotlin agent preflight proof', readme)
        self.assertIn('docs/examples/preflight-before-jetbrains-koog-jvm-agents.md', index)
        self.assertIn('JETBRAINS_KOOG_JVM_AGENT_PROOF', index)


if __name__ == '__main__':
    unittest.main()
