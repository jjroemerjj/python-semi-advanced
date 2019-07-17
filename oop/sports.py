from oop.tests.exception_class import *


class Arena:
    def __init__(self):
        self.games = []
        self.standing = []

    def add_game(self, game):
        self.games.append(game)

    """
    1. stwórz listę zawodników
    2. Stwórz mapę zawodnik -> liczba zwycięstw albo drugą listę
    3. Posortuj liczbę zawodników względem ich liczby zwycięstw
    """
    def standing(self):
        players = []
        scores = []

        for game in self.games:
            white = game.white
            black = game.black
            if white not in players:
                players.append(white)
                scores.append(0)
            if black not in players:
                players.append(black)
                scores.append(0)

            if game.white_won():
                index = players.index(white)
            else:
                index = players.index(black)
            scores[index] += 1

        player_score_list = list(zip(players, scores))
        player_score_list.sort(reverse=True, key=lambda x: x[1])

        return [pair[0] for pair in player_score_list]


class Game:
    def __init__(self, white, black, result):
        self.white = white
        self.black = black
        self.result = result

    def white_won(self):
        return self.result == 1

    def black_won(self):
        return self.result == 2


class Player:
    def __init__(self, name, ranking):
        if len(name) < 3:
            raise NameToShortException()
        self.name = name
        self.ranking = ranking

    def description(self):
        return f"My name is {self.name} and my ranking is {self.ranking}."


