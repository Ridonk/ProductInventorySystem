from product import Product
from inventory import Inventory
from money import Money

fake_inventory = Inventory([])
print(fake_inventory.products)
fake_inventory.add_existing_product(Product("Monster 16oz", Money(2.50, "USD"), Money(1.29, "USD"), 10))
print(fake_inventory.products[0])
print("ID: {}\nName: {}\nPrice: {}\nCost: {}\nOn Hand: {}\nMargin: {}%\nProfit: {}\nGross Profit: {}".format(
    fake_inventory.products[0].product_id,
    fake_inventory.products[0].name,
    fake_inventory.products[0].price,
    fake_inventory.products[0].cost,
    fake_inventory.products[0].on_hand,
    fake_inventory.products[0].margin,
    fake_inventory.products[0].profit,
    fake_inventory.products[0].gross_profit
))