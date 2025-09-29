import unittest
import sys

sys.path.append('../')

from src.two_sum import Solution

class TestTwoSum(unittest.TestCase):
    
    def setUp(self):
        """Set up test instance"""
        self.solution = Solution()

    def test_basic_case(self):
        """Test basic two sum case"""
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])
        
    def test_two_elements_valid(self):
        """Test with exactly 2 elements that sum to target"""
        result = self.solution.twoSum([1, 2], 3)
        self.assertEqual(result, [0, 1])
        
    def test_no_solution_case(self):
        """Test case where no solution exists (should raise error)"""
        with self.assertRaises(ValueError):
            result = self.solution.twoSum([1, 5], 7)  # 1+5≠7, no valid solution
            
    def test_duplicates(self):
        """Test with duplicate numbers"""
        result = self.solution.twoSum([3, 3], 6)
        self.assertEqual(result, [0, 1])
        
    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = self.solution.twoSum([-1, -2, -3, -4, -5], -8)
        # -3 + -5 = -8, should return indices of -3 and -5
        self.assertIn(result, [[2, 4], [4, 2]])
        
    def test_validation_empty_array(self):
        """Test validation: empty array should raise error"""
        with self.assertRaises(ValueError):
            self.solution.twoSum([], 5)
            
    def test_validation_single_element(self):
        """Test validation: single element should raise error"""
        with self.assertRaises(ValueError):
            self.solution.twoSum([1], 5)

if __name__ == '__main__':
    unittest.main()