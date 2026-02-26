from lib.stock_repository import StockItem, StockRepository
import lib.database_connection as database
from pytest import mark


@mark.it("Get's all the stock items provided in the seed")
def test_get_all_stock_items():
    conn = database.connect()
    database.seed(conn)

    stock_repo = StockRepository(conn)
    actual_result = stock_repo.get_all()
    expected_result = [
        StockItem("Airpods", 40000 / 100, 103, id=1),
        StockItem("Sony Headphones", 80099 / 100, 300, id=2),
        StockItem("Playstation 4", 49999 / 100, 5, id=3),
        StockItem("Yamaha Ninja", 39999 / 100, 30, id=4),
    ]

    assert actual_result == expected_result


@mark.it("Adds a stock item to the database and retrieves it")
def test_add_stock():
    conn = database.connect()
    database.seed(conn)

    stock_repo = StockRepository(conn)
    new_stock = StockItem("Maison Margiela", 30000, 40)
    stock_repo.add(new_stock)

    result = []
    with conn.cursor() as cursor:
        response = cursor.execute(
            "select * from stock_items where name = %s", ["Maison Margiela"]
        )
        result = response.fetchall()

    # new_stock.price = new_stock.price / 100
    row = result[0]
    actual_result = StockItem(row["name"], row["price"]/100, row["quantity"])
    assert actual_result == new_stock
