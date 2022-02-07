""""""
import random
from src.cube import Cube
from src.player import Player


class Processor:
    """"""

    def __init__(self, cube: Cube, players: list):
        self._cube = cube
        self._players = players

    def create_player(self) -> None:
        """"""
        level = random.choice(self._cube.get_levels())
        x = random.randrange(0, self._cube.get_row())
        y = random.randrange(0, self._cube.get_row())
        new_player = Player(level, x, y)
        self._players.append(new_player)

    def move_player(self, player: Player) -> None:
        """"""



