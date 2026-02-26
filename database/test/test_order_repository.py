from datetime import date
from lib.order_repository import *
import lib.database_connection as database
from pytest import mark

# PRICES are stored as minor-cents, 
# ie price = 123.92. stored_as: int = 12392, retrived_as: int = 12392
# and in application code: price = 123.92
# This is to avoid floating errors and parsing magic
@mark.it("All orders from the seed database return expected result")
def test_get_all_orders():
    conn = database.connect()
    database.seed(conn)
    order_1 = OrderEntity("Bill Evans", 1, 139.99)
    order_1.id = 1
    order_1.stock_id = 3
    order_1.purchased_at = date.fromisoformat("2021-11-12")

    order_2 = OrderEntity("Jonathan Blow", 3, 420.00)
    order_2.id = 2
    order_2.stock_id = 1
    order_2.purchased_at = date.fromisoformat("2026-04-25")


    expected_result = [ order_1, order_2 ]

    order_repo = OrderRepository(conn)
    actual_result = order_repo.get_all()
    assert actual_result == expected_result

@mark.it("Order is added to the database and yields the same value")
def test_add_order():
    conn = database.connect()
    database.seed(conn, "seeds/extension_db.sql")

    order = OrderEntity("Fyodor Doestoeyesky", 1, 13999)
    order.purchased_at = date.today()

    order_repo = OrderRepository(conn)
    order_repo.add(order)

    query = "SELECT * FROM orders where customer_name = 'Fyodor Doestoeyesky'"
    result = []
    with conn.cursor() as cursor:
        response = cursor.execute(query)
        result = response.fetchall()

    row = result[0]
    actual_result = OrderEntity(row["customer_name"], row["quantity_purchased"], row["total_price"])
    actual_result.purchased_at = row["purchased_at"]


    assert actual_result == order


