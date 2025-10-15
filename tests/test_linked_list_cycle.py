import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lined_list_cycle.solution import Node, Solution


class TestLinkedListCycle(unittest.TestCase):
    def test_no_cycle(self):
        # 1 -> 2 -> 3 -> None
        n3 = Node(3)
        n2 = Node(2, n3)
        n1 = Node(1, n2)
        self.assertFalse(Solution.has_cycle(n1))

    def test_cycle(self):
        # 1 -> 2 -> 3 -> 2 ...
        n3 = Node(3)
        n2 = Node(2)
        n1 = Node(1, n2)
        n2.next = n3
        n3.next = n2  # cycle
        self.assertTrue(Solution.has_cycle(n1))

    def test_single_node_cycle(self):
        n1 = Node(1)
        n1.next = n1
        self.assertTrue(Solution.has_cycle(n1))


if __name__ == '__main__':
    unittest.main()
