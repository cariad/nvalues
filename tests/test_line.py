from nvalues import Line


def test() -> None:
    line = Line[int, str]()
    line.set(0, "foo")
    assert line.get(0) == "foo"
