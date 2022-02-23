"""Tests the cube module with the unittest."""
import configparser
import random
import unittest
from src.cube import Cube
from src.player import Player
from resources.steps import Steps, step_difference

config = configparser.ConfigParser()
config.read('test_config.ini')
ROW = config.getint('TEST_CUBE', 'row')
DIFFICULTY_COEFFICIENT = config.getfloat('TEST_CUBE', 'difficult_coefficient')
RANDOM_INDEX = random.randrange(0, ROW)

ROOM_COORDS = 0, 0, 0
EXPECTED_NUMBER_OF_NEIGHBOURS = 3

STEP_UPPER = Steps.UPPER
PLAYER_START_COORDS = (5, 5, 5)


class CubeTest(unittest.TestCase):
    """Main test class."""

    def test_create_rooms(self) -> None:
        """Tests creating rooms in the all cube levels."""
        cube = Cube(ROW, DIFFICULTY_COEFFICIENT)
        cube.create_rooms()
        self.assertEqual(len(cube.get_levels()), ROW)
        self.assertEqual(len(cube.get_level(RANDOM_INDEX)), ROW)
        self.assertEqual(len(cube.get_level(RANDOM_INDEX)[RANDOM_INDEX]), ROW)

    def test_create_traps_around_loc(self) -> None:
        """Tests creating traps in the start loc,
        upper level and below level."""
        cube = Cube(ROW, DIFFICULTY_COEFFICIENT)
        cube.create_rooms()
        cube.create_traps_around_loc(RANDOM_INDEX)
        levels = [cube.get_level(RANDOM_INDEX),
                  cube.get_level(RANDOM_INDEX - 1),
                  cube.get_level(RANDOM_INDEX + 1)]
        levels_traps = []
        for level in levels:
            level_trap = None
            for room in level[RANDOM_INDEX]:
                if room.is_trap:
                    level_trap = True
            levels_traps.append(level_trap)

        for trap in levels_traps:
            self.assertTrue(trap)

    def test_create_exit(self) -> None:
        """Tests creation of the exit room."""
        cube = Cube(ROW, DIFFICULTY_COEFFICIENT)
        cube.create_rooms()
        cube.create_exit()
        self.assertTrue(cube.get_room(cube.get_exit_coords()).is_exit)

    def test_get_neighbour_rooms(self) -> None:
        """Tests correctness of the returning neighbour rooms."""
        cube = Cube(ROW, DIFFICULTY_COEFFICIENT)
        cube.create_rooms()
        neighbours = cube.get_neighbour_rooms(ROOM_COORDS)
        self.assertEqual(len(neighbours), EXPECTED_NUMBER_OF_NEIGHBOURS)

    def test_move_player(self) -> None:
        """Tests player replacement
        and creation traps in the upper level. """
        cube = Cube(ROW, DIFFICULTY_COEFFICIENT)
        cube.create_rooms()
        player = Player(PLAYER_START_COORDS)
        cube.add_player(player)
        new_coords = step_difference(player.get_coords(), STEP_UPPER)
        cube.move_player(player, STEP_UPPER)
        trap_presence = False
        for row in cube.get_level(player.get_coords()[0] - 1):
            for room in row:
                if room.is_trap:
                    trap_presence = True

        self.assertTrue(cube.get_room(new_coords).is_player_here)
        self.assertFalse(cube.get_room(PLAYER_START_COORDS).is_player_here)
        self.assertTrue(trap_presence)






