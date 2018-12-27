from product import Product


class Inventory:
    def __init__(self, products: list):
        self.products = products
        print("Inventory initialized.")

    def add_existing_product(self, product: Product):
        print(product.get_product_details())
        self.products.append(product)
