"""Tests the player module with unittest."""
import configparser
import unittest
from src.player import Player
from resources.steps import Steps, step_difference

config = configparser.ConfigParser()
config.read('test_config.ini')
PLAYER_LEVEL = config.getint('PLAYER_TEST', 'level')
PLAYER_X = config.getint('PLAYER_TEST', 'x')
PLAYER_Y = config.getint('PLAYER_TEST', 'y')
PLAYER_COORDS = PLAYER_LEVEL, PLAYER_X, PLAYER_Y

ROOM_LEVEL = config.getint('PLAYER_TEST', 'room_level')
ROOM_X = config.getint('PLAYER_TEST', 'room_x')
ROOM_Y = config.getint('PLAYER_TEST', 'room_y')
ROOM_COORDS = ROOM_LEVEL, ROOM_X, ROOM_Y
ROOM_IS_TRAP = config.getboolean('PLAYER_TEST', 'room_is_trap')

STEP = Steps.UP
EXPLORE_ROOM_COORDS = step_difference(PLAYER_COORDS, STEP)


class PlayerTest(unittest.TestCase):
    """Main test class.
    Tests funcs: add_examined_room_coords, explore_room, move."""

    def test_explore_room(self) -> None:
        """Tests adding room coords
        to the player's list of examined rooms coords
        and losing shoe."""
        player = Player(PLAYER_COORDS)
        must_remains_shoes = player.get_shoes() - 1

        player.explore_room(STEP, ROOM_IS_TRAP)

        self.assertIn(EXPLORE_ROOM_COORDS, player.get_examined_rooms())
        self.assertEqual(player.get_shoes(), must_remains_shoes)

    def test_move(self) -> None:
        """Tests changing player's coords to step value."""
        player = Player(PLAYER_COORDS)
        room_coords = step_difference(player.get_coords(), STEP)
        player.move(STEP)
        self.assertEqual(player.get_coords(), room_coords)


