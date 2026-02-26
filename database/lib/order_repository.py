import psycopg
from datetime import date
from typing import override
from lib.stock_repository import StockItem


# OrderEntity represents how an Order
# is represented in the database.
# No value should be added into the `stock_item` argument
# when sending to the database as this is only provided
# when doing joins on the the `stock_item` and `orders` table
class OrderEntity:
    def __init__(
        self,
        customer_name,
        quantity,
        total_price,
        order_id=None,
        stock_item=None,
        stock_id=None,
    ):
        self.id = order_id
        self.customer_name = customer_name
        self.quantity = quantity
        self.total_price = total_price
        self.stock_id = stock_id
        self.stock_item = stock_item
        self.purchased_at = date.today()

    @override
    def __eq__(self, other) -> bool:
        if not isinstance(other, OrderEntity):
            return False
        return (
            self.id == other.id
            and self.customer_name == other.customer_name
            and self.quantity == other.quantity
            and self.total_price == other.total_price
            and self.purchased_at == other.purchased_at
        )

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
    def __init__(self, db_conn: psycopg.Connection) -> None:
        self.conn = db_conn

    def add(self, order: OrderEntity) -> None:
        query = """
        INSERT INTO orders (customer_name, quantity_purchased, total_price, purchased_at, stock_id)
        VALUES ( %s, %s, %s, %s, %s);
        """

        try:
            params = [
                order.customer_name,
                order.quantity,
                order.total_price * 100,
                order.purchased_at,
                order.stock_id,
            ]
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                self.conn.commit()
        except psycopg.Error as err:
            print(" UNEXPECTED ERROR OCCURED\n")
            raise psycopg.Error(err)

    def get_all(self) -> list[OrderEntity]:
        # query = "SELECT * FROM orders"
        new_query = """
        SELECT * FROM orders
        INNER JOIN stock_items
        on stock_items.id = orders.stock_id
        """
        # results = None
        results = None
        try:
            with self.conn.cursor() as cursor:

                response = cursor.execute(new_query)
                results = response.fetchall()

            all_entries = []
            for row in results:
                entity = OrderEntity(
                    row["customer_name"],
                    row["quantity_purchased"],
                    row["total_price"] / 100,
                )
                stock = StockItem(row["name"], row["price"] / 100, None)
                entity.stock_item = stock

                all_entries.append(entity)

            return all_entries
        except Exception as err:
            print(" unexpected error occured!")
            raise (err)
