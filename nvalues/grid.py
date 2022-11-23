from nvalues.types import ValueT, XKeyT, YKeyT
from nvalues.volume import Volume


class Grid(Volume[tuple[XKeyT, YKeyT], ValueT]):
    """
    A two-dimensional volume of values.
    """

    def get(self, x: XKeyT, y: YKeyT) -> ValueT:
        """
        Gets the value of key `x, y`.
        """

        return self[(x, y)]

    def set(self, x: XKeyT, y: YKeyT, value: ValueT) -> None:
        """
        Sets the value of key `x, y`.
        """

        self[(x, y)] = value
