# Volume class

The `Volume` class represents a strongly-typed _n_-dimensional volume of values.

## Construction

`Volume` requires two generic types:

1. Tuple of key types
2. Value type

For example:

```python
from nvalues import Volume

# A dictionary with integer keys and string values:
volume = Volume[tuple[int], str]()

# A grid with integer coordinates and string values:
volume = Volume[tuple[int, int], str]()

# A spreadsheet of floats with horizontal alphabetic keys and
# vertical integer keys:
volume = Volume[tuple[str, int], float]()

# A cube of booleans with integer x, string y and float z keys:
volume = Volume[tuple[int, str, float], bool]()
```

## Default values

By default, volumes will raise `nvalues.exceptions.NKeyError` if you try to read a key that doesn't exist.

To return a default value instead, you can either:

- Pass the default value as the `default` argument:

    ```python
    from nvalues import Volume

    volume = Volume[tuple[int, int], str](default="default")
    print(volume[0, 0])
    # "default"
    ```

- Pass a function that generates a default value as the `default_maker` argument:

    ```python
    from nvalues import Volume

    def make_default(key: tuple[int, int]) -> str:
        return f"default for {key}"

    volume = Volume[tuple[int, int], str](default_maker=make_default)
    print(volume[0, 0])
    # "default for (0, 0)"
    ```

Default values generated at runtime will be added to the volume, while static defaults will not.

## Reading, setting and deleting values

Values are read, set and deleted via their keys. For example:

```python
from nvalues import Volume

volume = Volume[tuple[str, int], float](0)

volume["A", 0] = 1.2
print(volume["A", 0])
# 1.2

del volume["A", 0]
print(volume["A", 0])
# 0
```

## Key validation

A `Volume` can be configured to reject invalid keys if a validator is passed in the initialiser or set on the `key_validator` property.

If set, the key validator is a function that examines the key and raises any exception if it's invalid. Any attempts to access an invalid key will result in `InvalidKey` being raised.

```python
from nvalues import Volume
from nvalues.exceptions import InvalidKey

max_x = 3
max_y = 4

def check_key_range(key: tuple[int, int]) -> None:
    x = key[0]
    if x < 0 or x > max_x:
        raise ValueError(f"x {x} must be 0-{max_x} inclusive")

    y = key[1]
    if y < 0 or y > max_y:
        raise ValueError(f"y {y} must be 0-{max_y} inclusive")

volume = Volume[tuple[int, int], str](key_validator=check_key_range)

try:
    volume[0, 17] = "foo"
except InvalidKey as ex:
    print(ex)

# Key (0, 17) failed validation (y 17 must be 0-4 inclusive)
```

## Iterating values

`Volume` natively supports iteration and will yield the key and value for every item it holds.

```python
from nvalues import Volume

volume = Volume[tuple[int, int], str]()

volume[0, 0] = "zero-zero"
volume[4, 0] = "four-zero"
volume[0, 4] = "zero-four"

for item in volume:
    print(f"Found {item.value} at {item.key}")

# Found zero-zero at (0, 0)
# Found zero-four at (0, 4)
# Found four-zero at (4, 0)
```
