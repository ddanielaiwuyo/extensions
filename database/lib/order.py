from typing import override
from datetime import date
from lib.utils import Utils
import psycopg
from lib.order_repository import OrderEntity, OrderRepository
from lib.stock_repository import StockItem


def get_new_orders(stocks: list[StockItem]) -> list[OrderEntity]:
    all_orders = []
    while True:
        try:
            for idx, stock in enumerate(stocks, start=1):
                print(f"  {idx}.  {stock.name} £{stock.price} {stock.quantity}")

            max_choice = len(stocks)
            user_choice = Utils.get_choice(max_choice)

            selected_stock_item = stocks[user_choice]
            qty = Utils.get_quantity(selected_stock_item.quantity)

            print("\n  Please provide the following for your reciept")
            total_price = qty * selected_stock_item.price
            customer_name = input(" name: ")
            print()

            new_order = OrderEntity(customer_name, qty, total_price)
            new_order.stock_id = selected_stock_item.id
            new_order.stock_item = selected_stock_item

            all_orders.append(new_order)
            choice = input(" Make a new order?[y/n]: ")
            if choice.lower().strip() in ["n", "no"]:
                return all_orders

        except Exception as err:
            raise (err)
