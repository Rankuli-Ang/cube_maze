"""Module contains class Processor."""
import random
from src.cube import Cube
from src.player import Player
from src.statistics import Statistics
from src.visualizer import Visualizer
from resources.colors import Colors
from resources.steps import Steps


class Processor:
    """"""

    def __init__(self):
        self._cube = None
        self._visualizer = None
        # self._players: list = []
        self._current_player = None  # temporary solution
        self._current_level_number = None  # temporary solution
        self._exit_room_coords = None
        self._stats = None
        self._is_activated = False

    def activate(self) -> None:
        """Changes is_activated status to True."""
        self._is_activated = True

    def create_visualizer(self,
                          cube_row: int, room_side_pxls: int,
                          scale: int) -> None:
        """"""
        self._visualizer = Visualizer(cube_row)
        self._visualizer.set_visualization(room_side_pxls, scale)
        self._visualizer.set_rooms()

    def new_game(self,
                 row_length: int, difficulty_coefficient: float
                 ) -> None:
        """"""
        self._cube = Cube(row_length, difficulty_coefficient)
        self._cube.create_rooms()
        start_level = self._cube.get_random_level_index()
        print(start_level)
        self._cube.create_traps_on_level(start_level)
        start_room_coords = self._cube.get_random_safe_room_in_level(start_level)
        player_one = Player(start_room_coords)
        self._cube.add_player(player_one)
        self._current_player = player_one
        # add doors
        exit_room_coords = self._cube.get_random_safe_room_in_level(start_level)  # del later
        while exit_room_coords == start_room_coords:
            exit_room_coords = self._cube.get_random_safe_room_in_level(start_level)
        self._cube._exit = exit_room_coords
        self._exit_room_coords = exit_room_coords

    def get_room_statuses(self) -> list:
        """"""
        all_examined_rooms_coords = self._current_player.get_examined_rooms()
        current_level_examined_rooms_coords = []
        for room in all_examined_rooms_coords:
            if room[0] == self._current_player.get_coords()[0]:
                current_level_examined_rooms_coords.append(room)

        current_level_room_statuses = []
        current_level = self._cube.get_level(self._current_player.get_coords()[0])
        for row in current_level:
            current_row = []
            for room in row:
                room_coords = room.get_coords()
                if room_coords == self._current_player.get_coords():
                    current_row.append((room_coords, Colors.PLAYER_COLOR))
                elif room_coords == self._exit_room_coords:
                    current_row.append((room_coords, Colors.EXIT_COLOR))
                elif room_coords in current_level_examined_rooms_coords:
                    if room.is_trap:
                        current_row.append((room_coords, Colors.TRAP_COLOR))
                    else:
                        current_row.append((room_coords, Colors.EXAMINED_COLOR))
                else:
                    current_row.append((room_coords, Colors.NOT_EXAMINED_COLOR))
            current_level_room_statuses.append(current_row)
        return current_level_room_statuses


    # def new_game(
    #         self, cube_row: int, difficulty_level: int, cube_side_pxls: int,
    #         frame_color: Colors, player_color: Colors, trap_color: Colors,
    #         exit_color: Colors, examined_color: Colors, not_examined_color: Colors
    # ) -> None:  # create cube, 3 levels, player
    #     # i doubt the design of this function
    #     """"""
    #     self._cube = Cube(cube_row, difficulty_level)
    #     self._cube.create_rooms()
    #     start_level_index = self._cube.get_random_level_index()
    #     self._current_level_number = start_level_index
    #     self._cube.create_traps_around_loc(start_level_index)
    #
    #     start_loc = self._cube.get_random_safe_room_in_level(start_level)
    #     player_one = Player(start_loc[0], start_loc[1], start_loc[2])
    #     self._current_player = player_one
    #     self._players.append(player_one)
    #
    #     self._cube.add_player(start_loc, player_one)
    #     start_room = self._cube.get_room(start_loc)
    #     # start_room.create_doors(self._cube.get_neighbour_rooms(start_loc))
    #
    #     self._exit_room_coords = self._cube.create_exit(
    #         self._cube.get_level(self._current_level_number)
    #     )
    #
    #     self._stats = Statistics()
    #     self.create_visualizer(
    #         cube_side_pxls, frame_color, player_color,
    #         trap_color, exit_color, examined_color, not_examined_color
    #     )
    #     self.activate()
    #
    # # def explore_room(self, player: Player, step: Steps) -> None:
    # #     """"""
    # #     if player.get_shoes() <= 0:
    # #         return
    # #     player_coords = player.get_coords()
    # #     neighbour_room = self._cube.get_neighbour_room_by_step(
    # #         player_coords[0], player_coords[1], player_coords[2], step
    # #     )
    # #     if neighbour_room.is_trap:
    # #         player.lose_a_shoe()
    # #     player.add_examined_room(neighbour_room.get_coords())
    #
    # @property
    # def is_end_game(self) -> bool:
    #     """Returns True if exit_room and player has the same coordinates."""
    #     if not self._players[0].get_coords() == self._exit_room_coords:
    #         return False
    #     else:
    #         return True
    #
    # def end_game(self) -> None:
    #     """"""
    #     self._stats.get_results()
    #
    # def get_player(self):
    #     return self._players[0]
    #
    # def process(self) -> None:  # temporary test solution
    #     """"""
    #     self._visualizer.visualize(self._cube.get_level(self._current_level_number),
    #                                self._current_player)
    #
    #     # step = input("next step")
    #     # if step == '1':
    #     #     self._cube.move_player(self._current_player, Steps.UP)
    #     # elif step == '2':
    #     #     self._cube.move_player(self._current_player, Steps.LEFT)
    #     # elif step == '3':
    #     #     self._cube.move_player(self._current_player, Steps.RIGHT)
    #     # elif step == '4':
    #     #     self._cube.move_player(self._current_player, Steps.DOWN)
    #     # elif step == '5':
    #     #     self._cube.move_player(self._current_player, Steps.UPPER)
    #     # elif step == '6':
    #     #     self._cube.move_player(self._current_player, Steps.DOWN_LEVEL)
    #     #
    #     # self._stats.add_step()
    #     # pl_coords = self._current_player.get_coords()
    #     # self._current_level_number = pl_coords[0]
    #     # self._cube.get_neighbour_rooms(pl_coords)
    #     # return self.is_end_game
