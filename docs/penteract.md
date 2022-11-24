# Penteract class

The `Penteract` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of five-dimensional volumes.

All the base functionality, such as default values, key accessors and iteration, is inherited by `Penteract`.

## Construction

`Penteract` requires six generic types:

1. `v` key type
1. `w` key type
1. `x` key type
1. `y` key type
1. `z` key type
1. Value type

For example, to create a `Tesseract` with `v` integer keys, `w` string keys, `x` string keys, `y` int keys, `z` float keys and boolean values:

```python
from nvalues import Penteract

penteract = Penteract[int, str, str, int, float, bool]()
```

## Reading, setting and deleting values

Values can be read, set and deleted via their keys as described in the base [`Volume` class](/volume), but `Penteract` also provides `get()`, `set()` and `delete()` helper functions:

```python
from nvalues import Penteract

penteract = Penteract[int, str, str, int, float, bool](False)
penteract.set(3, "A", "B", 0, 1.2, True)
print(penteract.get(3, "A", "B", 0, 1.2))
# True

penteract.delete(3, "A", "B", 0, 1.2)
print(penteract.get(3, "A", "B", 0, 1.2))
# False
```
