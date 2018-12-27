from product import Product
from inventory import Inventory
from money import Money

fake_inventory = Inventory([])
fake_inventory.add_existing_product(
    Product("Monster Original 16oz",
            Money(2.50, "USD"),
            Money(1.29, "USD"),
            10))
