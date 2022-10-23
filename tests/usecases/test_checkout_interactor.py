import json
import unittest

from src.usecases.checkout import CheckoutInteractor


class TestCheckoutInteractor(unittest.TestCase):

    def setUp(self):
        # Basic products and discounts test fixture
        price_rules = [
                {
                    "code": "VOUCHER",
                    "name": "Voucher",
                    "price": {
                        "amount": "5.00",
                        "currency_code": "EUR"
                    }
                },
                {
                    "code": "TSHIRT",
                    "name": "T-shirt",
                    "price": {
                        "amount": "20.00",
                        "currency_code": "EUR"
                    }
                },
                {
                    "code": "MUG",
                    "name": "Coffee mug",
                    "price": {
                        "amount": "7.50",
                        "currency_code": "EUR"
                    }
                }
        ]
        price_rules_json = json.dumps(price_rules)
        self.checkout = CheckoutInteractor(price_rules_json)

    def test_raise_error_product_code_not_found(self):
        with self.assertRaises(ValueError):
            self.checkout.scan("FOO")

    def test_empty_checkout(self):
        self.assertEqual(self.checkout.total, "0.00€")

    def test_simple_checkout(self):
        self.checkout.scan("VOUCHER")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("MUG")
        self.assertEqual(self.checkout.total, "32.50€")

