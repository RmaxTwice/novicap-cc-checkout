from dataclasses import dataclass, field
from collections import Counter
from typing import Dict, List, Union, Any

from moneyed import Money


@dataclass
class Product:
    """Class for keeping track of a Product"""
    code: str
    name: str
    unit_price: Dict[str, Dict]

    def get_unit_price(self) -> Money:
        return Money(self.unit_price["amount"], self.unit_price["currency_code"])


@dataclass
class Checkout:
    products: Union[Dict[str, Product], List[Product]]
    scanned_products: List = field(default_factory=list)
    discounts: Dict[str, Dict] = field(default_factory=dict)
    default_currency: str = "EUR"

    def __post_init__(self):
        product_list = dict()
        for product in self.products:
            product_list[product.code] = product
        self.products = product_list

    def add_scanned_product(self, product_code: str) -> None:
        if product_code in self.products.keys():
            self.scanned_products.append(product_code)
        else:
            raise ValueError("Product code not found!")

    def calculate_total(self) -> Money:
        sub_total = Money("0.00", self.default_currency)
        items_qty = Counter(self.scanned_products)

        for product_code, qty  in items_qty.items():
            sub_total += self.calculate_item_subtotal(product_code, qty)
            self.products[product_code].get_unit_price()

        total = sub_total
        return total

    def calculate_item_subtotal(self, product_code: str, qty: int) -> Money:
        sub_total = Money("0.00", self.default_currency)
        discount = self.get_applicable_product_discount(product_code)
        remaining_qty = qty

        if discount:
            if discount["type"] == "bulk":
                pass
            elif discount["type"] == "package":
                package_price = Money(
                    discount["price"]["amount"],
                    discount["price"]["currency_code"]
                )
                package_qty = remaining_qty // discount["qty"]
                sub_total += package_price * package_qty
                remaining_qty = remaining_qty % discount["qty"]

        if remaining_qty > 0:
            # Remaining subtotal without discounts
            unit_price = self.products[product_code].get_unit_price()
            sub_total += unit_price * remaining_qty

        return sub_total

    def get_applicable_product_discount(self, product_code: str) -> Union[Any, Dict]:
        discount = self.discounts.get(product_code, None)
        if discount:
            return discount["available_discounts"].get(discount["active"], None)
        return None
