"""Tests the cube module with the unittest."""
import configparser
import random
import unittest
from src.cube import Cube

config = configparser.ConfigParser()
config.read('test_config.ini')
ROW = config.getint('CUBE_TEST', 'row')
DIFFICULTY_COEFFICIENT = config.getint('CUBE_TEST', 'difficult_coefficient')
RANDOM_INDEX = random.randrange(0, ROW)


class CubeTest(unittest.TestCase):
    """Main test class."""

    def test_create_rooms(self) -> None:
        """Tests"""
        cube = Cube(ROW, DIFFICULTY_COEFFICIENT)
        cube.create_rooms()
        self.assertEqual(cube.get_levels(), ROW)
        self.assertEqual(cube.get_level(RANDOM_INDEX), ROW)
        self.assertEqual(cube.get_level(RANDOM_INDEX)[RANDOM_INDEX], ROW)
