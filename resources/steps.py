from enum import Enum


class Steps(Enum):
    UP_LEVEL = (-1, 0, 0)
    DOWN_LEVEL = (1, 0, 0)
    UP = (0, 0, -1)
    DOWN = (0, 0, 1)
    LEFT = (0, -1, 0)
    RIGHT = (0, 1, 0)
