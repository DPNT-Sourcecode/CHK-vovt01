import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):
    def test_single_sku(self):
        self.assertEqual(checkout_solution.hello('AABDD'), )


if __name__ == '__main__':
    unittest.main()
