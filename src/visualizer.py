""""""
import numpy as np
import cv2
from resources.colors import Colors


class Visualizer:
    """"""

    def __init__(self, cube_width: int, cube_height: int, cube_row: int,
                 frame_color: Colors, trap_color: Colors):
        self._cube_height = cube_height
        self._cube_width = cube_width
        self._cube_row = cube_row
        self._frame_color = frame_color.value
        self._trap_color = trap_color.value
        self._rooms = []

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
            self._rooms.append(new_level)

    def draw_point(self, visualization) -> None:
        for level in self._rooms:
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

    def draw_room(self, visualization, room_coordinates: tuple) -> None:
        """"""
        step_height = int((self._cube_height / self._cube_row))

        cv2.floodFill(visualization, None, seedPoint=room_coordinates, newVal=self._trap_color)
        # cur_x = 0
        # cur_y = 0
        # limit = int((self._cube_width / self._cube_row))
        # while cur_y < limit:
        #     while cur_x < limit:
        #         visualization[cur_x][cur_y] = self._trap_color
        #         cur_x += 1
        #     cur_y += 1

    def visualize(self) -> None:
        """"""
        visualization = np.zeros((self._cube_width, self._cube_height, 3), dtype='uint8')

        self.draw_frame(visualization)
        self.draw_point(visualization)
        self.draw_room(visualization, self._rooms[0][0])
        scale = 2
        vis_image = cv2.resize(visualization, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        cv2.imshow('vis', vis_image)
        cv2.waitKey()
