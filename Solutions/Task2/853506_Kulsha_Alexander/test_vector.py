import unittest
import vector

class TestVector(unittest.TestCase):
    def setup(self):
        self.v1 = Vector([2, 5, 3])
        self.v2 = Vector([1, 4, 2])
        self.v3 = Vector([3, 9, 8, 13])
        self.sub_v = Vector([1, 1, 1])
        self.add_v = Vector([3, 9, 5])
        self.mul_v = Vector([4, 10, 6])
        
    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, self.sub_v)
        
    def test_add(self):
        self.assertEqual(self.v1 + self.v2, self.add_v)
    
    @unittest.expectedFailure    
    def test_add_size_err(self):
        self.assertEqual(self.v1 + self.v3, self.add_v)
        
    def test_mul(self):
        self.assertEqual(self.v1 * 2, self.mul_v)
    
    def test_length(self):
        self.assertEqual(self.v1.size == 3)
        
    def test_get_item(self):
        self.assertEqual(self.v1[0], 2)
