""""""
import random
from src.room import Room


class Cube:
    """"""

    def __init__(self, row: int, difficulty: int):
        self._row = row
        self._levels = []
        self._generated_levels_index = []

    def get_row(self) -> int:
        """Returns row value of cube."""
        return self._row

    def get_levels(self) -> list:
        """Returns list of cube's levels."""
        return self._levels

    def get_level(self, level_index: int) -> list:
        """"""
        return self._levels[level_index]

    def create_rooms(self) -> None:
        """"""
        cur_level = 0
        cur_x = 0
        cur_y = 0

        while cur_level < self._row:
            new_level = []
            while cur_y < self._row:
                new_row = []
                while cur_x < self._row:
                    new_room = Room(cur_x, cur_y)
                    new_row.append(new_room)
                    cur_x += 1
                new_level.append(new_row)
                cur_x = 0
                cur_y += 1
            self._levels.append(new_level)
            cur_x = 0
            cur_y = 0
            cur_level += 1

    def create_traps_on_level(self, cube_square: int, difficulty_level: int,
                              cube_instance_level: list, cube_instance_level_index: int) -> None:
        """"""
        if cube_instance_level_index in self._generated_levels_index:
            return
        for row in cube_instance_level:
            for room in row:
                trap_score = random.randrange(0, cube_square)
                if trap_score <= difficulty_level:
                    room.add_trap()
        self._generated_levels_index.append(cube_instance_level_index)

    def get_neighbour_rooms(self, current_level_index: int, current_room_x: int, current_room_y: int) -> list:
        """"""
        current_level = self._levels[current_level_index]
        neighbour_rooms = []

        if current_room_x > 0:
            left_room = current_level[current_room_x - 1][current_room_y]
            neighbour_rooms.append(left_room)
        if current_room_x < 15:
            right_room = current_level[current_room_x + 1][current_room_y]
            neighbour_rooms.append(right_room)
        if current_room_y > 0:
            upper_room = current_level[current_room_x][current_room_y - 1]
            neighbour_rooms.append(upper_room)
        if current_room_y < 15:
            down_room = current_level[current_room_x][current_room_y + 1]
            neighbour_rooms.append(down_room)

        if current_level_index > 0:
            up_level = self._levels[current_level_index - 1]
            up_level_room = up_level[current_room_x][current_room_y]
            neighbour_rooms.append(up_level_room)

        if current_level_index < 15:
            down_level = self._levels[current_level_index + 1]
            down_level_room = down_level[current_room_x][current_room_y]
            neighbour_rooms.append(down_level_room)
        return neighbour_rooms

    def add_player(self, level: int, x: int, y: int) -> None:
        """Adds player in the room's list."""
        self._levels[level][x][y].add_player()
