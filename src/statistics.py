""""""


class Statistics:
    """"""

    def __init__(self):
        self._steps_counter = 0

    def add_step(self) -> None:
        """Adds one steps counter."""
        self._steps_counter += 1

    def get_results(self) -> None:
        """"""
        print('YOU ARE A WINNER !!!')
        print('number of steps:', self._steps_counter)