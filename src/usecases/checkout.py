import json

from moneyed import Money
from moneyed.l10n import format_money

class CheckoutInteractor:

    def __init__(self, price_rules: str):
        self.products = {}
        self.items = []
        self.load_price_rules(price_rules)

    def load_price_rules(self, price_rules_json: str) -> None:
        price_rules = json.loads(price_rules_json)
        for product in price_rules:
            amount, currency = product["price"].split(" ")
            self.products[product["code"]] = {
                "name": product["name"],
                "price": Money(amount, currency),
            }

    def scan(self, product_code: str) -> None:
        if product_code in self.products.keys():
            self.items.append(product_code)
        else:
            raise ValueError("Product code not found!")

    @property
    def total(self) -> str:
        result = Money("0.00", "EUR")
        for item in self.items:
            result += self.products[item]["price"]

        formatted_result = format_money(result, "0.00¤", locale="en_US")
        return formatted_result
