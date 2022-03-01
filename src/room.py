"""Contains class Room -
is the cell of the cube
on which the player moves."""
import random
from typing import List
from src.player import Player


class Room:
    """Cell unit of the cube.
    Room may contains trap or exit or nothing.
    If player comes into the room with a trap - he dies ang game over,
    with an exit - player wins.
    Room has attributes:
    -coords tuple(level, x, y),
    -list of players in the room,
    trap and exit presence - bool."""

    def __init__(self, coords: tuple):
        """Creates room instance with a given coords(level, x, y),
        trap, exit, and doors creates separately."""
        self._coords: tuple = coords[0], coords[1], coords[2]
        self._players: list = []
        self._doors: dict = {}
        self._trap: bool = False
        self._exit: bool = False

    def get_coords(self) -> tuple:
        """Gets room's coordinates in tuple(level, x, y)."""
        return self._coords

    def get_doors(self) -> dict:
        """Gets doors in dictionary with Steps as keys."""
        return self._doors

    @property
    def is_player_here(self) -> bool:
        """Returns True if player in this room."""
        if len(self._players) > 0:
            return True
        else:
            return False

    @property
    def is_trap(self) -> bool:
        """Returns True if room has a trap."""
        return self._trap

    @property
    def is_exit(self) -> bool:
        """Returns True if room has an exit."""
        return self._exit

    def add_player(self, player: Player) -> None:
        """Adds player to room's list."""
        self._players.append(player)
        if not self._doors:  # need to add doors generating
            pass

    def del_player(self, player: Player) -> None:
        """Deletes player from the room's list."""
        self._players.remove(player)

    def add_trap(self) -> None:  # add types of traps
        """Sets room._trap to True."""
        self._trap = True

    def set_exit(self) -> None:
        """Sets room._exit to True."""
        self._exit = True

    def is_examined(self, player: Player) -> bool:  # change after add mixing room func
        """Returns True if room examined by player."""
        if self.get_coords() in player.get_examined_rooms():
            return True
        else:
            return False

    def create_doors(self, neighbour_rooms_is_trap: dict, door_numbers_amount: int,
                     min_prime_numbers: int, max_prime_numbers: int,
                     prime_numbers: List[int], non_prime_numbers: List[int]) -> None:
        """Adds to self._doors pairs Steps(key) - tuple of three numbers(value).
        If neighbour room (with a Steps coord shift) has a trap -
        from 1 to 3 of the numbers is prime."""
        for neighbour in neighbour_rooms_is_trap:
            if not neighbour_rooms_is_trap[neighbour]:
                self._doors[neighbour] = [
                    random.choice(non_prime_numbers)
                    for i in range(1, door_numbers_amount + 1)]
            else:
                prime_numbers_amount = random.randint(
                    min_prime_numbers, max_prime_numbers)

                [self._doors[neighbour].append(random.choice(prime_numbers))
                    for i in range(1, prime_numbers_amount + 1)]
                if len(self._doors[neighbour]) < door_numbers_amount:
                    [self._doors[neighbour].append(random.choice(non_prime_numbers))
                     for i in range(
                        len(self._doors[neighbour]), door_numbers_amount + 1)]

