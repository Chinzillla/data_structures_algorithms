import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.gen_practice.num_of_submatrices_sum_target.solution import Solution


class TestNumSubmatrixSumTarget(unittest.TestCase):
    def test_example_zeros(self):
        matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        self.assertEqual(Solution().numSubmatrixSumTarget(matrix, 0), 4)

    def test_example_mixed(self):
        matrix = [[1, -1], [-1, 1]]
        self.assertEqual(Solution().numSubmatrixSumTarget(matrix, 0), 5)

    def test_single_cell_no_match(self):
        matrix = [[904]]
        self.assertEqual(Solution().numSubmatrixSumTarget(matrix, 0), 0)


if __name__ == '__main__':
    unittest.main()