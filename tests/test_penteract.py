from nvalues import Penteract


def test() -> None:
    penteract = Penteract[int, int, int, int, int, str]()
    penteract.set(0, 0, 0, 0, 0, "foo")
    assert penteract.get(0, 0, 0, 0, 0) == "foo"
