from money import Money


class Product:
    def __init__(self, name: str, price: Money, cost: Money, on_hand: int, last_product_id=0):
        self.name = name
        self.price = price
        self.cost = cost
        self.on_hand = on_hand
        self.margin = self._get_margin()
        self.profit = self._get_profit()
        self.gross_profit = self._get_gross_profit()
        self.product_id = self._generate_id(last_product_id)
        print("Product initialized.")

    @staticmethod
    def _generate_id(last_id: int) -> int:
        return last_id + 1

    def _get_margin(self) -> float:
        return round(((self.price.amount - self.cost.amount) / self.price.amount) * 100)

    def _get_profit(self) -> Money:
        return Money(self.price.amount - self.cost.amount, "USD")

    def _get_gross_profit(self) -> Money:
        return Money((self.profit.amount * self.on_hand), "USD")
