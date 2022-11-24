from .types import GridType


def test_delete(grid: GridType) -> None:
    grid.delete(0, 0)
    assert grid.get(0, 0) == "default"


def test_get(grid: GridType) -> None:
    assert grid.get(0, 0) == "foo"
