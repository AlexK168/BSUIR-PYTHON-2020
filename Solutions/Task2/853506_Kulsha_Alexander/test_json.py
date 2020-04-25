import unittest
from human import Human
from to_json import ToJSON


class TestJson(unittest.TestCase):
    def setUp(self):
        self.conv = ToJSON()

    def test_numbers(self):
        a = 4
        b = 2.23
        self.assertEqual(self.conv.dumps(a), """4""")
        self.assertEqual(self.conv.dumps(b), """2.23""")

    def test_string(self):
        string = "this test is not gonna fail"
        self.assertEqual(self.conv.dumps(string), "\"this test is not gonna fail\"")

    def test_boolean(self):
        true_var = True
        false_var = False
        self.assertEqual(self.conv.dumps(true_var), 'true')
        self.assertEqual(self.conv.dumps(false_var), 'false')

    def test_none(self):
        nonesence = None
        self.assertEqual(self.conv.dumps(nonesence), 'null')

    def test_tuple(self):
        test_tuple = ("maya", "hee", 4, 1, False, [3, 11, 0])
        self.assertEqual(self.conv.dumps(test_tuple), "[\"maya\", \"hee\", 4, 1, false, [3, 11, 0]]")

    def test_dict(self):
        test_dict = {3: "three", 1: 'one', "hotel?": 'trivago'}
        self.assertEqual(self.conv.dumps(test_dict), "{3: \"three\", 1: \"one\", \"hotel?\": \"trivago\"}")

    def test_custom(self):
        human = Human('Vincent Vega', 35, 'M')
        self.assertEqual(self.conv.dumps(human), "{\"name\": \"Vincent Vega\", \"age\": 35, \"sex\": \"M\"}")


if __name__ == '__main__':
    unittest.main()
