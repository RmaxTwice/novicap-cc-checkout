import unittest

from moneyed import Money

from src.entities.checkout import Product, Checkout
from tests.fixtures import price_rules_fixture


class TestProduct(unittest.TestCase):
    def setUp(self):
        product = {
            "code": "VOUCHER",
            "name": "Voucher",
            "price": {
                "amount": "5.00",
                "currency_code": "EUR"
            }
        }
        self.product = Product(**product)

    def test_product_properties(self):
        self.assertEqual(str(self.product.code), "VOUCHER")
        self.assertEqual(self.product.name, "Voucher")
        self.assertEqual(
            self.product.price, {"amount": "5.00","currency_code": "EUR"}
        )
        unit_price = self.product.unit_price
        self.assertIsInstance(unit_price, Money)
        self.assertEqual(unit_price.get_amount_in_sub_unit(), 500)
        self.assertEqual(unit_price.currency.code, "EUR")


class TestCheckout(unittest.TestCase):
    def setUp(self):
        price_rules = price_rules_fixture()
        self.products = [Product(**p) for p in price_rules["products"]]
        self.discounts = price_rules["discounts"]
        self.checkout = Checkout(products=self.products, discounts=self.products)

    def test_empty_checkout(self):
        checkout = Checkout(products=[], discounts=[])
        empty_total = checkout.calculate_total()

        self.assertIsInstance(empty_total, Money)
        self.assertEqual(empty_total.get_amount_in_sub_unit(), 0)
        self.assertEqual(empty_total.currency.code, "EUR")

    def test_checkout_without_discounts(self):
        checkout = Checkout(products=self.products, discounts=[])
        checkout.add_scanned_item("VOUCHER")
        checkout.add_scanned_item("TSHIRT")
        checkout.add_scanned_item("MUG")
        total = checkout.calculate_total()
        self.assertIsInstance(total, Money)
        self.assertEqual(total.get_amount_in_sub_unit(), 3250)
        self.assertEqual(total.currency.code, "EUR")
