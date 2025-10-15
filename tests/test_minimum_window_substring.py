import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.minimum_window_substring.solution import Solution


class TestMinimumWindowSubstring(unittest.TestCase):
    def test_example_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(Solution.get_minimum_window(s, t), "BANC")

    def test_example_2(self):
        s = "a"
        t = "a"
        self.assertEqual(Solution.get_minimum_window(s, t), "a")

    def test_example_3(self):
        s = "a"
        t = "aa"
        self.assertEqual(Solution.get_minimum_window(s, t), "")


if __name__ == '__main__':
    unittest.main()
