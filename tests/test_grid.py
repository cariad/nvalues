from nvalues import Grid


def test_default() -> None:
    assert Grid[int, int, str]("default").get(0, 0) == "default"


def test_set() -> None:
    line = Grid[int, int, str]()
    line.set(0, 0, "foo")
    assert line.get(0, 0) == "foo"
