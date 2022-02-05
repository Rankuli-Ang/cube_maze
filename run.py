""""""
import configparser
from resources.colors import Colors
from resources.steps import Steps
from src.visualizer import Visualizer
from src.cube import Cube
from src.player import Player
from src.processor import Processor

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
    start_room_coords = (0, 10, 2)

    player = Player(start_room_coords[0], start_room_coords[1], start_room_coords[2])
    cube.add_player(start_room_coords[0], start_room_coords[1], start_room_coords[2], player)
    players = [player]

    proc = Processor(cube, players)

    vis = Visualizer(CUBE_WIDTH, CUBE_HEIGHT, CUBE_ROW, Colors.FRAME_COLOR, Colors.PLAYER_COLOR, Colors.TRAP_COLOR,
                     Colors.NOT_EXAMINED_COLOR, Colors.EXAMINED_COLOR)
    vis.set_rooms()
    process = True
    while process:
        print('play cords in cube', player.get_coords())
        vis.visualize(CUBE_ROW, cube.get_level(0), 0, player)
        move = input('enter step')
        if move == '1':
            cube.move_player(player, Steps.UP)
            print(player.get_coords())
        elif move == '2':
            cube.move_player(player, Steps.LEFT)
            print(player.get_coords())
        elif move == '3':
            cube.move_player(player, Steps.RIGHT)
            print(player.get_coords())
        elif move == '4':
            cube.move_player(player, Steps.DOWN)
            print(player.get_coords())


