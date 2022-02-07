""""""
from src.room import Room


class Player:
    """"""

    def __init__(self, level: int, coordinate_x: int, coordinate_y: int):
        self._level = level
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y
        self._shoes = 2
        self._examined_rooms = []
        self._alive = True

    @property
    def is_alive(self) -> bool:
        """If Player is alive returns True, else returns False."""
        if self._alive is True:
            return True
        else:
            return False

    def add_examined_room(self, room_coordinate_x: int, room_coordinate_y: int) -> None:
        """"""
        examined_room = room_coordinate_x, room_coordinate_y
        if examined_room in self._examined_rooms:
            return
        else:
            self._examined_rooms.append(examined_room)

    def move(self, next_room: Room) -> None:  # maybe return bool with alive status
        """"""
        if next_room.is_trap is True:
            self._alive = False
            return
        self._coordinate_x = next_room.get_coordinate_x()
        self._coordinate_y = next_room.get_coordinate_y()
        self.add_examined_room(next_room.get_coordinate_x(), next_room.get_coordinate_y())

    def get_examined_rooms(self) -> list:
        """"""
        return self._examined_rooms
