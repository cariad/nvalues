# Grid class

The `Grid` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of two-dimensional volumes.

## Construction

`Grid` requires three generic types:

1. `x` key type
1. `y` key type
1. Value type

For example, to create a `Grid` with `x` string keys, `y` integer keys and boolean values:

```python
from nvalues import Grid

grid = Grid[str, int, bool]()
```

See the base [`Volume` class](/volume) for more construction detail.

## Usage

Values can be read and set via their keys as described in the base [`Volume`](/volume) class, but `Grid` also provides `get()` and `set()` helper functions:


```python
from nvalues import Grid

grid = Grid[str, int, bool]()
grid.set("A", 0, True)
print(grid.get("A", 0))
# True
```
