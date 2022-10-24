import unittest

from moneyed import Money

from src.entities.checkout import Product, Checkout
from tests.fixtures import products_fixture, discounts_fixture


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
        self.discounts = discounts_fixture()
        self.checkout = Checkout(products=self.products, product_discounts=self.discounts)

    def add_scanned_products(self, products):
        for p in products:
            self.checkout.add_scanned_product(p)

    def test_empty_checkout_total(self):
        checkout = Checkout(products=[])
        empty_total = checkout.calculate_total()

        self.assertIsInstance(empty_total, Money)
        self.assertEqual(empty_total.get_amount_in_sub_unit(), 0)
        self.assertEqual(empty_total.currency.code, "EUR")

    def test_calculate_total_without_discounts(self):
        checkout = Checkout(products=self.products)
        checkout.add_scanned_product("VOUCHER")
        checkout.add_scanned_product("TSHIRT")
        checkout.add_scanned_product("MUG")
        total = checkout.calculate_total()

        self.assertIsInstance(total, Money)
        self.assertEqual(total.get_amount_in_sub_unit(), 3250)
        self.assertEqual(total.currency.code, "EUR")

    def test_calculate_total_with_package_discount(self):
        products = ["VOUCHER", "TSHIRT", "VOUCHER"]
        self.add_scanned_products(products)
        total = self.checkout.calculate_total()

        self.assertIsInstance(total, Money)
        self.assertEqual(total.get_amount_in_sub_unit(), 2500)
        self.assertEqual(total.currency.code, "EUR")

    def test_calculate_total_with_bulk_discount(self):
        products = ["TSHIRT", "TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"]
        self.add_scanned_products(products)
        total = self.checkout.calculate_total()

        self.assertIsInstance(total, Money)
        self.assertEqual(total.get_amount_in_sub_unit(), 8100)
        self.assertEqual(total.currency.code, "EUR")

    def test_calculate_total_with_all_discounts(self):
        products = ["VOUCHER", "TSHIRT", "VOUCHER", "VOUCHER", "MUG", "TSHIRT", "TSHIRT"]
        self.add_scanned_products(products)
        total = self.checkout.calculate_total()

        self.assertIsInstance(total, Money)
        self.assertEqual(total.get_amount_in_sub_unit(), 7450)
        self.assertEqual(total.currency.code, "EUR")
