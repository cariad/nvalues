# Grid class

The `Grid` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of two-dimensional volumes.

All the base functionality, such as default values, key accessors and iteration, is inherited by `Grid`.

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

## Reading, setting and deleting values

Values can be read, set and deleted via their keys as described in the base [`Volume` class](/volume), but `Grid` also provides `get()`, `set()` and `delete()` helper functions:

```python
from nvalues import Grid

grid = Grid[str, int, bool](False)
grid.set("A", 0, True)
print(grid.get("A", 0))
# True

grid.delete("A", 0)
print(grid.get("A", 0))
# False
```
