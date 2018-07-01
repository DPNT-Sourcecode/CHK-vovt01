import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):
    def test_single_sku(self):
        self.assertEqual(checkout_solution.checkout('AABDD'), 160)

    def test_single_offer(self):
        self.assertEqual(checkout_solution.checkout('AAAD'), 145)

    def test_multiple_offer(self):
        self.assertEqual(checkout_solution.checkout('AAABB'), 175)

    def test_multiple_offer_with_extra(self):
        self.assertEqual(checkout_solution.checkout('AAAABBB'), 255)

    def test_bad_input(self):
        self.assertEqual(checkout_solution.checkout('AAABBZZ'), 175)


if __name__ == '__main__':
    unittest.main()
