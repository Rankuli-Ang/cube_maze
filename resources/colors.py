from enum import Enum


class Colors(Enum):
    FRAME_COLOR = (32, 165, 218)
    PLAYER_COLOR = (140, 230, 240)
    TRAP_COLOR = (0, 0, 255)
    EXIT_COLOR = (255, 255, 255)
    EXAMINED_COLOR = (230, 216, 173)
    NOT_EXAMINED_COLOR = (115, 115, 115)
