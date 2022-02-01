""""""
import configparser
from resources.colors import Colors
from src.visualizer import Visualizer

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('resources/config.ini')

    CUBE_HEIGHT = config.getint('CUBE', 'height')
    CUBE_WIDTH = config.getint('CUBE', 'width')
    CUBE_ROW = config.getint('CUBE', 'row')
    FRAME_COLOR = Colors.FRAME_COLOR
    TRAP_COLOR = Colors.TRAP_COLOR

    vis = Visualizer(CUBE_WIDTH, CUBE_HEIGHT, CUBE_ROW, FRAME_COLOR, TRAP_COLOR)
    vis.set_rooms()
    vis.visualize()

