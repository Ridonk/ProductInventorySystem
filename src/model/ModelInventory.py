from model.ModelProduct import Product
from money import Money
import json


class Inventory:
    def __init__(self, products: list):
        self.products = products
        print("Inventory initialized.")

    def add_new_product(self, product: Product):
        self.products.append(product)

    def load_from_json(self, data_file_path: str):
        with open(data_file_path, "r") as f:
            data = json.load(f)
        for item in data["item"]:
            self.products.append(
                Product(
                    item["name"],
                    Money(item["price"], "USD"),
                    Money(item["cost"], "USD"),
                    item["on_hand"]))

    def save_to_json(self):
        print("Saving to JSON...")
        print(self.products)
        # TODO: Setup JSON saving

    def gross_inventory_profit(self):
        total_profit = Money(0, "USD")
        for product in self.products:
            total_profit += product.gross_profit
        return total_profit
