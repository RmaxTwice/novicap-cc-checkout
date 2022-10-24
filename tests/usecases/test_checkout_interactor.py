import json
import unittest

from src.usecases.checkout import CheckoutInteractor
from tests.fixtures import price_rules_json_fixture


class TestCheckoutInteractor(unittest.TestCase):

    def setUp(self):
        # Basic products and discounts test fixture
        price_rules = price_rules_json_fixture()
        self.checkout = CheckoutInteractor(price_rules)

    def test_product_code_not_found_error(self):
        with self.assertRaises(ValueError):
            self.checkout.scan("FOO")

    def test_no_items_scanned_total(self):
        self.assertEqual(self.checkout.total, "0.00€")

    def test_total_without_discounts(self):
        self.checkout.scan("VOUCHER")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("MUG")
        self.assertEqual(self.checkout.total, "32.50€")

    def test_calculate_total_with_package_discount(self):
        self.checkout.scan("VOUCHER")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("VOUCHER")
        self.assertEqual(self.checkout.total, "25.00€")

    def test_calculate_total_with_bulk_discount(self):
        self.checkout.scan("TSHIRT")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("VOUCHER")
        self.checkout.scan("TSHIRT")
        self.assertEqual(self.checkout.total, "81.00€")

    def test_calculate_total_with_all_discounts(self):
        self.checkout.scan("VOUCHER")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("VOUCHER")
        self.checkout.scan("VOUCHER")
        self.checkout.scan("MUG")
        self.checkout.scan("TSHIRT")
        self.checkout.scan("TSHIRT")
        self.assertEqual(self.checkout.total, "74.50€")
