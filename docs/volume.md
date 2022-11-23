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

# A spreadsheet of floats with horizontal alphabetic
# keys and vertical integer keys:
volume = Volume[tuple[str, int], float]()

# A cube of booleans with integer x, string y and float z keys:
volume = Volume[tuple[int, str, float], bool]()
```

An optional default value can be specified here too:

```python
from nvalues import Volume

volume = Volume[tuple[int, int], str](default_value="")
```

If you request a key that doesn't exist then this default value will be returned. If you request a key that doesn't exist without a default value set then the volume will raise `nvalues.exceptions.NKeyError`.

A default value can be set after construction via the `default` property and cleared by calling `clear_default()`.

## Usage

Values are read and set via their keys. For example:

```python
from nvalues import Volume

volume = Volume[tuple[int, int], str]()
volume[0, 0] = "zero"
print(volume[0, 0])
# "zero"
```
