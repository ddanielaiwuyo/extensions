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

class StockRepository:
    def __init__(self, db_conn: psycopg.Connection) -> None:
        self.conn = db_conn

    def add_item(self, stock: StockItem) -> None:
        query = """
        INSERT INTO stock_items(name, price, quantity)
        VALUES (%s, %s, %s)
        """
        # the price is stored as a minor unit
        # to avoid rounding/floating errors
        # ie price = 20, saved as 2000, retreived as 20.00
        params = [stock.name, stock.price*100, stock.quantity]

        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            self.conn.commit()

        print(" item added to stock successfully")
        return

    def get_all(self) -> list[StockItem]:
        results = None
        with self.conn.cursor() as cursor:
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
