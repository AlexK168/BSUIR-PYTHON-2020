import cached.py
from timeit import default_timer as timer
import unittest

class TestDecorator(unittest.TestCase):
    def setup(self):
        @cached
        def arithmetics(a, b):
            return a**2 + b**2 - 2 *a * b
        
    def test_cached(self):
        start = timer()
        self.arithmetics(123456, 123456)
        time1 = timer() - start
        start = timer()
        self.arithmetics(123456, 123456)
        time2 = timer() - start
        self.assertTrue(time_1 > time_2)

