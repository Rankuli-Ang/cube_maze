""""""
import random
from resources.steps import Steps


class Door:
    """"""

    def __init__(self, next_room_step: Steps.value, next_room_trap: bool):
        self._next_room_step = next_room_step

        if next_room_trap:  # temporary solution
            self._numbers = random.randint(100, 999), random.randint(100, 999), random.randint(100, 999)
        else:
            self._numbers = random.randint(100, 999), random.randint(100, 999), random.randint(100, 999)

    def get_next_room_step(self) -> Steps.value:
        """"""
        return self._next_room_step
