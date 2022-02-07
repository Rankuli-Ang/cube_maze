""""""
import numpy as np
import cv2
from resources.colors import Colors
from src.room import Room
from src.player import Player


class Visualizer:
    """"""

    def __init__(self, cube_width: int, cube_height: int, cube_row: int,
                 frame_color: Colors, player_color: Colors,
                 trap_color: Colors, not_examined_color: Colors, examined_color: Colors):
        self._cube_height = cube_height
        self._cube_width = cube_width
        self._cube_row = cube_row

        self._frame_color = frame_color.value
        self._player_color = player_color.value
        self._trap_color = trap_color.value
        self._examined_color = examined_color.value
        self._not_examined_color = not_examined_color.value

        self._rooms_coordinates = []

    def set_rooms(self) -> None:
        """"""
        step_width = int((self._cube_width / self._cube_row))
        step_height = int((self._cube_height / self._cube_row))
        cur_height = 0

        while cur_height < self._cube_height:
            cur_width = 0
            new_level = []
            while cur_width < self._cube_width:
                start_room_point = cur_width, cur_height
                new_level.append(start_room_point)
                cur_width += step_width
            cur_height += step_height
            self._rooms_coordinates.append(new_level)

    def draw_point(self, visualization) -> None:
        for level in self._rooms_coordinates:
            print(level)
            for room in level:
                print(room)
                visualization[room[0]][room[1]] = self._trap_color

    def draw_frame(self, visualization) -> None:
        """"""
        step_width = int((self._cube_width / self._cube_row))
        step_height = int((self._cube_height / self._cube_row))

        """vertical frame"""
        cur_height = step_height

        while cur_height < self._cube_height:
            cur_counter = 0
            while cur_counter < self._cube_width:
                visualization[cur_counter][cur_height] = self._frame_color
                cur_counter += 1
            cur_height += step_height

        """horizontal frame"""
        cur_width = step_width

        while cur_width < self._cube_width:
            cur_counter = 0
            while cur_counter < self._cube_height:
                visualization[cur_width][cur_counter] = self._frame_color
                cur_counter += 1
            cur_width += step_width

    def draw_room(self, visualization,
                  room_coordinates: tuple, player: bool, trap: bool, examined: bool) -> None:  # add examined rooms
        """"""
        step = int((self._cube_height / self._cube_row))  # need to change

        # cv2.floodFill(visualization, None, seedPoint=room_coordinates, newVal=self._trap_color)
        cur_x = room_coordinates[0]
        cur_y = room_coordinates[1]
        limit_x = cur_x + int((self._cube_width / self._cube_row)) - 1  # correct visualization
        limit_y = cur_y + int((self._cube_height / self._cube_row)) - 1
        while cur_y < limit_y:
            while cur_x < limit_x:
                if player:
                    visualization[cur_x][cur_y] = self._player_color
                    print('player cords in vis', cur_x, cur_y)
                elif trap:
                    visualization[cur_x][cur_y] = self._trap_color
                elif examined:
                    visualization[cur_x][cur_y] = self._examined_color
                else:
                    visualization[cur_x][cur_y] = self._not_examined_color  # customize color options
                cur_x += 1
            cur_y += 1
            cur_x = room_coordinates[0]

    def visualize(self, cube_row: int, cube_level: list,
                  current_level_index: int, player: Player) -> None:  # create player checks - сейчас игрок передается всей визуализации
        """"""
        visualization = np.zeros((self._cube_width, self._cube_height, 3), dtype='uint8')

        self.draw_frame(visualization)
        row_number = 0
        room_number = 0
        while row_number < cube_row:
            while room_number < cube_row:
                is_examined = cube_level[row_number][room_number].is_examined(player)
                self.draw_room(visualization,
                               self._rooms_coordinates[row_number][room_number],
                               cube_level[row_number][room_number].is_player_here,
                               cube_level[row_number][room_number].is_trap,
                               is_examined)
                room_number += 1
            row_number += 1
            room_number = 0
        scale = 2
        vis_image = cv2.resize(visualization, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        cv2.imshow('vis', vis_image)
        cv2.waitKey()
