from oop.tests.exception_class import *


class Arena:
    def __init__(self):
        self.games = []
        self.standings = []

    def add_game(self, game):
        self.games.append(game)

    def scoring(self):
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
        self._name = name
        self.ranking = ranking

    def description(self):
        return f"My name is {self.name} and my ranking is {self.ranking}."

    @property
    def name(self):
        return self._name

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Player):
            return False
        return self.name == o.name

    def __hash__(self) -> int:
        result = 0
        for letter in self.name:
            result += ord(letter)
            result += 31
        return result
