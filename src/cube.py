"""Contains game field class Cube."""
import random
from src.room import Room
from src.player import Player
from resources.steps import Steps


class Cube:
    """Cube is a 3d game field, consisting of rooms.
    _row_length - is a side of the cube,
    level is plane with a side equivalent the _row_length.
    _difficulty is a number of rooms with a traps on the level."""

    def __init__(self, row_length: int, difficulty_coefficient: float):
        """"""
        self._row_length: int = row_length
        self._square = self._row_length * self._row_length
        self._difficulty: int = int(self._square * difficulty_coefficient)
        self._levels: list = []
        self._generated_levels_indexes: list = []

    """Get functions."""

    def get_row(self) -> int:
        """Returns row value of cube."""
        return self._row_length

    def get_difficulty(self) -> int:
        """Gets difficulty."""
        return self._difficulty

    def get_level(self, level_index: int) -> list:
        """Gets level with a given index."""
        return self._levels[level_index]

    def get_levels(self) -> list:
        """Returns list of cube's levels."""
        return self._levels

    def get_random_level_index(self) -> int:
        """Gets random level index."""
        return random.randrange(0, self._row_length)

    def get_room_by_cords(self, room_coords: tuple) -> Room:
        """Gets room with a given coordinates."""
        return self._levels[room_coords[0]][room_coords[2]][room_coords[1]]

    def get_random_safe_room_coords(self, current_level_index: int) -> tuple:
        """Gets random safe coords in the level with a given level index."""
        search = True
        while search:
            row = random.randrange(0, self._row_length)
            room = random.randrange(0, self._row_length)
            if not self._levels[current_level_index][row][room].is_trap:
                return current_level_index, room, row

    """Create functions."""
    # need to test -----------------------------------------------------------------------------------
    def create_rooms(self) -> None:
        """Creates start set of the empty rooms."""
        for level_index in range(0, self._row_length):
            new_level = []
            for row_index in range(0, self._row_length):
                new_row = []
                [new_row.append(Room((level_index, room_index, row_index)))
                 for room_index in range(0, self._row_length)]
                new_level.append(new_row)
            self._levels.append(new_level)

    def create_traps_on_level(self, level_index: int) -> None:
        """Creates traps in the given level
        with probability depending on difficulty."""
        if level_index in self._generated_levels_indexes:
            return
        for row in self._levels[level_index]:
            [room.add_trap() for room in row
             if random.randrange(0, self._square) <= self._difficulty]
        self._generated_levels_indexes.append(level_index)

    #  refactoring line ----------------------------------------------------------------------------------------
    def create_traps_around_start_loc(self, start_level_index: int) -> None:
        """Creates trap in the start level,
         if the start level index != 0 in the upper level
         and if the start level index < _row_length - 1
         creates traps in the under level."""
        self.create_traps_on_level(self.get_level(start_level_index))
        if start_level_index > 0:
            upper_level_index = start_level_index - 1
            self.create_traps_on_level(self.get_level(upper_level_index))

        if start_level_index < self._row_length - 1:
            under_level_index = start_level_index + 1
            self.create_traps_on_level(self.get_level(under_level_index))

    def create_exit(self, temporary_player_level_instance: list) -> tuple:
        """Creates exit in random border room and returns its coordinates."""
        potential_rooms = []
        for row in temporary_player_level_instance:
            for room in row:
                if not room.is_trap:
                    room_coords = room.get_coords()
                    if room_coords[1] == self._row_length - 1 or room_coords[1] == 0:
                        potential_rooms.append(room)
                    if room_coords[2] == self._row_length - 1 or room_coords[2] == 0:
                        potential_rooms.append(room)

        exit_room = random.choice(potential_rooms)
        exit_room.set_exit()
        return exit_room.get_coords()

    def get_neighbour_room_by_step(self, current_coords: tuple, step: Steps) -> Room:  # update name to better one
        """"""
        neighbour_level = current_coords[0] - step.value[0]
        neighbour_x = current_coords[1] - step.value[1]
        neighbour_y = current_coords[2] - step.value[2]
        return self._levels[neighbour_level][neighbour_y][neighbour_x]

    def get_neighbour_rooms(self, current_coords: tuple) -> dict:  # need to fix, add with a bool version
        """"""
        current_level = self._levels[current_coords[0]]
        neighbour_rooms = {}

        if current_coords[1] > 0:
            left_room = current_level[current_coords[2]][current_coords[1] - 1]
            neighbour_rooms[Steps.LEFT] = left_room
        if current_coords[1] < 15:
            right_room = current_level[current_coords[2]][current_coords[1] + 1]
            neighbour_rooms[Steps.RIGHT] = right_room
        if current_coords[2] > 0:
            upper_room = current_level[current_coords[2] - 1][current_coords[1]]
            neighbour_rooms[Steps.UP] = upper_room
        if current_coords[2] < 15:
            down_room = current_level[current_coords[2] + 1][current_coords[1]]
            neighbour_rooms[Steps.DOWN] = down_room

        if current_coords[0] > 0:
            up_level = self._levels[current_coords[0] - 1]
            up_level_room = up_level[current_coords[2]][current_coords[1]]
            neighbour_rooms[Steps.UP_LEVEL] = up_level_room
        if current_coords[0] < 15:
            down_level = self._levels[current_coords[0] + 1]
            down_level_room = down_level[current_coords[2]][current_coords[1]]
            neighbour_rooms[Steps.DOWN_LEVEL] = down_level_room
        return neighbour_rooms

    def add_player_by_coords(self, coords: tuple, player: Player) -> None:
        """Adds player in the room's list."""
        self._levels[coords[0]][coords[2]][coords[1]].add_player(player)

    # def move_player(self, player: Player, step: Steps) -> None:
    #     """"""
    #     previous_room_coords = player.get_coords()
    #     previous_room = self.get_room_by_cords(previous_room_coords)
    #     if step == Steps.UP_LEVEL:
    #         double_up_level_index = previous_room_coords[0] - 2
    #         if double_up_level_index >= 0:
    #             if double_up_level_index not in self._generated_levels_indexes:
    #                 self.create_traps_on_level(self._difficulty)
    #
    #     if step == Steps.DOWN_LEVEL:
    #         double_down_level_index = previous_room_coords[0] - 2
    #         if double_down_level_index <= 15:
    #             if double_down_level_index not in self._generated_levels_indexes:
    #                 self.create_traps_on_level(self._difficulty)
    #
    #     player.move(step)
    #
    #     next_room_coords = player.get_coords()
    #     next_room = self.get_room_by_cords(next_room_coords)
    #     next_room.add_player(player)
    #     next_room.create_doors(self.get_neighbour_rooms(next_room_coords))
    #     previous_room.del_player(player))
