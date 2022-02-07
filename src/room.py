""""""
from src.door import Door
from src.player import Player


class Room:
    """"""

    def __init__(self, coordinate_x: int, coordinate_y: int):
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y
        self._players = []
        self._doors = []
        self._adjoining_rooms = []
        self._trap = None
        # to add types of traps
        self._exit = None
        # resolve border rooms nuances

    def add_adjoining_rooms(self, adjoining_rooms: list) -> None:
        """"""
        self._adjoining_rooms = adjoining_rooms

    def add_player(self, player: Player) -> None:
        """Adds player to room's list."""
        self._players.append(player)

    def get_coordinate_x(self) -> int:
        """Returns 'x' coordinate of the room."""
        return self._coordinate_x

    def get_coordinate_y(self) -> int:
        """Returns 'y' coordinate of the room."""
        return self._coordinate_y

    def set_doors(self) -> None:
        """"""
        for room in self._adjoining_rooms:
            new_door = Door(room.get_coordinate_x(), room.get_coordinate_y(), room.is_trap)
            self._doors.append(new_door)

    @property
    def is_trap(self) -> bool:
        """Returns True if room has a trap, else False."""
        if self._trap is None:
            return False
        else:
            return True

    @property
    def is_exit(self) -> bool:
        """Returns True if room has an exit, else False."""
        if self._exit is None:
            return False
        else:
            return True
