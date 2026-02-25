from datetime import date
from typing import override

import psycopg

from lib.database_connection import connect_to_db

class OrderEntity:
    def __init__(self, customer_name, quantity, total_price, order_id=None, stock_item=None, stock_id=None, ):
        self.id = order_id
        self.customer_name = customer_name
        self.quantity = quantity
        self.total_price = total_price
        self.stock_id = stock_id
        self.stock_item = stock_item
        self.purchased_at = date.today()

    def cal_total_price(self, unit_price):
        self.total_price = self.quantity  * unit_price

    @override
    def __repr__(self) -> str:
        return f""" 
        Order Id: {self.id}
        Customer Name: {self.customer_name}
        Quantity: {self.quantity}
        Purchase date: {self.purchased_at}
        Total Price: £{self.total_price:.2f}
        Stock Id: {self.stock_id}
        """



def get_all_orders(conn: psycopg.Connection) -> list[None]:
    query = "SELECT * FROM orders"
    results = None
    with conn.cursor() as cursor:
        response = cursor.execute(query)
        results = response.fetchall()

    if results is None:
        print(" results returned for all orders is none")
        print(results)
        return []

    all_orders = []
    for row in results:
        entity = OrderEntity(
                row["customer_name"], row["quantity"],
                row["total_price"]/100
                )
        entity.stock_id = row["stock_id"]
        entity.id = row["id"]
        entity.purchased_at = row["purchased_at"]

        all_orders.append(entity)

    return all_orders


# if __name__ == "__main__":
#     conn = connect_to_db()
#     get_all_orders(conn)
