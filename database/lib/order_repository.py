import psycopg
import traceback
from datetime import date
from typing import override

class OrderEntity:
    def __init__(self, customer_name, quantity, total_price, order_id=None, stock_item=None, stock_id=None):
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

class OrderRepository:
    def __init__(self, db_conn: psycopg.Connection):
        self.conn = db_conn

    def add(self, order: OrderEntity) -> None:
        query = """
        INSERT INTO orders (customer_name, quantity, total_price, purchased_at, stock_id)
        VALUES ( %s, %s, %s, %s, %s);
        """

        try:
            params = [order.customer_name, order.quantity, order.total_price, order.purchased_at, order.stock_id]
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                self.conn.commit()
        except psycopg.Error as err :
            print(" UNEXPECTED ERROR OCCURED\n")
            raise psycopg.Error(err)
            # traceback.print_exc


        

    def get_all(self) -> list[OrderEntity]:
        query = "SELECT * FROM orders"
        results = None
        with self.conn.cursor() as cursor:
            response = cursor.execute(query)
            results = response.fetchall()

        if results is None:
            print(" results returned for all orders is none")
            return results

        all_orders = []
        for row in results:
            entity = OrderEntity( row["customer_name"], row["quantity"], row["total_price"]/100) # type: ignore
            entity.stock_id = row["stock_id"] # type: ignore
            entity.id = row["id"] # type: ignore
            entity.purchased_at = row["purchased_at"] # type: ignore

            all_orders.append(entity)

        return all_orders

