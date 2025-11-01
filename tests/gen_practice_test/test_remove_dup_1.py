import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gen_practice.remove_duplicate.remove_dup_1 import remove_duplicates

class TestRemoveDuplicate(unittest.TestCase):
    
    def test_basic_case(self):
        self.assertEqual(remove_duplicates([1,2,3,4,4,5,6]), 6)

    def test_large_num_case(self):
        self.assertEqual(remove_duplicates([99, 100, 100]), 2)

    def test_all_dup_case(self):
        self.assertEqual(remove_duplicates([1,1,1,1,1,1,1,1,1]), 1)

    def test_basic_2_case(self):
        self.assertEqual(remove_duplicates([0,0,1,1,1,2,2,3,3,4]), 5)

    def test_negatives_case(self):
        self.assertEqual(remove_duplicates([-100, -100, -100, -50, -20, -10]), 4)