from dataclasses import dataclass, field
from typing import Dict, List, Union

from moneyed import Money


@dataclass
class Product:
    """Class for keeping track of a Product"""
    code: str
    name: str
    price_models: Dict[str, Dict]

    def get_unit_price(self) -> Money:
        unit_price = self.price_models["unit_price"]
        return Money(unit_price["amount"], unit_price["currency_code"])


@dataclass
class Checkout:
    products: Union[Dict[str, Product], List[Product]]
    scanned_items: List = field(default_factory=list)
    default_currency: str = "EUR"

    def __post_init__(self):
        product_list = dict()
        for product in self.products:
            product_list[product.code] = product
        self.products = product_list

    def add_scanned_item(self, product_code: str) -> None:
        if product_code in self.products.keys():
            self.scanned_items.append(product_code)
        else:
            raise ValueError("Product code not found!")

    def calculate_total(self) -> Money:
        total = Money("0.00", self.default_currency)
        for item in self.scanned_items:
            total += self.products[item].get_unit_price()

        return total
