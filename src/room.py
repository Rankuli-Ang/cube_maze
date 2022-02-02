""""""


class Room:
    """"""

    def __init__(self, coordinate_x: int, coordinate_y: int):
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y
        self._players = []
        self._doors = []
        self._adjoining_rooms = []
        self._trap = None
        # to add types of traps
        self._exit = None
        # resolve border rooms nuances

    def get_adjoining_rooms(self, adjoining_rooms: list) -> None:
        """"""
        self._adjoining_rooms = adjoining_rooms

    def set_doors(self) -> None:
        """"""
        pass

    @property
    def is_trap(self) -> bool:
        """Returns True if room has a trap, else False."""
        if self._trap is None:
            return False
        else:
            return True

    @property
    def is_exit(self) -> bool:
        """Returns True if room has an exit, else False."""
        if self._exit is None:
            return False
        else:
            return True
