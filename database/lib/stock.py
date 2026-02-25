import psycopg
from typing import override

class StockItem:
    def __init__(self, name, price, quantity, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @override
    def __repr__(self) -> str:
        return f"""
    Id: {self.id}
    Stock Name: {self.name}  
    Price: £{self.price}
    Quantity: {self.quantity}
    """

def get_stock_items(conn: psycopg.Connection) -> list[StockItem]:
    results = None
    with conn.cursor() as cursor:
        response = cursor.execute("select * from stock_items", )
        results = response.fetchall()


    stocks = []
    for row in results:
        stock = StockItem(
            row["name"], row["price"] / 100, 
            row["quantity"], row["id"]
                )
        stocks.append(stock)


    return stocks

def list_stock_items(conn: psycopg.Connection):
    print(" showing all stock items")
    stocks = get_stock_items(conn)
    for item in stocks:
        print(item)

