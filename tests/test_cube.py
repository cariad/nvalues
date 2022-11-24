from .types import CubeType


def test_delete(cube: CubeType) -> None:
    cube.delete(0, 0, 0)
    assert cube.get(0, 0, 0) == "default"


def test_get(cube: CubeType) -> None:
    assert cube.get(0, 0, 0) == "foo"
