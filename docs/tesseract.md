# Tesseract class

The `Tesseract` class is a wrapper around the [`Volume` class](/volume) to simplify the creation of four-dimensional volumes.

All the base functionality, such as default values, key accessors and iteration, is inherited by `Tesseract`.

## Construction

`Tesseract` requires five generic types:

1. `w` key type
1. `x` key type
1. `y` key type
1. `z` key type
1. Value type

For example, to create a `Tesseract` with `w` string keys, `x` string keys, `y` int keys, `z` float keys and boolean values:

```python
from nvalues import Tesseract

tesseract = Tesseract[str, str, int, float, bool]()
```

## Reading, setting and deleting values

Values can be read, set and deleted via their keys as described in the base [`Volume` class](/volume), but `Tesseract` also provides `get()`, `set()` and `delete()` helper functions:

```python
from nvalues import Tesseract

tesseract = Tesseract[str, str, int, float, bool](False)
tesseract.set("A", "B", 0, 1.2, True)
print(tesseract.get("A", "B", 0, 1.2))
# True

tesseract.delete("A", "B", 0, 1.2)
print(tesseract.get("A", "B", 0, 1.2))
# False
```
