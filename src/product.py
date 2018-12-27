from money import Money
import math


class Product:
    def __init__(self, name: str, price: Money, cost: Money, on_hand: int, last_product_id=0):
        self.name = name
        self.price = price
        self.cost = cost
        self.on_hand = on_hand
        self.margin = self._set_margin()
        self.profit = self._set_profit()
        self.gross_profit = self._set_gross_profit()
        self.product_id = self._generate_id(last_product_id)
        print("Product initialized.")

    # Methods for init

    def _set_margin(self) -> float:
        return self._round_half_up(float(((self.price.amount - self.cost.amount) / self.price.amount) * 100))

    def _set_profit(self) -> Money:
        return Money(self.price.amount - self.cost.amount, "USD")

    def _set_gross_profit(self) -> Money:
        return Money((self.profit.amount * self.on_hand), "USD")

    @staticmethod
    def _generate_id(last_id: int) -> int:
        return last_id + 1

    # helper methods

    @staticmethod
    def _round_half_up(n: float, decimals=2):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier + 0.5) / multiplier

    def get_product_details(self) -> str:
        return "ID: {}\nName: {}\nPrice: {}\nCost: {}\nOn Hand: {}\nMargin: {}%\nProfit: {}\nGross Profit: {}".format(
            self.product_id,
            self.name,
            self.price,
            self.cost,
            self.on_hand,
            self.margin,
            self.profit,
            self.gross_profit
        )
