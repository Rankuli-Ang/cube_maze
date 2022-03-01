"""Contains game field class Cube."""
import random
from src.room import Room
from src.player import Player
from resources.steps import Steps, STEPS, step_difference


class Cube:
    """Cube is a 3d game field, consisting of rooms.
    _row_length - is a side of the cube,
    level is square plane with a side equivalent the _row_length.
    _difficulty shows what part of level's rooms is trap."""

    def __init__(self, row_length: int, difficulty_coefficient: float):
        """"""
        self._row_length: int = row_length
        self._border_index: int = self._row_length - 1
        self._square: int = self._row_length * self._row_length
        self._difficulty: int = int(self._square * difficulty_coefficient)
        self._exit: tuple = 0, 0, 0
        self._levels: list = []
        self._generated_levels_indexes: list = []

    """Get functions."""

    def get_row_length(self) -> int:
        """Gets length of the cube row."""
        return self._row_length

    def get_border_index(self) -> int:
        """Gets border index."""
        return self._border_index

    def get_difficulty(self) -> int:
        """Gets difficulty."""
        return self._difficulty

    def get_exit_coords(self) -> tuple:
        """Gets exit coords."""
        return self._exit

    def get_level(self, level_index: int) -> list:
        """Gets level with a given index."""
        return self._levels[level_index]

    def get_levels(self) -> list:
        """Returns list of cube's levels."""
        return self._levels

    def get_random_level_index(self) -> int:
        """Gets random level index."""
        return random.randrange(0, self._row_length)

    def get_room(self, room_coords: tuple) -> Room:
        """Gets room with a given coordinates."""
        return self._levels[room_coords[0]][room_coords[2]][room_coords[1]]

    def get_neighbour_room(self, current_coords: tuple, step: Steps) -> Room:
        """Gets neighbour of the room with current coords by step value."""
        neighbour_coords = step_difference(current_coords, step)
        return self._levels[neighbour_coords[0]][neighbour_coords[2]][neighbour_coords[1]]

    def get_neighbour_rooms(self, current_coords: tuple) -> dict:  # cut the length of strings
        """Gets all neighbours of the current loc."""
        neighbour_rooms = {}
        for step in Steps:
            neighbour_coords = step_difference(current_coords, step)
            if neighbour_coords[0] >= 0 and neighbour_coords[1] >= 0 and neighbour_coords[2] >= 0:
                if neighbour_coords[0] <= 15 and neighbour_coords[1] <= 15 and neighbour_coords[2] <= 15:
                    neighbour_rooms[step] = self.get_room(neighbour_coords)
        return neighbour_rooms

    def get_random_safe_room_in_level(self, current_level_index: int) -> tuple:
        """Gets random safe coords in the level with a given level index."""
        search = True
        while search:
            row = random.randrange(0, self._row_length)
            room = random.randrange(0, self._row_length)
            if not self._levels[current_level_index][row][room].is_trap:
                return current_level_index, room, row

    """Create functions."""

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
        if level_index < 0 or level_index > self._border_index:
            return
        if level_index in self._generated_levels_indexes:
            return
        for row in self._levels[level_index]:
            [room.add_trap() for room in row
             if random.randrange(0, self._square) <= self._difficulty]
        self._generated_levels_indexes.append(level_index)

    def create_traps_around_loc(self, current_level_index: int) -> None:
        """Creates trap in the current level,
         if the current level index != 0 in the upper level
         and if the current level index < _row_length - 1
         creates traps in the under level."""
        self.create_traps_on_level(current_level_index)
        self.create_traps_on_level(current_level_index - 1)
        self.create_traps_on_level(current_level_index + 1)

    def create_exit(self) -> None:  # need to come up with more interesting mechanics
        """Creates exit in random coords."""
        loc_not_found = True
        while loc_not_found:
            random_loc = (random.randrange(0, self._row_length),
                          random.randrange(0, self._row_length),
                          random.randrange(0, self._row_length))
            if not self.get_room(random_loc).is_trap:
                self.get_room(random_loc).set_exit()
                self._exit = random_loc
                return

    """Player's interactions."""

    def add_player(self, player: Player) -> None:
        """Adds player in the room's list."""
        coords = player.get_coords()
        self._levels[coords[0]][coords[2]][coords[1]].add_player(player)
        self.create_traps_around_loc(coords[0])

    def move_player(self, player: Player, step: Steps) -> None:
        """Moves player to the next room by step value
        and creates traps in the around levels, if current level changed."""
        self.get_room(player.get_coords()).del_player(player)
        player.move(step)
        self.get_room(player.get_coords()).add_player(player)
        if step == Steps.UPPER or step == Steps.UNDER:
            self.create_traps_around_loc(player.get_coords()[0])

    """Cube Initialization."""

    def initialization(self) -> None:  # maybe create traps in all level at the beginning
        """"""
        self.create_rooms()
        self.create_exit()

