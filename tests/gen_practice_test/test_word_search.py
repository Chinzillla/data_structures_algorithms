import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gen_practice.word_search.solution import Solution


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test basic case where word exists."""
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))

    def test_example_2(self):
        """Test shorter word that exists."""
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_example_3(self):
        """Test word that doesn't exist (reuses cell)."""
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))

    def test_single_cell_match(self):
        """Test single cell board with matching word."""
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solution.exist(board, word))

    def test_single_cell_no_match(self):
        """Test single cell board with non-matching word."""
        board = [["A"]]
        word = "B"
        self.assertFalse(self.solution.exist(board, word))

    def test_word_longer_than_board(self):
        """Test when word is longer than total cells."""
        board = [["A","B"],["C","D"]]
        word = "ABCDE"
        self.assertFalse(self.solution.exist(board, word))

    def test_snake_pattern(self):
        """Test word that requires zigzag path."""
        board = [["A","B","C"],["D","E","F"],["G","H","I"]]
        word = "ABCFEDGHI"
        self.assertTrue(self.solution.exist(board, word))

    def test_all_same_characters(self):
        """Test board with all same characters."""
        board = [["A","A","A"],["A","A","A"],["A","A","A"]]
        word = "AAAAAAA"
        self.assertTrue(self.solution.exist(board, word))


if __name__ == '__main__':
    unittest.main()
