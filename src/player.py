"""Contains class Player - main active character."""
from resources.steps import Steps


class Player:
    """Main active game character class.
    Player travel the cube moves from room to room,
    if room has a trap, player dies.
    Player's aim is to find exit room.
    Player has attributes:
    coordinates(level, x, y), a certain amount of shoes,
    list of coordinates examined rooms
    and alive bool status.
    """

    def __init__(self, level: int, x: int, y: int):
        self._coords: tuple = level, x, y
        self._shoes: int = 2
        self._examined_rooms: list = [self._coords]
        self._alive: bool = True

    def get_coords(self) -> tuple:
        """Returns player's coordinates(level, x, y)."""
        return self._coords

    def get_shoes(self) -> int:
        """Gets number of shoes a player has."""
        return self._shoes

    def get_examined_rooms(self) -> list:
        """Gets list of examined by player rooms."""
        return self._examined_rooms

    def get_stats(self) -> list:  # test function
        """Gets all stats of player"""
        stats = []
        stats.append(self.get_coords())
        stats.append(self._shoes)
        stats.append(self._examined_rooms)
        stats.append(self._alive)

        return stats

    @property
    def is_alive(self) -> bool:
        """If Player is alive returns True."""
        return self._alive

    def add_examined_room(self, room_coords: tuple) -> None:
        """Adds room's coordinates
        to the list of examined rooms."""
        examined_room = room_coords[0], room_coords[1], room_coords[2]
        if examined_room in self._examined_rooms:
            return
        else:
            self._examined_rooms.append(examined_room)

    def throw_a_shoe(self) -> None:
        """Reduces player's shoes by 1."""
        self._shoes -= 1

    def move(self, step: Steps) -> None:
        """Changes the player's coordinates to the step value."""
        self._coords[0] += step.value[0]
        self._coords[1] += step.value[1]
        self._coords[2] += step.value[2]
        self.add_examined_room(self.get_coords())





