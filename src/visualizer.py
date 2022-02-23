"""Module contains class Visualizer."""
import numpy as np
import cv2
from resources.colors import Colors
from src.room import Room
from src.player import Player


class Visualizer:
    """Visualize game playing field.
    Player can see its current location on the field,
    examined and not examined rooms,
    trap rooms if player explore its."""

    def __init__(self, cube_row: int):
        self._frame_color: tuple = Colors.FRAME_COLOR.value
        self._player_color: tuple = Colors.PLAYER_COLOR.value
        self._trap_color: tuple = Colors.TRAP_COLOR.value
        self._exit_color: tuple = Colors.EXIT_COLOR.value
        self._examined_color: tuple = Colors.EXAMINED_COLOR.value
        self._not_examined_color: tuple = Colors.NOT_EXAMINED_COLOR.value

        self._cube_side_pxls: int = 0
        self._room_side_pxls: int = 0
        self._scale = 0
        self._cube_row: int = cube_row
        self._rooms_coordinates: list = []

    def set_visualization(self, room_side_pxls: int, scale: int) -> None:
        """Sets room side and cube side in pixels on the visualization."""
        self._room_side_pxls = room_side_pxls
        self._cube_side_pxls = self._room_side_pxls * self._cube_row
        self._scale = scale

    def set_rooms(self) -> None:
        """Sets start point of the rooms on the visualization."""
        for y in range(0, self._cube_side_pxls, self._room_side_pxls):
            row = []
            for x in range(0, self._cube_side_pxls, self._room_side_pxls):
                start_room_point = y, x
                row.append(start_room_point)
            self._rooms_coordinates.append(row)

    def draw_frame(self, visualization) -> None:
        """Draws frames between rooms."""

        """Vertical frame."""
        for start_point in range(0, self._cube_side_pxls, self._room_side_pxls):
            for point in range(0, self._cube_side_pxls):
                visualization[start_point][point] = self._frame_color

        """Horizontal frame."""
        for start_point in range(0, self._cube_side_pxls, self._room_side_pxls):
            for point in range(0, self._cube_side_pxls):
                visualization[point][start_point] = self._frame_color

    def draw_room(self, visualization, coords: tuple, room_status: dict) -> None:
        """"""
        for color in room_status:
            if room_status[color] is True:
                for y in range(
                        (self._rooms_coordinates[2] + 1),
                        (self._rooms_coordinates[2] + self._room_side_pxls)
                ):
                    for x in range(
                            (self._rooms_coordinates[1] + 1),
                            (self._rooms_coordinates[1] + self._room_side_pxls)
                    ):
                        visualization[y][x] = color
                return




        # step = int((self._cube_side_pxls / self._cube_row))  # need to change
        #
        # # cv2.floodFill(visualization, None, seedPoint=room_coordinates, newVal=self._trap_color)
        # cur_x = room_coordinates[1]
        # cur_y = room_coordinates[0]
        # limit_x = cur_x + int((self._cube_side_pxls / self._cube_row)) - 1
        # limit_y = cur_y + int((self._cube_side_pxls / self._cube_row)) - 1
        # while cur_x < limit_x:
        #     while cur_y < limit_y:
        #         if player:
        #             visualization[cur_y][cur_x] = self._player_color
        #         elif exit_room:
        #             visualization[cur_y][cur_x] = self._exit_color
        #         elif trap:
        #             visualization[cur_y][cur_x] = self._trap_color
        #         elif examined:
        #             visualization[cur_y][cur_x] = self._examined_color
        #         else:
        #             visualization[cur_y][cur_x] = self._not_examined_color  # customize color options
        #         cur_y += 1
        #     cur_x += 1
        #     cur_y = room_coordinates[0]

    def visualize(self, cube_level_instance: list,
                  player: Player) -> None:
        """"""
        visualization = np.zeros((self._cube_side_pxls, self._cube_side_pxls, 3), dtype='uint8')

        self.draw_frame(visualization)
        row_number = 0
        room_number = 0
        while row_number < self._cube_row:
            while room_number < self._cube_row:
                self.draw_room(visualization,
                               self._rooms_coordinates[row_number][room_number],
                               cube_level_instance[row_number][room_number].is_player_here,
                               cube_level_instance[row_number][room_number].is_exit,
                               cube_level_instance[row_number][room_number].is_trap,
                               cube_level_instance[row_number][room_number].is_examined(player))
                room_number += 1
            row_number += 1
            room_number = 0
        scale = 2
        vis_image = cv2.resize(visualization, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        cv2.imwrite('vis.png', vis_image)  # fix for more images
        cv2.imshow('vis', vis_image)
        cv2.waitKey()

    def vis_test(self, coords, room_status):  # delete after all testing
        visualization = np.zeros((self._cube_side_pxls, self._cube_side_pxls, 3), dtype='uint8')
        self.draw_frame(visualization)
        self.draw_room(visualization, coords, room_status)
        scale = 2
        vis_image = cv2.resize(visualization, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        cv2.imshow('vis', vis_image)
        cv2.waitKey()
