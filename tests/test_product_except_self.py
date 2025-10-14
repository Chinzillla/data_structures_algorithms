import unittest
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.product_except_self.solution import Solution


class TestProductExceptSelf(unittest.TestCase):
    """Test cases for Product of Array Except Self (solution.py)"""

    def test_basic_case(self):
        """Test basic case with positive numbers"""
        solution = Solution()
        result = solution.productExceptSelf([1, 2, 3, 4])
        self.assertEqual(result, [24, 12, 8, 6])

    def test_with_zero(self):
        """Test with one zero in the array"""
        solution = Solution()
        result = solution.productExceptSelf([1, 2, 0, 4])
        self.assertEqual(result, [0, 0, 8, 0])

    def test_all_zeros(self):
        """Test with all zeros"""
        solution = Solution()
        result = solution.productExceptSelf([0, 0, 0])
        self.assertEqual(result, [0, 0, 0])

    def test_single_element(self):
        """Test with single element"""
        solution = Solution()
        result = solution.productExceptSelf([5])
        self.assertEqual(result, [1])

    def test_negative_numbers(self):
        """Test with negative numbers"""
        solution = Solution()
        result = solution.productExceptSelf([-1, 1, 0, -3, 3])
        # Calculations: i=0: 1*0*(-3)*3=0, i=1: -1*0*(-3)*3=0, i=2: -1*1*(-3)*3=9, i=3: -1*1*0*3=0, i=4: -1*1*0*(-3)=0
        self.assertEqual(result, [0, 0, 9, 0, 0])

    def test_two_elements(self):
        """Test with two elements"""
        solution = Solution()
        result = solution.productExceptSelf([2, 3])
        self.assertEqual(result, [3, 2])

    def test_large_numbers(self):
        """Test with larger numbers to ensure no overflow issues"""
        solution = Solution()
        result = solution.productExceptSelf([10, 20, 30])
        self.assertEqual(result, [600, 300, 200])


if __name__ == '__main__':
    unittest.main()