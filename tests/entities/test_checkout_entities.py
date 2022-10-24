import unittest

from moneyed import Money

from src.entities.checkout import Product, Checkout
from tests.fixtures import products_fixture


class TestProduct(unittest.TestCase):
    def setUp(self):
        products = products_fixture()
        product = products[0]
        self.product = Product(**product)

    def test_basic_constructor(self):
        self.assertEqual(str(self.product.code), "VOUCHER")
        self.assertEqual(self.product.name, "Voucher")
        self.assertEqual(self.product.unit_price, {
            "amount": "5.00", "currency_code": "EUR"
        })

    def test_get_unit_price(self):
        unit_price = self.product.get_unit_price()
        self.assertIsInstance(unit_price, Money)
        self.assertEqual(unit_price.get_amount_in_sub_unit(), 500)
        self.assertEqual(unit_price.currency.code, "EUR")


class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.products = [Product(**p) for p in products_fixture()]
        # self.discounts = price_rules["discounts"]
        self.checkout = Checkout(products=self.products)

    def test_empty_checkout_total(self):
        checkout = Checkout(products=[])
        empty_total = checkout.calculate_total()

        self.assertIsInstance(empty_total, Money)
        self.assertEqual(empty_total.get_amount_in_sub_unit(), 0)
        self.assertEqual(empty_total.currency.code, "EUR")

    def test_calculate_total_without_discounts(self):
        checkout = Checkout(products=self.products)
        checkout.add_scanned_item("VOUCHER")
        checkout.add_scanned_item("TSHIRT")
        checkout.add_scanned_item("MUG")
        total = checkout.calculate_total()

        self.assertIsInstance(total, Money)
        self.assertEqual(total.get_amount_in_sub_unit(), 3250)
        self.assertEqual(total.currency.code, "EUR")
