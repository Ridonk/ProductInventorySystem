from money import Money


class Product:
    def __init__(self, name: str, product_id: int, price: Money, cost: Money, on_hand: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.cost = cost
        self.on_hand = on_hand
        self.margin = self._get_margin()
        self.profit = self._get_profit()
        self.gross_profit = self._get_gross_profit()
        print("Product initialized.")

    def _get_margin(self) -> float:
        return ((self.price.amount - self.cost.amount) / self.price.amount) * 100

    def _get_profit(self) -> Money:
        return Money(self.price.amount - self.cost.amount, "USD")

    def _get_gross_profit(self) -> Money:
        return Money((self.profit.amount * self.on_hand), "USD")
