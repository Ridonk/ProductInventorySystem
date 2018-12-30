def display_inventory(inventory: list):
    for item in inventory:
        print("ID: {}\n"
              "Name: {}\n"
              "Price: {}\n"
              "Cost: {}\n"
              "On Hand: {}\n"
              "Margin: {}%\n"
              "Profit: {}\n"
              "Gross Profit: {}"
              "".format(
                    item.product_id,
                    item.name,
                    item.price,
                    item.cost,
                    item.on_hand,
                    item.margin,
                    item.profit,
                    item.gross_profit
                ))


def inventory_menu_1():
    print("Welcome to Open Inventory. Version is DEV.")
    print("Would you like to view the current inventory? (y/n)")


def inventory_menu_error():
    print("Invalid input, please try again. ")
