import unittest
from pathlib import Path

class TestAce(unittest.TestCase):
    def test_ace_exists(self):
        self.assertTrue(Path('ace.html').exists())

if __name__ == '__main__':
    unittest.main()
