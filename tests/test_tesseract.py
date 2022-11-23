from nvalues import Tesseract


def test() -> None:
    cube = Tesseract[int, int, int, int, str]()
    cube.set(0, 0, 0, 0, "foo")
    assert cube.get(0, 0, 0, 0) == "foo"
