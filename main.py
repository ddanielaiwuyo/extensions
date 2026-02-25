from lib.order import StockItem

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
        choice = int(input(" enter: "))
        choice = choice - 1

        if choice < 0 or choice > max_choice:
            print(" please provide choice between 1 and 4")
            continue

        return choice

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

def create_new_order(stock: list[StockItem]) -> None:
    # 1. show all items in stock
    # 2. get quantity
    # 3. confirm and create order
    pass


def matcher(user_choice: int) -> None:
    if user_choice == LIST_ITEMS:
        list_all_items()
    elif user_choice == CREATE_NEW_ITEM:
        create_new_item()
    elif user_choice == LIST_ALL_ORDERS:
        list_all_orders()
    elif user_choice == CREATE_NEW_ORDER:
        create_new_order()
    else:
        print(" Quitting application")
        return
        # raise Exception("Got unidentified user_choice: ", user_choice)


def main():
    while True:
        user_choice = main_menu()
        matcher(user_choice)

        new_op = input(" start again?[y/n]: ")
        if new_op.lower() in ["n", "no"]:
            print(" see you another time")
            break

if __name__ == "__main__":
    main()
