import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gen_practice.two_sum_II.two_sum_II import two_sum_II


class TestTwoSumII(unittest.TestCase):
    """
    Test cases for Two Sum II - Input Array Is Sorted
    
    This problem assumes:
    - Input array is sorted in non-decreasing order
    - Exactly one solution exists
    - Returns 1-indexed positions (not 0-indexed)
    """

    def test_basic_case(self):
        """Test basic example from LeetCode"""
        result = two_sum_II([2, 7, 11, 15], 9)
        self.assertEqual(result, [1, 2])

    def test_three_elements(self):
        """Test with three elements"""
        result = two_sum_II([2, 3, 4], 6)
        self.assertEqual(result, [1, 3])

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = two_sum_II([-1, 0], -1)
        self.assertEqual(result, [1, 2])

    def test_all_negative(self):
        """Test with all negative numbers"""
        result = two_sum_II([-10, -5, -3, -1], -8)
        self.assertEqual(result, [2, 3])  # -5 + -3 = -8

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        result = two_sum_II([-3, -1, 0, 2, 4, 5], 1)
        self.assertEqual(result, [1, 5])  # -3 + 4 = 1 (index 1, 5 in 1-indexed)

    def test_two_elements_only(self):
        """Test with exactly two elements"""
        result = two_sum_II([1, 2], 3)
        self.assertEqual(result, [1, 2])

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        result = two_sum_II([1, 2, 3, 3, 4], 6)
        self.assertEqual(result, [2, 5])  # 2 + 4 = 6

    def test_same_number_twice(self):
        """Test when answer uses same value twice"""
        result = two_sum_II([3, 3], 6)
        self.assertEqual(result, [1, 2])

    def test_large_numbers(self):
        """Test with large numbers"""
        result = two_sum_II([1000, 2000, 3000, 4000], 7000)
        self.assertEqual(result, [3, 4])  # 3000 + 4000 = 7000

    def test_zero_target(self):
        """Test with zero as target"""
        result = two_sum_II([-5, -3, 0, 3, 5], 0)
        self.assertEqual(result, [1, 5])  # -5 + 5 = 0

    def test_first_and_last(self):
        """Test when solution is first and last elements"""
        result = two_sum_II([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, [1, 5])  # 1 + 5 = 6

    def test_adjacent_elements(self):
        """Test when solution is adjacent elements"""
        result = two_sum_II([1, 3, 4, 5, 7], 7)
        self.assertEqual(result, [2, 3])  # 3 + 4 = 7

    def test_large_array(self):
        """Test with larger sorted array"""
        nums = list(range(1, 101))  # [1, 2, 3, ..., 100]
        result = two_sum_II(nums, 150)
        self.assertEqual(result, [50, 100])  # 50 + 100 = 150

    def test_multiple_zeros(self):
        """Test with multiple zeros"""
        result = two_sum_II([-2, 0, 0, 2], 0)
        self.assertEqual(result, [1, 4])  # -2 + 2 = 0

    def test_target_larger_than_sum_of_largest(self):
        """Test when no solution exists (should raise ValueError)"""
        with self.assertRaises(ValueError):
            two_sum_II([1, 2, 3, 4], 100)

    def test_target_smaller_than_sum_of_smallest(self):
        """Test when target is too small (should raise ValueError)"""
        with self.assertRaises(ValueError):
            two_sum_II([10, 20, 30, 40], 5)

    def test_consecutive_numbers(self):
        """Test with consecutive numbers"""
        result = two_sum_II([5, 6, 7, 8, 9], 15)
        self.assertEqual(result, [2, 5])  # 6 + 9 = 15

    def test_all_same_numbers(self):
        """Test with all same numbers"""
        result = two_sum_II([5, 5, 5, 5], 10)
        self.assertEqual(result, [1, 4])  # 5 + 5 = 10 (first and last)

    def test_negative_target(self):
        """Test with negative target"""
        result = two_sum_II([-10, -8, -5, -3, -1], -13)
        self.assertEqual(result, [1, 4])  # -10 + -3 = -13

    def test_very_close_numbers(self):
        """Test with numbers very close together"""
        result = two_sum_II([1, 1, 1, 2, 2, 2, 3], 4)
        self.assertEqual(result, [1, 7])  # 1 + 3 = 4


class TestTwoSumIIEdgeCases(unittest.TestCase):
    """Edge cases and boundary conditions for Two Sum II"""

    def test_minimum_input_size(self):
        """Test with minimum valid input (2 elements)"""
        result = two_sum_II([0, 0], 0)
        self.assertEqual(result, [1, 2])

    def test_pointer_movement_left_only(self):
        """Test case where mostly left pointer moves"""
        result = two_sum_II([1, 2, 3, 100], 101)
        self.assertEqual(result, [1, 4])  # 1 + 100 = 101

    def test_pointer_movement_right_only(self):
        """Test case where mostly right pointer moves"""
        result = two_sum_II([1, 99, 100, 101], 100)
        self.assertEqual(result, [1, 2])  # 1 + 99 = 100

    def test_answer_in_middle(self):
        """Test when answer is in the middle of array"""
        result = two_sum_II([1, 2, 5, 6, 7, 8, 9, 10], 11)
        self.assertEqual(result, [1, 8])  # 1 + 10 = 11

    def test_large_range_values(self):
        """Test with large range between values"""
        result = two_sum_II([1, 1000, 2000, 10000], 11000)
        self.assertEqual(result, [2, 4])  # 1000 + 10000 = 11000


class TestTwoSumIIPerformance(unittest.TestCase):
    """Performance and algorithmic correctness tests"""

    def test_efficiency_large_array(self):
        """Test efficiency with large array (should be O(n))"""
        nums = list(range(1, 10001))  # [1, 2, ..., 10000]
        
        result = two_sum_II(nums, 19999)
        self.assertEqual(result, [9999, 10000])  # 9999 + 10000 = 19999

    def test_worst_case_scenario(self):
        """Test worst case where pointers traverse entire array"""
        nums = list(range(1, 1001))  # [1, 2, ..., 1000]
        result = two_sum_II(nums, 1001)
        self.assertEqual(result, [1, 1000])  # 1 + 1000 = 1001


if __name__ == '__main__':
    unittest.main(verbosity=2)
