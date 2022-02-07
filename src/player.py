""""""
from resources.steps import Steps


class Player:
    """"""

    def __init__(self, level: int, x: int, y: int):
        self._level = level
        self._x = x
        self._y = y
        self._shoes = 2
        self._examined_rooms = []
        self._alive = True

    def get_coords(self) -> tuple:
        """"""
        return self._level, self._x, self._y

    @property
    def is_alive(self) -> bool:
        """If Player is alive returns True, else returns False."""
        return self._alive

    def add_examined_room(self, level: int, room_x: int, room_y: int) -> None:
        """"""
        examined_room = level, room_x, room_y
        if examined_room in self._examined_rooms:
            return
        else:
            self._examined_rooms.append(examined_room)

    def move(self, step: Steps) -> None:  # maybe return bool with alive status
        """"""
        # if next_room_trap:
        #     self._alive = False
        #     return
        self._level += step.value[0]
        self._x += step.value[1]
        self._y += step.value[2]
        self.add_examined_room(self._level, self._x, self._y)

    def get_examined_rooms(self) -> list:
        """"""
        return self._examined_rooms


