
from restaurant.cash_desk import CashDesk
from restaurant.give_away import GiveAway
from restaurant.kitchen import Kitchen
from restaurant.manager import Manager
from restaurant.order import Order


if __name__ == '__main__':

    """--------------POCZATEK SETUPU--------------"""

    """Inicjalizacja obiektów z pustymi 'polami' managerów"""
    cash_desk = CashDesk(None)
    kitchen = Kitchen(None)
    give_away = GiveAway(None)

    """Stworzenie obiektu managera"""
    manager = Manager(cash_desk, kitchen, give_away)

    """Przypisanie managera do wcześniej stworzonych obiektów (w miejsce pustych pól wchodzi manager)"""
    cash_desk.manager = manager
    kitchen.manager = manager
    give_away.manager = manager

    """--------------KONIEC SETUPU--------------"""

    """Inicjalizujemy pierwsze zamówienie, program defacto 'rusza' od tego miejsca"""
    cash_desk.new_order(Order('Burger'))
    cash_desk.new_order(Order('Pizza'))
    print("\nProgram is done")



