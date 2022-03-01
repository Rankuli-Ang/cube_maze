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

    def draw_room(self, visualization, coords: tuple, room_status: Colors) -> None:
        """Draws room with a given Color."""
        start_x = self._rooms_coordinates[coords[2]][coords[1]][1]
        start_y = self._rooms_coordinates[coords[2]][coords[1]][0]

        for y in range(
                start_y,
                (start_y + self._room_side_pxls - 1)
        ):
            for x in range(
                    start_x,
                    (start_x + self._room_side_pxls - 1)
            ):
                visualization[y][x] = room_status.value

    def visualize(self, room_statuses: dict) -> None:
        """Visualizes game field."""
        visualization = np.zeros((self._cube_side_pxls, self._cube_side_pxls, 3), dtype='uint8')
        self.draw_frame(visualization)
        for room in room_statuses:
            self.draw_room(visualization, room, room_statuses[room])

        vis_image = cv2.resize(visualization, None,
                               fx=self._scale, fy=self._scale,
                               interpolation=cv2.INTER_NEAREST)
        cv2.imwrite('vis.png', vis_image)
        cv2.imshow('vis', vis_image)
        cv2.waitKey()

