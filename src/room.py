"""Contains class Room -
is the point of the cube
on which the player moves."""
from src.player import Player
from resources.steps import Steps
import random


# prime_numbers_raw = open(r'prime_numbers.txt')  # temporary place
# prime_numbers_raw = prime_numbers_raw.read().split()
# prime_numbers = []
# for prime_number in prime_numbers_raw:
#     new_number = int(prime_number)
#     prime_numbers.append(new_number)
#
# counter = 0
# not_prime_numbers = []
# while counter < 1000:
#     counter += 1
#     if counter not in prime_numbers:
#         not_prime_numbers.append(counter)


class Room:
    """"""

    def __init__(self, level: int, x: int, y: int):
        self._coords: tuple = level, x, y
        self._players: list = []
        self._doors: dict = {}
        self._trap: bool = False
        # to add types of traps
        self._exit: bool = False
        # self._processed = False
        # resolve border rooms nuances

    def get_coords(self) -> tuple:
        """Gets room's coordinates."""
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

    def is_examined(self, player: Player) -> bool:
        """Returns True if room examined by player."""
        if self.get_coords() in player.get_examined_rooms():
            return True
        else:
            return False

    # def create_doors(self, neighbour_rooms: dict) -> None:  # doubtful design, fix later
    #     """Adds to self._doors pairs Steps(key) - tuple of three numbers(value).
    #     If neighbour room (with a Steps coord shift) has a trap -
    #     from 1 to 3 of the numbers is prime."""
    #     for neighbour in neighbour_rooms:
    #         if neighbour_rooms[neighbour].is_trap:
    #
    #             prime_amount = random.randint(1, 3)
    #             counter = 1
    #             door_numbers = []
    #             while counter <= prime_amount:
    #                 door_numbers.append(random.choice(prime_numbers))
    #                 counter += 1
    #             while len(door_numbers) < 3:
    #                 door_numbers.append(random.choice(not_prime_numbers))
    #             random.shuffle(door_numbers)
    #             self._doors[neighbour] = (
    #                 door_numbers[0], door_numbers[1],
    #                 door_numbers[2]
    #             )
    #         else:
    #             self._doors[neighbour] = (
    #                 random.choice(not_prime_numbers),
    #                 random.choice(not_prime_numbers),
    #                 random.choice(not_prime_numbers)
    #             )
