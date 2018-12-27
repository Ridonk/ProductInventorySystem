from product import Product
import json


class Inventory:
    def __init__(self, products: list):
        self.products = products
        print("Inventory initialized.")

    def add_existing_product(self, product: Product):
        print(product.get_product_details())
        self.products.append(product)

    def load_from_json(self, data_file: str):
        data = json.loads(data_file)
        print(data)
        # TODO: Setup JSON processing

    def save_to_json(self):
        print("Saving to JSON...")
        print(self.products)
        # TODO: Setup JSON saving
