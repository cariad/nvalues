from nvalues import Cube


def test() -> None:
    cube = Cube[int, int, int, str]()
    cube.set(0, 0, 0, "foo")
    assert cube.get(0, 0, 0) == "foo"
