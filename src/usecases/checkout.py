import json

from moneyed.l10n import format_money

from src.entities.checkout import Checkout, Product


class CheckoutInteractor:

    def __init__(self, price_rules_json: str):
        # Normally this would be done by an external layer
        price_rules = json.loads(price_rules_json)
        products = [Product(**p) for p in price_rules]
        self.checkout = Checkout(products)

    def scan(self, product_code: str) -> None:
        self.checkout.add_scanned_item(product_code)

    @property
    def total(self) -> str:
        total = self.checkout.calculate_total()
        return format_money(total, "0.00¤", locale="en_US")
