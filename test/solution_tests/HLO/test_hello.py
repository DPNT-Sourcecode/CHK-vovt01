import unittest

from solutions.HLO import hello_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(hello.compute(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
