from dataclasses import dataclass
from typing import Dict

from moneyed import Money


@dataclass
class Product:
    """Class for keeping track of a Product"""
    code: str
    name: str
    price: Dict[str, str]

    @property
    def unit_price(self) -> Money:
        return Money(self.price["amount"], self.price["currency_code"])
