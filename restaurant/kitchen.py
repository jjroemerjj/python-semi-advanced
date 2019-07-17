from time import time, sleep


class Kitchen:
    def __init__(self, manager):
        self.manager = manager

    def prepare_meal(self, order):
        message = f'{order.order_name}: preparing in kitchen'
        self.log(message)
        print(message)
        sleep(1)
        self.meal_ready(order)

    def meal_ready(self, order):
        message = f'Order {order.order_name} ready for delivery'
        self.log(message)
        print(message)
        order.order_outcome_time: float = time()
        self.manager.meal_ready(order)

    @staticmethod
    def log(message):
        with open('Kitchen.log', 'a', encoding='utf-8') as f:
            f.write(message + '\n')
