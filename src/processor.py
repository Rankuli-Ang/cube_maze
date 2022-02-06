""""""
from src.cube import Cube
from src.player import Player
from src.visualizer import Visualizer
from resources.colors import Colors
from resources.steps import Steps


class Processor:
    """"""

    def __init__(self):
        self._cube = None
        self._visualizer = None
        self._players = []
        self._current_level = None
        self._current_player = None

    def new_game(self, cube_row: int, difficulty_level: int) -> None:  # create cube, 3 levels, player
        """"""
        self._cube = Cube(cube_row, difficulty_level)
        self._cube.create_rooms()
        start_level = self._cube.get_random_level()
        self._current_level = start_level
        self._cube.create_traps_on_level(self._cube.get_difficulty(),
                                         self._cube.get_level(start_level),
                                         start_level)
        if start_level > 0:
            upper_level = start_level - 1
            self._cube.create_traps_on_level(self._cube.get_difficulty(),
                                             self._cube.get_level(upper_level),
                                             upper_level)

        if start_level < self._cube.get_row() - 1:
            under_level = start_level + 1
            self._cube.create_traps_on_level(self._cube.get_difficulty(),
                                             self._cube.get_level(under_level),
                                             under_level)

        start_loc = self._cube.get_random_safe_room_coords(start_level)
        player_one = Player(start_loc[0], start_loc[1], start_loc[2])
        self._current_player = player_one
        self._players.append(player_one)

    def create_visualizer(self, cube_side_pxls: int,
                          frame_color: Colors, player_color: Colors,
                          trap_color: Colors, examined_color: Colors,
                          not_examined_color: Colors) -> None:
        """"""
        self._visualizer = Visualizer(cube_side_pxls, self._cube.get_row(),
                                      frame_color, player_color,
                                      trap_color, examined_color,
                                      not_examined_color)
        self._visualizer.set_rooms()

    def process(self) -> None:  # temporary test solution
        """"""
        self._visualizer.visualize(self._cube.get_level(self._current_level),
                                   self._current_player)
        step = input("next step")
        if step == '1':
            self._cube.move_player(self._current_player, Steps.UP)
            print(self._current_player.get_coords())
        elif step == '2':
            self._cube.move_player(self._current_player, Steps.LEFT)
            print(self._current_player.get_coords())
        elif step == '3':
            self._cube.move_player(self._current_player, Steps.RIGHT)
            print(self._current_player.get_coords())
        elif step == '4':
            self._cube.move_player(self._current_player, Steps.DOWN)
            print(self._current_player.get_coords())
