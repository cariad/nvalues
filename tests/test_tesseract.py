from nvalues import Tesseract


def test() -> None:
    tesseract = Tesseract[int, int, int, int, str]()
    tesseract.set(0, 0, 0, 0, "foo")
    assert tesseract.get(0, 0, 0, 0) == "foo"
