from cached import cached
from timeit import default_timer as timer
import unittest


class TestDecorator(unittest.TestCase):

    def test_cached(self):
        start = timer()
        self.arithmetics(123456, 123456)
        time1 = timer() - start
        start = timer()
        self.arithmetics(123456, 123456)
        time2 = timer() - start
        self.assertTrue(time1 > time2)

    @cached
    def arithmetics(self, a, b):
        return a ** 2 + b ** 2 - 2 * a * b


if __name__ == '__main__':
    unittest.main()