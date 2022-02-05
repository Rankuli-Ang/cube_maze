""""""


class Player:
    """"""

    def __init__(self, level: int, coordinate_x: int, coordinate_y: int):
        self._level = level
        self._x = coordinate_x
        self._y = coordinate_y
        self._shoes = 2
        self._examined_rooms = []
        self._alive = True

    @property
    def is_alive(self) -> bool:
        """If Player is alive returns True, else returns False."""
        return self._alive

    def add_examined_room(self, room_x: int, room_y: int) -> None:
        """"""
        examined_room = room_x, room_y
        if examined_room in self._examined_rooms:
            return
        else:
            self._examined_rooms.append(examined_room)

    def move(self, next_room_trap: bool,
             next_room_x: int, next_room_y: int) -> None:  # maybe return bool with alive status
        """"""
        if next_room_trap:
            self._alive = False
            return
        self._x = next_room_x
        self._y = next_room_y
        self.add_examined_room(next_room_x, next_room_y)

    def get_examined_rooms(self) -> list:
        """"""
        return self._examined_rooms
