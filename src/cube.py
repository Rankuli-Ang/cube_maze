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

    def get_neighbour_rooms(self, current_level_index: int, current_room_x: int,
                            current_room_y: int) -> list:  # need to check rotation
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

    def add_player_by_coords(self, level: int, x: int, y: int, player: Player) -> None:
        """Adds player in the room's list."""
        self._levels[level][y][x].add_player(player)

    def move_player(self, player: Player, step: Steps) -> None:
        """"""
        previous_room_coords = player.get_coords()
        previous_room = self.get_room_by_cords(previous_room_coords[0], previous_room_coords[1],
                                               previous_room_coords[2])
        print('prev cord player', player.get_coords())
        print('prev room coord', previous_room.get_coords())
        print('prev room players', previous_room.is_player_here)
        player.move(step)
        print('step', step.value)
        next_room_coords = player.get_coords()
        print('next cords', player.get_coords())
        next_room = self.get_room_by_cords(next_room_coords[0], next_room_coords[1], next_room_coords[2])
        next_room.add_player(player)
        if next_room.is_trap:
            print('ITS A TRAP!')
        previous_room.del_player(player)
