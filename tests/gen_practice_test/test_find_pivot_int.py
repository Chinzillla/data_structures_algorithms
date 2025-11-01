import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gen_practice.find_pivot_int.solution import Solution


class TestFindPivotInteger(unittest.TestCase):
    """tests for pivotInteger"""

    def test_example_with_pivot(self):
        self.assertEqual(Solution().pivotInteger(8), 6)

    def test_single_element(self):
        self.assertEqual(Solution().pivotInteger(1), 1)

    def test_no_pivot(self):
        self.assertEqual(Solution().pivotInteger(4), -1)


if __name__ == '__main__':
    unittest.main()
