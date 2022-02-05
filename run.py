""""""
import configparser
from resources.colors import Colors
from src.visualizer import Visualizer
from src.cube import Cube
from src.player import Player

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('resources/config.ini')

    CUBE_HEIGHT = config.getint('VISUALIZER', 'height')
    CUBE_WIDTH = config.getint('VISUALIZER', 'width')
    CUBE_ROW = config.getint('CUBE', 'row')
    CUBE_SQUARE = CUBE_ROW * CUBE_ROW
    DIFFICULTY_LEVEL = config.getint('DIFFICULTY_LEVEL', 'medium')

    cube = Cube(CUBE_ROW, DIFFICULTY_LEVEL)
    cube.create_rooms()
    cube.create_traps_on_level(CUBE_SQUARE, DIFFICULTY_LEVEL, cube.get_level(0), 0)

    player = Player()
    vis = Visualizer(CUBE_WIDTH, CUBE_HEIGHT, CUBE_ROW,
                     Colors.FRAME_COLOR, Colors.CURRENT_COLOR,
                     Colors.TRAP_COLOR, Colors.NOT_EXAMINED_COLOR, Colors.EXAMINED_COLOR)
    vis.set_rooms()
    vis.visualize(CUBE_ROW, cube.get_level(0))


