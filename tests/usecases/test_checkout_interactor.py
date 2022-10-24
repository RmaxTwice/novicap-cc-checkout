import json
import unittest

from src.usecases.checkout import CheckoutInteractor
from tests.fixtures import price_rules_fixture

class TestCheckoutInteractor(unittest.TestCase):

    def setUp(self):
        # Basic products and discounts test fixture
        price_rules = price_rules_fixture()
        price_rules_json = json.dumps(price_rules)
        self.checkout = CheckoutInteractor(price_rules_json)

    def test_product_code_not_found_error(self):
        with self.assertRaises(ValueError):
            self.checkout.scan("FOO")

    def test_no_items_scanned_total(self):
        self.assertEqual(self.checkout.total, "0.00€")

    def test_simple_checkout(self):
        self.checkout.scan("VOUCHER")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("MUG")
        self.assertEqual(self.checkout.total, "32.50€")
