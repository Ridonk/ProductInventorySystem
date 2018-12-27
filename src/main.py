from product import Product
from inventory import Inventory
from money import Money

fake_product = Product("Monster 16oz", 1, Money(2.50, "USD"), Money(1.5, "USD"), 10)
print("ID: {}\nName: {}\nPrice: {}\nCost: {}\nOn Hand: {}\nMargin: {}%\nProfit: {}".format(
    fake_product.product_id,
    fake_product.name,
    fake_product.price,
    fake_product.cost,
    fake_product.on_hand,
    fake_product.margin,
    fake_product.gross_profit
))
fake_product_list = [fake_product]
fake_inventory = Inventory(fake_product_list)
