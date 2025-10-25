import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.range_sum_query_immutable.solution import solution


class TestRangeSumQueryImmutable(unittest.TestCase):
    def test_initialize_prefix_arr(self):
        nums = [1, 2, 3]
        self.assertEqual(solution.initialize_prefix_arr(nums), [0, 1, 3, 6])

    def test_range_sum_query(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(solution.range_sum_query_immutable(nums, 1, 2), 5)  # 2+3
        self.assertEqual(solution.range_sum_query_immutable(nums, 0, 3), 10) # full sum
        self.assertEqual(solution.range_sum_query_immutable(nums, 2, 2), 3)  # single element

if __name__ == '__main__':
    unittest.main()