# Cube class

The `Cube` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of three-dimensional volumes.

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

See the base [`Volume` class](/volume) for more construction detail.

## Usage

Values can be read and set via their keys as described in the base [`Volume` class](/volume), but `Cube` also provides `get()` and `set()` helper functions:


```python
from nvalues import Cube

cube = Cube[str, int, float, bool]()
cube.set("A", 0, 1.2, True)
print(cube.get("A", 0, 1.2))
# True
```
