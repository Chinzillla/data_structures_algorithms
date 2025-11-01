import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gen_practice.subarray_sum import subarray_sum

class TestSubarraySum(unittest.TestCase):
    def test_basic_case(self):
        result = subarray_sum.subarray_sum([1,-20,-3,30,5,4], 7)
        self.assertEqual(result, (1,4))


