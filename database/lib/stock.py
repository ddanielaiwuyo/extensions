import psycopg
from psycopg.rows import dict_row
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


def connect_to_db() -> psycopg.Connection:
    seed_path = "seeds/extension_db.sql"
    content = ""
    with open(seed_path, "r") as f:
        content = f.read()
    
    connstr = "postgresql://localhost/extension_db"
    conn = psycopg.connect(connstr, row_factory=dict_row)

    with conn.cursor() as cursor:
        cursor.execute(content)
        conn.commit()

    return conn

def get_stock_items() -> list[StockItem]:
    conn = connect_to_db()
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


    for item in stocks:
        print(item)
    return stocks

def list_stock_items():
    _ = get_stock_items()

if __name__ == "__main__":
    list_stock_items()
