from time import time


class CashDesk:
    def __init__(self, manager):
        self.manager = manager

    def new_order(self, order):
        message = f'Order received: {order.order_name}'
        self.log(message)
        print(message)
        order.order_income_time: float = time()
        self.manager.new_order(order)

    @staticmethod
    def log(message):
        with open('CashDesk.log', 'a', encoding='utf-8') as f:
            f.write(message + '\n')
