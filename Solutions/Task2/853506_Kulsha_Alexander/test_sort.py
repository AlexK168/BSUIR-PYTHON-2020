from . import sort
import os
import unittest

class TestSorting(unittest.TestCase):
    def setup(self):
        output()
    def test_data_integrity(self):
        in_size = os.stat('data.txt').st_size
        out_size = os.stat('output.txt').st_size
        self.assertEqual(in_size, out_size)
    def test_sort(self):
        with open("output.txt", 'r') as f:
            left = int(f.readline())
            for right in f:
                self.assertTrue(left <= int(right))
                left = int(right)        
