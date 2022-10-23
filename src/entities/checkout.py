from dataclasses import dataclass
from typing import Union

@dataclass
class Product:
    """Class for keeping track of a Product"""
    code: str = None
    name: str = None
    price_models: str = None
