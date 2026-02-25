import psycopg
from lib.order import OrderEntity, get_all_orders
from lib.utils import Utils
from lib.database_connection import connect_to_db
from lib.stock import StockItem, list_stock_items
import traceback

def main_menu() -> int:
    welcome_msg = """
    Welcome to the shop management system

    What would you want to do?
        1. List all shop items
        2. Create a new item
        3. List all orders
        4. Create a new order
        5. Quit
    """

    print(welcome_msg)
    max_choice = 4
    while True:
        try:
            choice = int(input(" enter: "))
            choice = choice - 1

            if choice < 0 or choice > max_choice:
                print(" please provide choice between 1 and 4")
                continue

            return choice
        except ValueError:
            print(" please provide a valid number")

LIST_ITEMS = 0
CREATE_NEW_ITEM = 1
LIST_ALL_ORDERS = 2
CREATE_NEW_ORDER = 3
QUIT = 4

def list_all_items() -> None:
    mock_items = ["chess game", "new patched updates"]
    print(" displaying items")
    for i, item in enumerate(mock_items, start=1):
        print( f" {i}. {item}")
    pass

def create_new_item() -> None:
    pass

def list_all_orders() -> None:
    mock_orders = ["chess game", "new patched updates"]
    print(" displaying items")
    for i, item in enumerate(mock_orders, start=1):
        print( f" {i}. {item}")


def create_new_order(stock: list[StockItem]) -> OrderEntity:
    # 1. show all items in stock
    # 2. get quantity
    # 3. confirm and create order
    max_choice = len(stock) - 1
    user_choice = Utils.get_choice(max_choice)

    selected_item = stock[user_choice]
    qty = Utils.get_quantity(selected_item.quantity)

    print(" please provide the following for your reciept")
    username = input(" name: ")
    new_order = OrderEntity(username,selected_item, qty)
    return new_order
    


# working order
# [x]. list_stock_items() from db 
# [2]. list_all_orders() from db
# [3]. create_new_order()
def matcher(user_choice: int, db_conn: psycopg.Connection) -> None:
    stock = [
        StockItem("Airpods", 139.21, 50), 
        StockItem("Headphones", 500.00, 500), 
        StockItem("Mercedes Pen", 399.99, 121), 
    ]

    if user_choice == LIST_ITEMS:
        list_stock_items(db_conn) 
    elif user_choice == CREATE_NEW_ITEM:
        print(" still under construction...")
    elif user_choice == LIST_ALL_ORDERS:
        all_orders = get_all_orders(db_conn)
        print(" ====  all orders from db ====")
        for order in all_orders:
            print(order)
    elif user_choice == CREATE_NEW_ORDER:
        new_order = create_new_order(stock)
        print("\n new order came in:", new_order)
    else:
        print(" Quitting application")
        return


def main():
    conn = connect_to_db()
    while True:
        try:
            user_choice = main_menu()
            matcher(user_choice, conn)

            new_op = input(" start again?[y/n]: ")
            if new_op.lower() in ["n", "no"]:
                print(" see you another time")
                break
        except KeyboardInterrupt:
            print(" closing application\n")
            return
        except Exception:
            print(" unexpected error!")
            traceback.print_exc()
            return

if __name__ == "__main__":
    main()
