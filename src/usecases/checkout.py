import json

from moneyed import Money
from moneyed.l10n import format_money

from src.entities.checkout import Checkout, Product


class CheckoutInteractor:

    def __init__(self, price_rules_json: str):
        price_rules = json.loads(price_rules_json)
        products = price_rules["products"] or []
        discounts = price_rules["discounts"] or []
        products = [Product(**p) for p in price_rules["products"]]
        self.checkout = Checkout(products, discounts)

    def scan(self, product_code: str) -> None:
        self.checkout.add_scanned_item(product_code)

    @property
    def total(self) -> str:
        total = self.checkout.calculate_total()
        return format_money(total, "0.00¤", locale="en_US")
