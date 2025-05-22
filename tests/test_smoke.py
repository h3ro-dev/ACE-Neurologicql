import unittest
from pathlib import Path

class TestAce(unittest.TestCase):
    def test_ace_exists(self):
        self.assertTrue(Path('ace.html').exists())

    def test_protective_factors_present(self):
        html = Path('ace.html').read_text()
        self.assertIn('id="supportiveSchool"', html)
        self.assertIn('id="peerRelationships"', html)

if __name__ == '__main__':
    unittest.main()
