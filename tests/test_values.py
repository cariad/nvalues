from pytest import mark

from nvalues.values import Values


@mark.parametrize(
    "key, expect",
    [
        ((0,), "zero"),
        ((1,), "one"),
        ((2,), "default"),
    ],
)
def test_1d(key: tuple[int], expect: str) -> None:
    """Test one-dimensional setting and getting."""

    values = Values[tuple[int], str]("default")
    values[(0,)] = "zero"
    values[(1,)] = "one"
    assert values[key] == expect


@mark.parametrize(
    "key, expect",
    [
        ((0, 0), "zero-zero"),
        ((0, 1), "zero-one"),
        ((1, 0), "one-zero"),
        ((1, 1), "one-one"),
        ((0, 2), "default"),
        ((1, 2), "default"),
        ((2, 2), "default"),
    ],
)
def test_2d(key: tuple[int, int], expect: str) -> None:
    """Test two-dimensional setting and getting."""

    values = Values[tuple[int, int], str]("default")
    values[0, 0] = "zero-zero"
    values[0, 1] = "zero-one"
    values[1, 0] = "one-zero"
    values[1, 1] = "one-one"
    assert values[key] == expect


@mark.parametrize(
    "key, expect",
    [
        ((0, 0, 0), "zero-zero-zero"),
        ((0, 0, 1), "zero-zero-one"),
        ((0, 1, 0), "zero-one-zero"),
        ((0, 1, 1), "zero-one-one"),
        ((1, 0, 0), "one-zero-zero"),
        ((1, 0, 1), "one-zero-one"),
        ((1, 1, 0), "one-one-zero"),
        ((1, 1, 1), "one-one-one"),
        ((0, 0, 2), "default"),
        ((0, 1, 2), "default"),
        ((0, 2, 2), "default"),
        ((1, 0, 2), "default"),
        ((1, 1, 2), "default"),
        ((1, 2, 2), "default"),
        ((2, 0, 2), "default"),
        ((2, 1, 2), "default"),
        ((2, 2, 2), "default"),
    ],
)
def test_dd(key: tuple[int, int, int], expect: str) -> None:
    """Test three-dimensional setting and getting."""

    values = Values[tuple[int, int, int], str]("default")

    values[0, 0, 0] = "zero-zero-zero"
    values[0, 0, 1] = "zero-zero-one"

    values[0, 1, 0] = "zero-one-zero"
    values[0, 1, 1] = "zero-one-one"

    values[1, 0, 0] = "one-zero-zero"
    values[1, 0, 1] = "one-zero-one"

    values[1, 1, 0] = "one-one-zero"
    values[1, 1, 1] = "one-one-one"

    assert values[key] == expect
