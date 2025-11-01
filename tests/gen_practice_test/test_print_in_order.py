import os
import sys
import unittest
import threading
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.gen_practice.print_in_order.solution import Foo


class TestPrintInOrder(unittest.TestCase):
    def test_print_in_order(self):
        foo = Foo()
        result = []
        
        def print_first():
            result.append("first")
        
        def print_second():
            result.append("second")
            
        def print_third():
            result.append("third")
        
        # Start threads in reverse order to test synchronization
        t3 = threading.Thread(target=foo.third, args=(print_third,))
        t2 = threading.Thread(target=foo.second, args=(print_second,))
        t1 = threading.Thread(target=foo.first, args=(print_first,))
        
        t3.start()
        t2.start()
        t1.start()
        
        t1.join()
        t2.join()
        t3.join()
        
        self.assertEqual(result, ["first", "second", "third"])

    def test_multiple_executions(self):
        for _ in range(3):
            foo = Foo()  # Create new instance for each iteration
            result = []
            
            def print_first():
                result.append(1)
            
            def print_second():
                result.append(2)
                
            def print_third():
                result.append(3)
            
            threads = [
                threading.Thread(target=foo.third, args=(print_third,)),
                threading.Thread(target=foo.second, args=(print_second,)),
                threading.Thread(target=foo.first, args=(print_first,))
            ]
            
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            
            self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()