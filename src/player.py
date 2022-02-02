""""""


class Player:
    """"""

    def __init__(self, coordinate_x: int, coordinate_y: int):
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y
        self._shoes = 2
        self._examined_rooms = []

    def move(self) -> None:
        """"""

    def add_examined_room(self, room_coordinate_x: int, room_coordinate_y: int) -> None:
        """"""
        examined_room = room_coordinate_x, room_coordinate_y
        if examined_room in self._examined_rooms:
            return
        else:
            self._examined_rooms.append(examined_room)

    def get_examined_rooms(self) -> list:
        """"""
        return self._examined_rooms
