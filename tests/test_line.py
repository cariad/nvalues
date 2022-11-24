from .types import LineType


def test_delete(line: LineType) -> None:
    line.delete(0)
    assert line.get(0) == "default"


def test_get(line: LineType) -> None:
    assert line.get(0) == "foo"
