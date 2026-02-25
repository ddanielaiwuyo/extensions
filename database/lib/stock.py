from lib.stock_repository import StockItem

def create_new_stock_item() -> list[StockItem]:
    print(" CREATING NEW STOCK ITEM ")
    new_stocks = []
    while True:
        try:
            name = input(" name: ")
            price = float(input(" unit price: "))
            quantity = int(input(" stock quantity: "))

            if len(name.strip()) == 0:
                print(" please provide a valid name for stock")
                continue
            elif price <= 0.00:
                print(" unit price must not be 0 or less")
                continue
            elif quantity <= 0:
                print(" quantity must not be 0 or less")
                continue

            new_item = StockItem(name, price, quantity)
            new_stocks.append(new_item)

            choice = input(" add another item?[y/n]: ")

            if choice.lower().strip() in ["y", "yes"]:
                continue
            else:
                return new_stocks

        except ValueError:
            print(" please enter the appropriate values")

