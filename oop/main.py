from oop.sports import *


if __name__ == '__main__':

    player1 = Player('Jakub', 1200)
    player2 = Player('Emilia', 1200)
    print(player1 == player2)

    print(player1.__hash__())
    print(player2.__hash__())



