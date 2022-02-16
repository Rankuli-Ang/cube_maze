""""""
import numpy as np
import cv2
from resources.colors import Colors
from src.room import Room
from src.player import Player


class Visualizer:
    """"""

    def __init__(self, cube_side_pxls: int, cube_row: int,
                 frame_color: Colors, player_color: Colors,
                 trap_color: Colors, exit_color: Colors,
                 examined_color: Colors, not_examined_color: Colors):
        self._cube_side_pxls: int = cube_side_pxls
        self._cube_row: int = cube_row

        self._frame_color: tuple = frame_color.value
        self._player_color: tuple = player_color.value
        self._trap_color: tuple = trap_color.value
        self._exit_color: tuple = exit_color.value
        self._examined_color: tuple = examined_color.value
        self._not_examined_color: tuple = not_examined_color.value

        self._rooms_coordinates: list = []

    def set_rooms(self) -> None:
        """"""
        step_width = int((self._cube_side_pxls / self._cube_row))
        step_height = int((self._cube_side_pxls / self._cube_row))
        cur_width = 0

        while cur_width < self._cube_side_pxls:
            cur_height = 0
            new_level = []
            while cur_height < self._cube_side_pxls:
                start_room_point = cur_width, cur_height
                new_level.append(start_room_point)
                cur_height += step_height
            cur_width += step_width
            self._rooms_coordinates.append(new_level)

    def draw_frame(self, visualization) -> None:
        """"""
        step_width = int((self._cube_side_pxls / self._cube_row))
        step_height = int((self._cube_side_pxls / self._cube_row))

        """vertical frame"""
        cur_height = step_height

        while cur_height < self._cube_side_pxls:
            cur_counter = 0
            while cur_counter < self._cube_side_pxls:
                visualization[cur_counter][cur_height] = self._frame_color
                cur_counter += 1
            cur_height += step_height

        """horizontal frame"""
        cur_width = step_width

        while cur_width < self._cube_side_pxls:
            cur_counter = 0
            while cur_counter < self._cube_side_pxls:
                visualization[cur_width][cur_counter] = self._frame_color
                cur_counter += 1
            cur_width += step_width

    def draw_room(self, visualization,
                  room_coordinates: tuple, player: bool, exit_room: bool, trap: bool, examined: bool) -> None:
        """"""
        step = int((self._cube_side_pxls / self._cube_row))  # need to change

        # cv2.floodFill(visualization, None, seedPoint=room_coordinates, newVal=self._trap_color)
        cur_x = room_coordinates[1]
        cur_y = room_coordinates[0]
        limit_x = cur_x + int((self._cube_side_pxls / self._cube_row)) - 1
        limit_y = cur_y + int((self._cube_side_pxls / self._cube_row)) - 1
        while cur_x < limit_x:
            while cur_y < limit_y:
                if player:
                    visualization[cur_y][cur_x] = self._player_color
                elif exit_room:
                    visualization[cur_y][cur_x] = self._exit_color
                elif trap:
                    visualization[cur_y][cur_x] = self._trap_color
                elif examined:
                    visualization[cur_y][cur_x] = self._examined_color
                else:
                    visualization[cur_y][cur_x] = self._not_examined_color  # customize color options
                cur_y += 1
            cur_x += 1
            cur_y = room_coordinates[0]

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
