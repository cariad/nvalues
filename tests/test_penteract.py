from .types import PenteractType


def test_delete(penteract: PenteractType) -> None:
    penteract.delete(0, 0, 0, 0, 0)
    assert penteract.get(0, 0, 0, 0, 0) == "default"


def test_get(penteract: PenteractType) -> None:
    assert penteract.get(0, 0, 0, 0, 0) == "foo"
