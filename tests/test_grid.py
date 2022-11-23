from nvalues import Grid


def test() -> None:
    grid = Grid[int, int, str]()
    grid.set(0, 0, "foo")
    assert grid.get(0, 0) == "foo"
