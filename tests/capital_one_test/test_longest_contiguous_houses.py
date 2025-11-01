import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.capital_one_full_time.longest_contiguous_houses.solution import solution


class TestLongestContiguousHouses(unittest.TestCase):
    def setUp(self):
        self.solution = solution()

    def test_example_case(self):
        """Test the example from the problem statement."""
        queries = [2, 1, 3, 5, 4]
        expected = [1, 2, 3, 3, 5]
        self.assertEqual(self.solution.longest_contiguous_house(queries), expected)

    def test_sequential_build(self):
        """Test building houses in sequential order."""
        queries = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.longest_contiguous_house(queries), expected)

    def test_reverse_sequential(self):
        """Test building houses in reverse sequential order."""
        queries = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.longest_contiguous_house(queries), expected)

    def test_single_house(self):
        """Test with only one house."""
        queries = [10]
        expected = [1]
        self.assertEqual(self.solution.longest_contiguous_house(queries), expected)

    def test_two_separate_segments(self):
        """Test building two separate segments."""
        queries = [1, 5, 2, 6]
        expected = [1, 1, 2, 2]
        self.assertEqual(self.solution.longest_contiguous_house(queries), expected)

    def test_merge_segments(self):
        """Test merging two separate segments."""
        queries = [1, 3, 2]
        expected = [1, 1, 3]
        self.assertEqual(self.solution.longest_contiguous_house(queries), expected)


if __name__ == '__main__':
    unittest.main()
