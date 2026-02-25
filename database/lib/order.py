from datetime import date
from typing import override

class Order:
    def __init__(self, customer_name, stock_item, quantity, stock_id=None):
        # self.id =  # TODO: come back to this
        self.customer_name = customer_name
        self.stock_item = stock_item
        self.quantity = quantity
        self.total_price = self._calc_total_price()
        self.purchased_at = date.today()
        if stock_id is None:
            stock_id = 0
        self.stock_id = stock_id

    def _calc_total_price(self) -> int:
        return self.quantity * self.stock_item.price
    

    @override
    def __repr__(self) -> str:
        return f"""
    Name: {self.customer_name}  
    Item: {self.stock_item.name}  @ £{self.stock_item.price}
    Quantity: {self.quantity}
    Total Price: {self.total_price}
    Ordered On: {self.purchased_at}
    """



# class StockItem:
#     def __init__(self, name, price, quantity):
#         self.id = 0
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     @override
#     def __repr__(self) -> str:
#         return f"""
#     Stock Name: {self.name}  
#     Price: {self.price}  @ £{self.price}
#     Quantity: {self.quantity}
#     """
#
