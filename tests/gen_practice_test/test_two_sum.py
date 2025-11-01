import unittest
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gen_practice.two_sum.two_sum_1 import two_sum_hash_map
from src.gen_practice.two_sum.two_sum_2 import two_sum_two_pointer


class TestTwoSumHashMap(unittest.TestCase):
    """Test cases for hash map approach (two_sum_1.py)"""

    def test_basic_case(self):
        """Test basic two sum case"""
        result = two_sum_hash_map([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_unsorted_array(self):
        """Test with unsorted array - hash map handles this well"""
        result = two_sum_hash_map([3, 2, 4], 6)
        self.assertEqual(result, [1, 2])
        
    def test_two_elements_valid(self):
        """Test with exactly 2 elements that sum to target"""
        result = two_sum_hash_map([1, 2], 3)
        self.assertEqual(result, [0, 1])
        
    def test_no_solution_case(self):
        """Test case where no solution exists (should raise error)"""
        with self.assertRaises(ValueError):
            two_sum_hash_map([1, 5], 7)  # 1+5≠7, no valid solution

    def test_duplicates(self):
        """Test with duplicate numbers"""
        result = two_sum_hash_map([3, 3], 6)
        self.assertEqual(result, [0, 1])

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = two_sum_hash_map([-1, -2, -3, -4, -5], -8)
        # -3 + -5 = -8, should return indices of -3 and -5
        self.assertIn(result, [[2, 4], [4, 2]])

    def test_validation_empty_array(self):
        """Test validation: empty array should raise error"""
        with self.assertRaises(ValueError):
            two_sum_hash_map([], 5)

    def test_validation_single_element(self):
        """Test validation: single element should raise error"""
        with self.assertRaises(ValueError):
            two_sum_hash_map([1], 5)
            
    def test_zero_target(self):
        """Test with zero as target"""
        result = two_sum_hash_map([-1, 0, 1], 0)
        self.assertEqual(result, [0, 2])
        
    def test_large_numbers(self):
        """Test with large numbers"""
        result = two_sum_hash_map([1000, 2000, 3000], 5000)
        self.assertEqual(result, [1, 2])


class TestTwoSumTwoPointer(unittest.TestCase):
    """Test cases for two-pointer with sorting approach (two_sum_2.py)"""

    def test_basic_case(self):
        """Test basic two sum case"""
        result = two_sum_two_pointer([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_unsorted_array(self):
        """Test with unsorted array - two pointer sorts first"""
        result = two_sum_two_pointer([3, 2, 4], 6)
        self.assertEqual(result, [1, 2])
        
    def test_two_elements_valid(self):
        """Test with exactly 2 elements that sum to target"""
        result = two_sum_two_pointer([1, 2], 3)
        self.assertEqual(result, [0, 1])
        
    def test_no_solution_case(self):
        """Test case where no solution exists (should raise error)"""
        with self.assertRaises(ValueError):
            two_sum_two_pointer([1, 5], 7)

    def test_duplicates(self):
        """Test with duplicate numbers"""
        result = two_sum_two_pointer([3, 3], 6)
        self.assertEqual(result, [0, 1])

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = two_sum_two_pointer([-1, -2, -3, -4, -5], -8)
        # -3 + -5 = -8, should return indices of -3 and -5
        self.assertIn(result, [[2, 4], [4, 2]])

    def test_validation_empty_array(self):
        """Test validation: empty array should raise error"""
        with self.assertRaises(ValueError):
            two_sum_two_pointer([], 5)

    def test_validation_single_element(self):
        """Test validation: single element should raise error"""
        with self.assertRaises(ValueError):
            two_sum_two_pointer([1], 5)
            
    def test_already_sorted_array(self):
        """Test with already sorted array"""
        result = two_sum_two_pointer([1, 2, 3, 4, 5], 9)
        self.assertEqual(result, [3, 4])
        
    def test_reverse_sorted_array(self):
        """Test with reverse sorted array"""
        result = two_sum_two_pointer([5, 4, 3, 2, 1], 9)
        self.assertEqual(result, [0, 1])  # Original indices of 5 and 4

if __name__ == '__main__':
    unittest.main()