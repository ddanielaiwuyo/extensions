import psycopg

import lib.database_connection as database
from lib.stock_repository import StockRepository
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


LIST_ITEMS_CHOICE = 0
CREATE_NEW_ITEM_CHOICE = 1
LIST_ALL_ORDERS_CHOICE = 2
CREATE_NEW_ORDER_CHOICE = 3
QUIT_CHOICE = 4


def matcher(user_choice: int, db_conn: psycopg.Connection) -> None:
    stock_repo = StockRepository(db_conn)
    order_repo = OrderRepository(db_conn)

    if user_choice == LIST_ITEMS_CHOICE:
        current_stocks = stock_repo.get_all()
        print(f"  {'ID':<2}  {'ITEM':<25} {'PRICE':<10} {'xQUANTITY':>5}")
        for idx, stock in enumerate(current_stocks, start=1):
            print(
                f"  {idx:<2} {stock.name:<25} £ {stock.price:<10} {stock.quantity:>5}"
            )

    elif user_choice == CREATE_NEW_ITEM_CHOICE:
        new_stocks = create_new_stock_item()
        for stock_item in new_stocks:
            stock_repo.add_item(stock_item)

        print("  ===== STOCKS UPDATED ===== ")
    elif user_choice == LIST_ALL_ORDERS_CHOICE:
        all_orders = order_repo.get_all()
        for idx, entry in enumerate(all_orders, start=1):
            stock = entry.stock_item
            print(
            f"""
            .{idx}
            NAME: {entry.customer_name} BOUGHT {stock.name}
            PAID: £{entry.total_price}, AMT:{entry.quantity} 
            UNIT_PRICE: £{stock.price} """
            )

    elif user_choice == CREATE_NEW_ORDER_CHOICE:
        current_stocks = stock_repo.get_all()
        new_orders = get_new_orders(current_stocks)
        for new_order in new_orders:
            order_repo.add(new_order)

        print(f"  Total of {len(new_orders)} made")
    else:
        print("  Quitting application")
        return


def main() -> None:
    conn = database.connect()
    database.seed(conn)
    while True:
        try:
            user_choice = main_menu()
            matcher(user_choice, conn)

            print()
            new_op = input("  Go back to main menu or quit?[m/q]: ")
            if new_op.lower() in ["q", "no"]:
                print("  See you another time")
                break
        except KeyboardInterrupt:
            print("  Closing application\n")
            return
        except Exception:
            print("  Unexpected error!")
            traceback.print_exc()
            return

    conn.close()

if __name__ == "__main__":
    main()
