from nvalues.types import ValueT, WKeyT, XKeyT, YKeyT, ZKeyT
from nvalues.volume import Volume


class Tesseract(Volume[tuple[WKeyT, XKeyT, YKeyT, ZKeyT], ValueT]):
    """
    A four-dimensional volume of values.
    """

    def get(self, w: WKeyT, x: XKeyT, y: YKeyT, z: ZKeyT) -> ValueT:
        """
        Gets the value of key `w, x, y, z`.
        """

        return self[(w, x, y, z)]

    def set(
        self,
        w: WKeyT,
        x: XKeyT,
        y: YKeyT,
        z: ZKeyT,
        value: ValueT,
    ) -> None:
        """
        Sets the value of key `w, x, y, z`.
        """

        self[(w, x, y, z)] = value
