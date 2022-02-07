""""""
from src.player import Player


class Room:
    """"""

    def __init__(self, level: int, x: int, y: int):
        self._level: int = level
        self._x: int = x
        self._y: int = y
        self._players: list = []
        self._doors: list = []
        self._neighbour_rooms: list = []
        self._trap: bool = False
        # to add types of traps
        self._exit: bool = False
        # resolve border rooms nuances

    def add_neighbour_rooms(self, neighbour_rooms: list) -> None:
        """"""
        self._neighbour_rooms = neighbour_rooms

    def add_player(self, player: Player) -> None:
        """Adds player to room's list."""
        self._players.append(player)
        if not self._doors:  # need to add doors generating
            pass

    def del_player(self, player: Player) -> None:
        """Deletes player from the room's list."""
        self._players.remove(player)

    def add_trap(self) -> None:
        """"""
        self._trap = True

    def get_x(self) -> int:
        """Returns 'x' coordinate of the room."""
        return self._x

    def get_y(self) -> int:
        """Returns 'y' coordinate of the room."""
        return self._y

    def get_coords(self) -> tuple:
        """"""
        return self._level, self._x, self._y

    @property
    def is_trap(self) -> bool:
        """Returns True if room has a trap."""
        return self._trap

    def is_examined(self, player: Player) -> bool:
        """Returns True if room examined by player."""
        if self.get_coords() in player.get_examined_rooms():
            return True
        else:
            return False

    @property
    def is_exit(self) -> bool:
        """Returns True if room has an exit."""
        return self._exit

    @property
    def is_player_here(self) -> bool:
        """Returns True if player in this room."""
        if len(self._players) > 0:
            return True
        else:
            return False
