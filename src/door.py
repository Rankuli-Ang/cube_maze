""""""
import random


class Door:
    """"""

    def __init__(self, next_room_x: int, next_room_y: int, room_trap: bool):
        self._next_room_coordinates = next_room_x, next_room_y

        if room_trap:  # temporary solution
            self._numbers = random.randint(100, 999), random.randint(100, 999), random.randint(100, 999)
        else:
            self._numbers = random.randint(100, 999), random.randint(100, 999), random.randint(100, 999)

    def get_next_room_coordinates(self) -> tuple:
        """"""
        return self._next_room_coordinates
