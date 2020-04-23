from json import dumps
import unittest
import human
import JSON

class TestJson(unittest.TestCase):
    def setup(self):
        self.conv = JSON()
        
    def test_numbers(self):
        a = 4
        b = 2.020
        self.assertEqual(self.conv.dumps(a), dumps(a))
        self.assertEqual(self.conv.dumps(b), dumps(b))
        
    def test_string(self):
        string = "this test is not gonna fail"
        self.assertEqual(self.conv.dumps(string), dumps(string))
    
    def test_boolean(self):
        true_var = True
        false_var = False
        self.assertEqual(self.conv.dumps(true_var), dumps(true_var))
        self.assertEqual(self.conv.dumps(false_var), dumps(false_var))

    def test_none(self):
        nonesence = None
        self.assertEqual(self.conv.dumps(nonesence), dumps(nonesence))
    
    def test_tuple(self):
        test_tuple = ("maya", "hee", 'maya', 'haa', 4, 1, False, [3, 11, 0])
        self.assertEqual(self.conv.dumps(test_tuple), dumps(test_tuple))
                         
    def test_dict(self):
        test_dict = {3: "three", 2: 'one', "hotel?": 'trivago'}
        self.assertEqual(self.conv.dumps(test_dict), dumps(test_dict))
                         
    def test_custom(self):
        human = Human('Vincent Vega', 35, 'M')   
        self.assertEqual(self.conv.dumps(human), dumps(human))
