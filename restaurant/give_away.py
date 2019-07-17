from time import time, sleep


class GiveAway:

    def __init__(self, manager):
        self.manager = manager

    def call_customer(self, order):
        message: str = 'Calling customer'
        self.log(message)
        print(message)
        sleep(1)
        self.customer_collected_order(order)

    def customer_collected_order(self, order):
        message: str = f'Order {order.order_name} received by customer'
        self.log(message)
        print(message)
        order.order_receive_time = time()
        self.manager.customer_collected_order(order)

    @staticmethod
    def log(message):
        with open('GiveAway.log', 'a', encoding='utf-8') as f:
            f.write(message + '\n')
