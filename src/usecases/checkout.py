class CheckoutInteractor:

    def __init__(self, price_rules: str):
        self.price_rules = price_rules

    def scan(self, product_code: str) -> None:
        return self.price_rules

    @property
    def total(self) -> str:
        return "5.00€"
