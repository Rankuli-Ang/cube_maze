""""""
import random
from src.room import Room
from src.player import Player
from resources.steps import Steps


class Cube:
    """"""

    def __init__(self, row: int, difficulty: int):
        self._row: int = row
        self._difficulty: int = difficulty
        self._levels: list = []
        self._generated_levels_index: list = []

    def get_row(self) -> int:
        """Returns row value of cube."""
        return self._row

    def get_difficulty(self) -> int:
        """"""
        return self._difficulty

    def get_levels(self) -> list:
        """Returns list of cube's levels."""
        return self._levels

    def get_level(self, level_index: int) -> list:
        """"""
        return self._levels[level_index]

    def get_room_by_cords(self, level: int, x: int, y: int) -> Room:
        return self._levels[level][y][x]

    def get_random_level(self) -> int:
        """"""
        return random.randrange(0, self._row)

    def get_random_safe_room_coords(self, current_level: int) -> tuple:  # correct
        search = True
        while search:
            row = random.randrange(0, self._row)
            room = random.randrange(0, self._row)
            if not self._levels[current_level][row][room].is_trap:
                return current_level, room, row

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
                    new_room = Room(cur_level, cur_x, cur_y)
                    new_row.append(new_room)
                    cur_x += 1
                new_level.append(new_row)
                cur_x = 0
                cur_y += 1
            self._levels.append(new_level)
            cur_x = 0
            cur_y = 0
            cur_level += 1

    def create_traps_on_level(self, difficulty_level: int,
                              cube_instance_level: list, cube_instance_level_index: int) -> None:
        """"""
        if cube_instance_level_index in self._generated_levels_index:
            return

        cube_square = self._row * self._row
        for row in cube_instance_level:
            for room in row:
                trap_score = random.randrange(0, cube_square)
                if trap_score <= difficulty_level:
                    room.add_trap()
        self._generated_levels_index.append(cube_instance_level_index)

    def get_neighbour_room_by_step(self, current_level: int,
                                   current_x: int, current_y: int,
                                   step: Steps) -> Room:  # update name to better one
        """"""
        neighbour_level = current_level - step.value[0]
        neighbour_x = current_x - step.value[1]
        neighbour_y = current_y - step.value[2]
        return self._levels[neighbour_level][neighbour_y][neighbour_x]

    def get_neighbour_rooms(self, current_level_index: int, current_room_number: int,
                            current_room_row: int) -> dict:
        """"""
        current_level = self._levels[current_level_index]
        neighbour_rooms = {}

        if current_room_number > 0:
            left_room = current_level[current_room_row][current_room_number - 1]
            print('left', left_room.get_coords())
            neighbour_rooms[Steps.LEFT] = left_room
        if current_room_number < 15:
            right_room = current_level[current_room_row][current_room_number + 1]
            print('right', right_room.get_coords())
            neighbour_rooms[Steps.RIGHT] = right_room
        if current_room_row > 0:
            upper_room = current_level[current_room_row - 1][current_room_number]
            print('upper', upper_room.get_coords())
            neighbour_rooms[Steps.UP] = upper_room
        if current_room_row < 15:
            down_room = current_level[current_room_row + 1][current_room_number]
            neighbour_rooms[Steps.DOWN] = down_room
            print('down', down_room.get_coords())

        if current_level_index > 0:
            up_level = self._levels[current_level_index - 1]
            up_level_room = up_level[current_room_row][current_room_number]
            neighbour_rooms[Steps.UP_LEVEL] = up_level_room
            print('up leve', up_level_room.get_coords())
        if current_level_index < 15:
            down_level = self._levels[current_level_index + 1]
            down_level_room = down_level[current_room_row][current_room_number]
            neighbour_rooms[Steps.DOWN_LEVEL] = down_level_room
            print('down level', down_level_room.get_coords())
        return neighbour_rooms

    def add_player_by_coords(self, level: int, x: int, y: int, player: Player) -> None:
        """Adds player in the room's list."""
        self._levels[level][y][x].add_player(player)

    def move_player(self, player: Player, step: Steps) -> None:
        """"""
        previous_room_coords = player.get_coords()
        previous_room = self.get_room_by_cords(previous_room_coords[0], previous_room_coords[1],
                                               previous_room_coords[2])
        if step == Steps.UP_LEVEL:
            double_up_level_index = previous_room_coords[0] - 2
            if double_up_level_index >= 0:
                if double_up_level_index not in self._generated_levels_index:
                    self.create_traps_on_level(self._difficulty,
                                               self._levels[double_up_level_index],
                                               double_up_level_index)

        if step == Steps.DOWN_LEVEL:
            double_down_level_index = previous_room_coords[0] - 2
            if double_down_level_index <= 15:
                if double_down_level_index not in self._generated_levels_index:
                    self.create_traps_on_level(self._difficulty,
                                               self._levels[double_down_level_index],
                                               double_down_level_index)

        player.move(step)

        next_room_coords = player.get_coords()
        next_room = self.get_room_by_cords(next_room_coords[0], next_room_coords[1], next_room_coords[2])
        next_room.add_player(player)
        next_room.create_doors(
            self.get_neighbour_rooms(next_room_coords[0],
                                     next_room_coords[1], next_room_coords[2])
        )
        previous_room.del_player(player)
