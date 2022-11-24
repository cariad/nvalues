from pytest import mark, raises

from nvalues import Value, Volume
from nvalues.exceptions import InvalidKey, NKeyError, NoDefaultValue


def validate_key(key: tuple[int, int]) -> None:
    x = key[0]
    if x not in [0, 1]:
        raise ValueError(f"x {x} must be 0 or 1")


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

    v = Volume[tuple[int], str]("default")
    v[(0,)] = "zero"
    v[(1,)] = "one"
    assert v[key] == expect


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

    v = Volume[tuple[int, int], str]("default")
    v[0, 0] = "zero-zero"
    v[0, 1] = "zero-one"
    v[1, 0] = "one-zero"
    v[1, 1] = "one-one"
    assert v[key] == expect


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
def test_3d(key: tuple[int, int, int], expect: str) -> None:
    """Test three-dimensional setting and getting."""

    v = Volume[tuple[int, int, int], str]("default")

    v[0, 0, 0] = "zero-zero-zero"
    v[0, 0, 1] = "zero-zero-one"

    v[0, 1, 0] = "zero-one-zero"
    v[0, 1, 1] = "zero-one-one"

    v[1, 0, 0] = "one-zero-zero"
    v[1, 0, 1] = "one-zero-one"

    v[1, 1, 0] = "one-one-zero"
    v[1, 1, 1] = "one-one-one"

    assert v[key] == expect


def test_clear_default() -> None:
    v = Volume[tuple[int, int], str]("default")
    v.clear_default()

    with raises(NKeyError):
        _ = v[0, 0]


def test_default__get() -> None:
    assert Volume[tuple[int], str]("default").default == "default"


def test_default__get_unset() -> None:
    with raises(NoDefaultValue) as ex:
        _ = Volume[tuple[int], str]().default

    assert str(ex.value) == "The volume does not have a default value"


def test_default__set() -> None:
    v = Volume[tuple[int], str]()
    v.default = "default"
    assert v.default == "default"


def test_delete__empty() -> None:
    v = Volume[tuple[int, int], str]("default")
    v[0, 0] = "0-0"
    del v[0, 0]
    assert v[0, 0] == "default"


def test_delete__idempotent() -> None:
    v = Volume[tuple[int, int], str]("default")
    del v[0, 0]
    assert v[0, 0] == "default"


def test_delete__last() -> None:
    v = Volume[tuple[int, int], str]("default")
    v[0, 0] = "0-0"
    v[1, 0] = "1-0"
    v[1, 1] = "1-1"

    del v[0, 0]

    assert v[0, 0] == "default"
    assert v[1, 0] == "1-0"
    assert v[1, 1] == "1-1"


def test_delete__one() -> None:
    v = Volume[tuple[int, int], str]("default")
    v[0, 0] = "0-0"
    v[0, 1] = "0-1"
    v[1, 0] = "1-0"
    v[1, 1] = "1-1"

    del v[0, 0]

    assert v[0, 0] == "default"
    assert v[0, 1] == "0-1"
    assert v[1, 0] == "1-0"
    assert v[1, 1] == "1-1"


def test_delete__with_key_validator() -> None:
    v = Volume[tuple[int, int], str](key_validator=validate_key)
    with raises(InvalidKey):
        del v[2, 0]


@mark.parametrize(
    "keys, expect",
    [
        ((0, 0, 1), "Key 2 of (0, 0, 1) (1) does not exist"),
        ((0, 1, 0), "Key 1 of (0, 1, 0) (1) does not exist"),
        ((1, 0, 0), "Key 0 of (1, 0, 0) (1) does not exist"),
    ],
)
def test_getitem__no_default(keys: tuple[int, int, int], expect: str) -> None:
    v = Volume[tuple[int, int, int], str]()
    v[0, 0, 0] = "zero-zero-zero"

    with raises(NKeyError) as ex:
        _ = v[(keys)]

    assert str(ex.value) == expect


def test_getitem__with_key_validator() -> None:
    v = Volume[tuple[int, int], str](key_validator=validate_key)
    with raises(InvalidKey):
        _ = v[2, 0]


def test_iter() -> None:
    v = Volume[tuple[int, int, int], str]()
    v[1, 1, 1] = "1-1-1"
    v[1, 1, 2] = "1-1-2"
    v[1, 2, 0] = "1-2-0"
    v[2, 0, 0] = "2-0-0"

    assert list(v) == [
        Value((1, 1, 1), "1-1-1"),
        Value((1, 1, 2), "1-1-2"),
        Value((1, 2, 0), "1-2-0"),
        Value((2, 0, 0), "2-0-0"),
    ]


def test_iter__empty() -> None:
    assert not list(Volume[tuple[int, int, int], str]())


def test_setitem__with_key_validator() -> None:
    v = Volume[tuple[int, int], str](key_validator=validate_key)
    with raises(InvalidKey):
        v[2, 0] = "foo"


def test_validate_key__fail() -> None:
    v = Volume[tuple[int, int], str](key_validator=validate_key)
    with raises(InvalidKey) as ex:
        v.validate_key((2, 0))

    assert str(ex.value) == "Key (2, 0) failed validation (x 2 must be 0 or 1)"
    assert isinstance(ex.value.exception, ValueError)
    assert ex.value.key == (2, 0)


def test_validate_key__pass() -> None:
    v = Volume[tuple[int, int], str](key_validator=validate_key)
    v.validate_key((0, 0))
