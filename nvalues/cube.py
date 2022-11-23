from nvalues.types import ValueT, XKeyT, YKeyT, ZKeyT
from nvalues.volume import Volume


class Cube(Volume[tuple[XKeyT, YKeyT, ZKeyT], ValueT]):
    """
    A three-dimensional volume of values.
    """

    def get(self, x: XKeyT, y: YKeyT, z: ZKeyT) -> ValueT:
        """
        Gets the value of key `x, y, z`.
        """

        return self[(x, y, z)]

    def set(self, x: XKeyT, y: YKeyT, z: ZKeyT, value: ValueT) -> None:
        """
        Sets the value of key `x, y, z`.
        """

        self[(x, y, z)] = value
