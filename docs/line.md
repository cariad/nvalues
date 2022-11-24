# Line class

The `Line` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of one-dimensional volumes.

All the base functionality, such as default values, key accessors and iteration, is inherited by `Line`.

## Construction

`Line` requires two generic types:

1. Key type
2. Value type

For example, to create a `Line` with integer keys and string values:

```python
from nvalues import Line

line = Line[int, str]()
```

## Reading, setting and deleting values

Values can be read, set and deleted via their keys as described in the base [`Volume` class](/volume), but `Line` also provides `get()`, `set()` and `delete()` helper functions:

```python
from nvalues import Line

line = Line[int, str]("default")

line.set(0, "zero")
print(line.get(0))
# "zero"

line.delete(0)
print(line.get(0))
# "default"
```
