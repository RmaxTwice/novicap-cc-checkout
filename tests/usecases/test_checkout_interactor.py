import unittest

from src.usecases.checkout import CheckoutInteractor


class TestCheckoutInteractor(unittest.TestCase):

    def setUp(self):
        self.price_rules = "{}"
        self.checkout = CheckoutInteractor(self.price_rules)

    def test_simple_case(self):
        self.checkout.scan("VOUCHER")
        self.assertEqual(self.checkout.total, "5.00€")
