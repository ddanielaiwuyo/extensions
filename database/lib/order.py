from datetime import date
from typing import override

class Order:
    def __init__(self, customer_name, quantity, stock_item=None, stock_id=None):
        self.id = id  # TODO: come back to this
        self.customer_name = customer_name
        self.quantity = quantity
        self.total_price = self._calc_total_price()
        self.purchased_at = date.today()
        self.stock_id = stock_id
        self.stock_item = stock_item

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
