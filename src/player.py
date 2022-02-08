""""""
from resources.steps import Steps


class Player:
    """Main game character class."""

    def __init__(self, level: int, x: int, y: int):
        self._level: int = level
        self._x: int = x
        self._y: int = y
        self._shoes: int = 2
        self._examined_rooms: list = [(self._level, self._x, self._y)]
        self._alive: bool = True

    def get_coords(self) -> tuple:
        """Returns player's coordinates."""
        return self._level, self._x, self._y

    def get_shoes(self) -> int:
        """Gets number of shoes a player has."""
        return self._shoes

    @property
    def is_alive(self) -> bool:
        """If Player is alive returns True."""
        return self._alive

    def add_examined_room(self, room_coords: tuple) -> None:
        """Adds room's coordinates
        to the list of examined rooms."""
        examined_room = room_coords[0], room_coords[1], room_coords[2]
        if examined_room in self._examined_rooms:
            return
        else:
            self._examined_rooms.append(examined_room)

    def throw_a_shoe(self) -> None:
        """Reduces player's shoes by 1."""
        self._shoes -= 1

    def move(self, step: Steps) -> None:
        """Changes the player's coordinates to the step value."""
        self._level += step.value[0]
        self._x += step.value[1]
        self._y += step.value[2]
        self.add_examined_room(self.get_coords())

    def get_examined_rooms(self) -> list:
        """"""
        return self._examined_rooms




