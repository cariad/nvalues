from nvalues import Value


def test_eq__not_key() -> None:
    assert Value((0, 0), "zero") != Value((1, 0), "zero")


def test_eq__not_type() -> None:
    assert Value((0, 0), "zero") != "zero"


def test_eq__not_value() -> None:
    assert Value((0, 0), "zero") != Value((0, 0), "nope")


def test_repr() -> None:
    assert repr(Value((0, 0), "zero")) == "'zero' @(0, 0)"
