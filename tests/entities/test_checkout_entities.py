import unittest

from src.entities.checkout import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        product = {
            "code": "VOUCHER",
            "name": "Voucher",
            "price_models": "5.00 EUR"
        }
        self.product = Product(**product)

    def test_product_properties(self):
        self.assertEqual(str(self.product.code), "VOUCHER")
        self.assertEqual(self.product.name, "Voucher")
        self.assertEqual(self.product.price_models, "5.00 EUR")
