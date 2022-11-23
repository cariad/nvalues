from nvalues.types import ValueT, VKeyT, WKeyT, XKeyT, YKeyT, ZKeyT
from nvalues.volume import Volume


class Penteract(Volume[tuple[VKeyT, WKeyT, XKeyT, YKeyT, ZKeyT], ValueT]):
    """
    A five-dimensional volume of values.
    """

    def get(self, v: VKeyT, w: WKeyT, x: XKeyT, y: YKeyT, z: ZKeyT) -> ValueT:
        """
        Gets the value of key `v, w, x, y, z`.
        """

        return self[(v, w, x, y, z)]

    def set(
        self,
        v: VKeyT,
        w: WKeyT,
        x: XKeyT,
        y: YKeyT,
        z: ZKeyT,
        value: ValueT,
    ) -> None:
        """
        Sets the value of key `v, w, x, y, z`.
        """

        self[(v, w, x, y, z)] = value
