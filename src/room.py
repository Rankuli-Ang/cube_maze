""""""
from src.door import Door
from src.player import Player


class Room:
    """"""

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._players = []
        self._doors = []
        self._neighbour_rooms = []
        self._trap = False
        # to add types of traps
        self._exit = False
        # resolve border rooms nuances

    def add_neighbour_rooms(self, neighbour_rooms: list) -> None:
        """"""
        self._neighbour_rooms = neighbour_rooms

    def add_player(self, player: Player) -> None:
        """Adds player to room's list."""
        self._players.append(player)

    def add_trap(self) -> None:
        """"""
        self._trap = True

    def get_x(self) -> int:
        """Returns 'x' coordinate of the room."""
        return self._x

    def get_y(self) -> int:
        """Returns 'y' coordinate of the room."""
        return self._y

    def set_doors(self) -> None:
        """"""
        for room in self._neighbour_rooms:
            new_door = Door(room.get_x(), room.get_y(), room.is_trap)
            self._doors.append(new_door)

    @property
    def is_trap(self) -> bool:
        """Returns True if room has a trap, else False."""
        return self._trap

    @property
    def is_exit(self) -> bool:
        """Returns True if room has an exit, else False."""
        return self._exit



