"""Tests the room module with unittest."""
import unittest
import configparser
from src.room import Room
from resources.steps import Steps


config = configparser.ConfigParser()
config.read('test_config.ini')
LEVEL = config.getint('ROOM_TEST', 'level')
X = config.getint('ROOM_TEST', 'x')
Y = config.getint('ROOM_TEST', 'y')

neighbours_rooms_is_traps = {Steps.UP: True, Steps.DOWN: False, Steps.LEFT: True, Steps.RIGHT: False}


class RoomTest(unittest.TestCase):
    """The Main test class. Tests func: create_doors."""

    # def test_create_doors(self) -> None:
    #     """"""
    #     room = Room((LEVEL, X, Y))
    #     room.create_doors(neighbours_rooms_is_traps,
    #                       PRIME_NUMBERS, NON_PRIME_NUMBERS)
    #
    #     doors = room.get_doors()
    #     doors.