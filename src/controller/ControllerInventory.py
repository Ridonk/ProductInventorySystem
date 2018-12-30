from model.ModelInventory import Inventory
from view import ViewInventory


def view_inventory(master_inventory):
    ViewInventory.inventory_menu_1()
    user_input = input(">>> ")
    if user_input == "y":
        ViewInventory.display_inventory(master_inventory.products)
        view_inventory(master_inventory)
    elif user_input == "n":
        quit(0)
    else:
        ViewInventory.inventory_menu_error()
        view_inventory(master_inventory)


def start():
    master_inventory = Inventory([])
    master_inventory.load_from_json("../configs/product_list.json")
    view_inventory(master_inventory)


if __name__ == "__main__":
    start()
