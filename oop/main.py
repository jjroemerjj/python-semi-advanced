from oop.sports import *

if __name__ == '__main__':
    arena = Arena()
    player1 = Player("Jan Kowalski", 1200)
    player2 = Player("Jan Nowak", 1200)
    player3 = Player("Jan Lewandowski", 1200)
    game1 = Game(player1, player2, 1)
    game2 = Game(player1, player3, 2)
    game3 = Game(player2, player3, 2)

    arena.add_game(game1)
    arena.add_game(game2)
    arena.add_game(game3)

    arena.scoring()
