""""""
from enum import Enum


class Steps(Enum):
    """"""
    UP_LEVEL = (-1, 0, 0)
    DOWN_LEVEL = (1, 0, 0)
    UP = (0, 0, -1)
    DOWN = (0, 0, 1)
    LEFT = (0, -1, 0)
    RIGHT = (0, 1, 0)


STEPS_VALUES = [Steps.UP_LEVEL.value, Steps.DOWN_LEVEL.value,
                Steps.UP.value, Steps.DOWN.value,
                Steps.LEFT.value, Steps.RIGHT.value]

