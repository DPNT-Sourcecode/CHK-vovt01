import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):
    def test_single_sku(self):
        self.assertEqual(checkout_solution.checkout('AABDD'), 160)

    def test_single_offer(self):
        self.assertEqual(checkout_solution.checkout('AAAD'), 145)

    def test_multiple_offer(self):
        self.assertEqual(checkout_solution.checkout('AAABB'), 145)


if __name__ == '__main__':
    unittest.main()
