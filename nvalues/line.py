from nvalues.types import ValueT, XKeyT
from nvalues.volume import Volume


class Line(Volume[tuple[XKeyT], ValueT]):
    """
    A 1-dimensional volume of values.
    """

    def get(self, x: XKeyT) -> ValueT:
        """
        Gets the value of key `x`.
        """

        return self[(x,)]

    def set(self, x: XKeyT, value: ValueT) -> None:
        """
        Sets the value of key `x`.
        """

        self[(x,)] = value
