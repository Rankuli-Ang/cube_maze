"""Tests visualizer module with the unittest."""
import configparser
import random
import unittest
from src.visualizer import Visualizer

config = configparser.ConfigParser()
config.read('test_config.ini')
CUBE_ROW = config.getint('VISUALIZER_TEST', 'row')
ROOM_SIDE_PXLS = config.getint('VISUALIZER_TEST', 'room_side_pxls')
RANDOM_INDEX = random.randrange(0, CUBE_ROW)


class VisualizerTest(unittest.TestCase):
    """The main test class."""

    def test_set_rooms(self) -> None:
        """Test correctness of the setting rooms."""
        vis = Visualizer(CUBE_ROW)
        vis.set_visualization(ROOM_SIDE_PXLS)
        vis.set_rooms()
        self.assertEqual(len(vis._rooms_coordinates), CUBE_ROW)
        self.assertEqual(len(vis._rooms_coordinates[RANDOM_INDEX]), CUBE_ROW)



