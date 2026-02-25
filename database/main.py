import psycopg

from lib.database_connection import connect_to_db
from lib.stock_repository import StockItem, StockRepository
from lib.stock import create_new_stock_item
from lib.order import get_new_orders
from lib.order_repository import OrderRepository
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
        print(f" {i}. {item}")
    pass


def list_all_orders() -> None:
    mock_orders = ["chess game", "new patched updates"]
    print(" displaying items")
    for i, item in enumerate(mock_orders, start=1):
        print(f" {i}. {item}")


# def create_new_order(stock: list[StockItem]) -> OrderEntity:
#     # 1. show all items in stock
#     # 2. get quantity
#     # 3. confirm and create order
#     max_choice = len(stock)
#     user_choice = Utils.get_choice(max_choice)
#
#     selected_stock_item = stock[user_choice]
#     qty = Utils.get_quantity(selected_stock_item.quantity)
#
#     print(" please provide the following for your reciept")
#     username = input(" name: ")
#     new_order = OrderEntity(username, selected_stock_item, qty)
#     new_order.stock_id = selected_stock_item.id
#     return new_order


# working order
# [x]. list_stock_items() from db
# [x]. list_all_orders() from db
# [x]. create_new_item() with db
# [5]. date_of_an_order() from db
# [6]. create_new_order()
def matcher(user_choice: int, db_conn: psycopg.Connection) -> None:
    stock_repo = StockRepository(db_conn)
    # stock = [
    #     StockItem("Airpods", 139.21, 50),
    #     StockItem("Headphones", 500.00, 500),
    #     StockItem("Mercedes Pen", 399.99, 121),
    # ]
    order_repo = OrderRepository(db_conn)

    current_stocks = stock_repo.get_all()

    if user_choice == LIST_ITEMS:
        all_stocks = stock_repo.get_all()
        for stock in enumerate(stocks, start=0):
            print(f" {stock.name} {stock.price} {stock.quantity}")

    elif user_choice == CREATE_NEW_ITEM:
        new_stocks = create_new_stock_item()
        for stock_item in new_stocks:
            stock_repo.add_item(stock_item)

        print(" STOCKS UPDATED ")
    elif user_choice == LIST_ALL_ORDERS:
        all_orders = get_all_orders(db_conn)
        print(" ====  all orders from db ====")
        for order in all_orders:
            print(order)

    elif user_choice == CREATE_NEW_ORDER:
        new_orders = get_new_orders(current_stocks)
        for new_order in new_orders:
            order_repo.add(new_order)

        print(f" total of {len(new_orders)} made")
        # print("\n", new_order)

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
