import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.range_sum_query_2d_immutable.soluition import NumMatrix


class TestNumMatrix(unittest.TestCase):
    """Test cases for NumMatrix class (2D range sum queries)."""

    def test_basic_case(self):
        """Test basic 2x2 matrix with full range sum."""
        matrix = [[1, 2], [3, 4]]
        obj = NumMatrix(matrix)
        result = obj.sumRegion(0, 0, 1, 1)
        self.assertEqual(result, 10)  # 1+2+3+4

    def test_single_cell(self):
        """Test sum of single cell."""
        matrix = [[1, 2], [3, 4]]
        obj = NumMatrix(matrix)
        result = obj.sumRegion(0, 0, 0, 0)
        self.assertEqual(result, 1)

    def test_partial_range(self):
        """Test sum of top-left submatrix."""
        matrix = [[1, 2], [3, 4]]
        obj = NumMatrix(matrix)
        result = obj.sumRegion(0, 0, 0, 1)
        self.assertEqual(result, 3)  # 1+2

    def test_larger_matrix(self):
        """Test with larger matrix."""
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ]
        obj = NumMatrix(matrix)
        result = obj.sumRegion(2, 1, 4, 3)
        self.assertEqual(result, 8)  # Sum of specified submatrix

    def test_empty_matrix(self):
        """Test with empty matrix."""
        matrix = []
        obj = NumMatrix(matrix)
        # sumRegion would need valid indices, but this tests initialization
        self.assertEqual(obj._prefix, [])

    def test_negative_numbers(self):
        """Test with negative numbers."""
        matrix = [[-1, 2], [3, -4]]
        obj = NumMatrix(matrix)
        result = obj.sumRegion(0, 0, 1, 1)
        self.assertEqual(result, 0)  # -1+2+3-4


if __name__ == '__main__':
    unittest.main()