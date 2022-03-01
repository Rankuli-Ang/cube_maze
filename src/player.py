"""Contains class Player - main active character."""
from resources.steps import Steps, step_difference


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

    def __init__(self, start_coords: tuple):
        """Creates a player instance.
        Start_coords is tuple(level, x, y)."""
        self._coords: tuple = start_coords[0], start_coords[1], start_coords[2]
        self._shoes: int = 2
        self._examined_rooms_coords: list = [self._coords]
        self._alive: bool = True
        self._stats: dict = {
            "coords": self._coords,
            "shoes": self._shoes,
            "examined_rooms_coords": self._examined_rooms_coords,
        }  # add alive status ???

    def get_coords(self) -> tuple:
        """Returns player's coordinates(level, x, y)."""
        return self._coords

    def get_shoes(self) -> int:
        """Gets number of shoes a player has."""
        return self._shoes

    def get_examined_rooms(self) -> list:
        """Gets list of examined by player rooms."""
        return self._examined_rooms_coords

    def get_stats(self) -> dict:
        """Gets player's stats in dict(without alive status)."""
        return self._stats

    @property
    def is_alive(self) -> bool:
        """If Player is alive returns True."""
        return self._alive

    def add_examined_room_coords(self, room_coords: tuple) -> None:
        """Adds room's coordinates
        to the list of examined rooms."""
        if room_coords in self._examined_rooms_coords:
            return
        else:
            self._examined_rooms_coords.append(room_coords)

    def explore_room(self, step: Steps, room_is_trap: bool) -> None:  # add message if room is trap
        """Adds room coords to list of examined rooms coords,
        if room is a trap, player lose 1 shoe."""
        self.add_examined_room_coords(
            step_difference(self._coords, step)
        )
        if room_is_trap:
            self._shoes -= 1

    def move(self, step: Steps) -> None:
        """Changes the player's coordinates to the step value."""
        print('pl coord', self._coords)
        self._coords = step_difference(self._coords, step)
        print('pl coord after', self._coords)
        self.add_examined_room_coords(self.get_coords())





