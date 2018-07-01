import unittest

from solutions.HLO import hello_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(hello_solution.hello('xxx'), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
