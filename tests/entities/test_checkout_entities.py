import unittest

from moneyed import Money

from src.entities.checkout import Product


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
