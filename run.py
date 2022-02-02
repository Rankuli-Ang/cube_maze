""""""
import configparser
from resources.colors import Colors
from src.visualizer import Visualizer
from src.cube import Cube

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('resources/config.ini')

    CUBE_HEIGHT = config.getint('VISUALIZER', 'height')
    CUBE_WIDTH = config.getint('VISUALIZER', 'width')
    CUBE_ROW = config.getint('CUBE', 'row')
    DIFFICULTY_LEVEL = config.getint('DIFFICULTY_LEVEL', 'medium')

    # vis = Visualizer(CUBE_WIDTH, CUBE_HEIGHT, CUBE_ROW,
    #                  Colors.FRAME_COLOR, Colors.CURRENT_COLOR,
    #                  Colors.TRAP_COLOR, Colors.EXAMINED_COLOR)
    # vis.set_rooms()
    # vis.visualize()

    cube = Cube(CUBE_ROW, DIFFICULTY_LEVEL)
    cube.set_rooms()
    print(len(cube._levels))
    print(len(cube._levels[3]))
    room = cube._levels[10][2][15]
    print(room._coordinate_x, room._coordinate_y)

