from tictactoe import main
import unittest

class TestInput(unittest.TestCase):
    def test_board(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
        
if __name__ == '__main__':
    unittest.main()