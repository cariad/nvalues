# Line class

The `Line` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of one-dimensional volumes.

## Construction

`Line` requires two generic types:

1. Key type
2. Value type

For example, to create a `Line` with integer keys and string values:

```python
from nvalues import Line

line = Line[int, str]()
```

See the base [`Volume` class](/volume) for more construction detail.

## Usage

Values can be read and set via their keys as described in the base [`Volume`](/volume) class, but `Line` also provides `get()` and `set()` helper functions:


```python
from nvalues import Line

line = Line[int, str]()
line.set(0, "zero")
print(line.get(0))
# "zero"
```
