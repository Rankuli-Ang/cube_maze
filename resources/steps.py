"""contains Step class with associated methods."""
from enum import Enum


class Steps(Enum):
    """Enum Class of the all possible steps of the player.
    Step is change in player coords in 1 turn."""
    UPPER = (-1, 0, 0)
    UNDER = (1, 0, 0)
    UP = (0, 0, -1)
    DOWN = (0, 0, 1)
    LEFT = (0, -1, 0)
    RIGHT = (0, 1, 0)


def step_difference(coords: tuple, step: Steps) -> tuple:
    """Returns coords with a Step change."""
    return (coords[0] + step.value[0],
            coords[1] + step.value[1],
            coords[2] + step.value[2])


STEPS = [Steps.UPPER, Steps.UNDER,
         Steps.UP, Steps.DOWN,
         Steps.LEFT, Steps.RIGHT]


STEPS_VALUES = [Steps.UPPER.value, Steps.UNDER.value,
                Steps.UP.value, Steps.DOWN.value,
                Steps.LEFT.value, Steps.RIGHT.value]




