import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.digital_root_freq.solution import Solution


class TestDigitalRootFreq(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        """Test the example from the problem statement."""
        numbers = [38, 29, 47, 156, 99]
        # 38→11→2, 29→11→2, 47→11→2, 156→12→3, 99→18→9
        # Frequency: {2:3, 3:1, 9:1}
        self.assertEqual(self.solution.digital_root_freq(numbers), 2)

    def test_tie_returns_highest_digit(self):
        """When frequencies are tied, return the highest digit."""
        numbers = [12, 21, 45, 54]
        # 12→3, 21→3, 45→9, 54→9
        # Frequency: {3:2, 9:2} - tied, so return 9
        self.assertEqual(self.solution.digital_root_freq(numbers), 9)

    def test_single_digit_numbers(self):
        """Test with numbers that are already single digits."""
        numbers = [1, 2, 3, 2, 2]
        # All are already single digits
        # Frequency: {1:1, 2:3, 3:1}
        self.assertEqual(self.solution.digital_root_freq(numbers), 2)

    def test_all_same_digital_root(self):
        """Test when all numbers have the same digital root."""
        numbers = [11, 20, 38]
        # 11→2, 20→2, 38→11→2
        # Frequency: {2:3}
        self.assertEqual(self.solution.digital_root_freq(numbers), 2)

    def test_large_numbers(self):
        """Test with large numbers."""
        numbers = [999, 888, 777]
        # 999→27→9, 888→24→6, 777→21→3
        # Frequency: {9:1, 6:1, 3:1} - all tied, return 9
        self.assertEqual(self.solution.digital_root_freq(numbers), 9)


if __name__ == '__main__':
    unittest.main()