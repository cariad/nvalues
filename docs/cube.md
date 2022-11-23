# Cube class

The `Cube` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of three-dimensional volumes.

All the base functionality, such as default values, key accessors and iteration, is inherited by `Cube`.

## Construction

`Cube` requires four generic types:

1. `x` key type
1. `y` key type
1. `z` key type
1. Value type

For example, to create a `Cube` with `x` string keys, `y` integer keys, `z` float keys and boolean values:

```python
from nvalues import Cube

cube = Cube[str, int, float, bool]()
```

## Reading and setting values

Values can be read and set via their keys as described in the base [`Volume` class](/volume), but `Cube` also provides `get()` and `set()` helper functions:

```python
from nvalues import Cube

cube = Cube[str, int, float, bool]()
cube.set("A", 0, 1.2, True)
print(cube.get("A", 0, 1.2))
# True
```
