import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector([2, 5, 3])
        self.v2 = Vector([1, 4, 2])
        self.v3 = Vector([3, 9, 8, 13])
        self.v4 = Vector([1, 4, 3])
        self.sub_v = Vector([1, 1, 1])
        self.add_v = Vector([3, 9, 5])
        self.mul_v = Vector([4, 10, 6])
        self.empty_v = Vector([])
        self.v_str = Vector(['one', 'two', 'three'])

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, self.sub_v)

    @unittest.expectedFailure
    def test_sub_size_err(self):
        self.assertEqual(self.v1 - self.v3, self.sub_v)

    @unittest.expectedFailure
    def test_sub_type_err(self):
        self.assertEqual(self.v1 - "self.v3", self.sub_v)

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, self.add_v)

    @unittest.expectedFailure
    def test_add_size_err(self):
        self.assertEqual(self.v1 + self.v3, self.add_v)

    @unittest.expectedFailure
    def test_add_type_err(self):
        self.assertEqual(self.v1 + "self.v3", self.add_v)

    def test_mul(self):
        self.assertEqual(self.v1 * 2, self.mul_v)

    @unittest.expectedFailure
    def test_mul_type_err(self):
        self.assertEqual(self.v1 * 'err', self.mul_v)

    @unittest.expectedFailure
    def test_mul_size_err(self):
        self.assertEqual(self.v1 * self.v3, self.mul_v)

    def test_length(self):
        self.assertEqual(len(self.v1), 3)

    def test_get_item(self):
        self.assertEqual(self.v1[0], 2)

    def test_empty(self):
        self.assertTrue(self.empty_v.is_empty())

    def test_eq(self):
        self.assertEqual(self.v1, self.v1)

    @unittest.expectedFailure
    def test_eq_size_err(self):
        self.assertEqual(self.v1, self.v3)

    @unittest.expectedFailure
    def test_eq_type_err(self):
        self.assertEqual(self.v1, self.v_str)

    def test_assign_value(self):
        self.v2[2] = 3
        self.assertEqual(self.v2, self.v4)

    @unittest.expectedFailure
    def test_assign_type_err(self):
        self.v2[2] = '3'

    def test_inner_product(self):
        self.assertEqual(self.v2.inner_product(self.v4), 23)

    @unittest.expectedFailure
    def test_inner_type_err(self):
        self.assertEqual(self.v2.inner_product("self.v4"), 23)

    @unittest.expectedFailure
    def test_inner_size_err(self):
        self.assertEqual(self.v2.inner_product(self.v3), 23)

    def test_str(self):
        self.assertTrue(str(self.v3) == "[3, 9, 8, 13]")

    def test_size(self):
        self.assertEqual(self.v2.size, 3)

    def test_clear(self):
        self.v1.clear()
        self.assertEqual(self.v1, self.empty_v)

    @unittest.expectedFailure
    def test_init(self):
        self.assertEqual(Vector([1, 'fore', 2]), self.v2)

    @unittest.expectedFailure
    def test_init_none(self):
        self.assertEqual(Vector(None), self.empty_v)


if __name__ == '__main__':
    unittest.main()
