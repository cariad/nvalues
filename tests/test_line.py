from nvalues import Line


def test_default() -> None:
    assert Line[int, str]("default").get(0) == "default"


def test_set() -> None:
    line = Line[int, str]()
    line.set(0, "foo")
    assert line.get(0) == "foo"
