from time import time
from datetime import datetime
"""Import universal time stamp"""


class Order:
    """This class represents how order flows through the system"""
    def __init__(self, name: str):
        self.order_name = name
        self.order_income_time: float = time()
        self.order_outcome_time: float = -1
        self.order_receive_time: float = -1

    def __str__(self) -> str:
        temp_time = datetime.utcfromtimestamp(self.order_receive_time).strftime('%Y-%m-%d %H:%M:%S')
        return f'Order name: {self.order_name}, receive time: {temp_time}'
