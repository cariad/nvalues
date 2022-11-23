# NValues

[![codecov](https://codecov.io/gh/cariad/nvalues/branch/main/graph/badge.svg?token=Qj6KxDEoVA)](https://codecov.io/gh/cariad/nvalues)

**NValues** is a Python package for working with _n_-dimensional volumes of data.

## Installation

**NValues** requires Python 3.9 or later and can be installed via [PyPI](https://pypi.org/project/nvalues/):

```console
pip install nvalues
```

## Usage

For example, to create a spreadsheet-like grid of float values with alphabetic `x` keys and integer `y` keys:

```python
from nvalues import Volume

grid = Volume[tuple[str, int], float]()
grid["A", 0] = 1.2
grid["B", 1] = 1.4
grid["C", 2] = 1.6

print(grid["A", 0])
# 1.2
```

See the [`Volume` class](#the-volume-class) for more detail, or if you don't need more than five dimensions then see the [`Line`](#the-line-class), [`Grid`](#the-grid-class), [`Cube`](#the-cube-class), [`Tesseract`](#the-tesseract-class) or [`Penteract`](#the-penteract-class) wrapper classes for an easier life.

## The `Volume` class

The `Volume` class represents a strongly-typed _n_-dimensional volume of values.

### Construction

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

An optional default value can be specified here too:

```python
from nvalues import Volume

volume = Volume[tuple[int, int], str](default_value="")
```

If you request a key that doesn't exist then this default value will be returned. If you request a key that doesn't exist without a default value set then the volume will raise `nvalues.exceptions.NKeyError`.

A default value can be set after construction via the `default` property and cleared by calling `clear_default()`.

### Usage

Values are read and set via their keys. For example:

```python
from nvalues import Volume

volume = Volume[tuple[int, int], str]()
volume[0, 0] = "zero"
print(volume[0, 0])
# "zero"
```

## The `Line` class

The `Line` class is a wrapper around the [`Volume` class](#the-volume-class) to simplify the creation of one-dimensional volumes.

### Construction

`Line` requires two generic types:

1. Key type
2. Value type

For example, to create a `Line` with integer keys and string values:

```python
from nvalues import Line

line = Line[int, str]()
```

See the base [`Volume` class](#the-volume-class) for more construction detail.

### Usage

Values can be read and set via their keys as described in the base [`Volume` class](#the-volume-class), but `Line` also provides `get()` and `set()` helper functions:


```python
from nvalues import Line

line = Line[int, str]()
line.set(0, "zero")
print(line.get(0))
# "zero"
```

## The `Grid` class

The `Grid` class is a wrapper around the [`Volume` class](#the-volume-class) to simplify the creation of two-dimensional volumes.

### Construction

`Grid` requires three generic types:

1. `x` key type
1. `y` key type
1. Value type

For example, to create a `Grid` with `x` string keys, `y` integer keys and boolean values:

```python
from nvalues import Grid

grid = Grid[str, int, bool]()
```

See the base [`Volume` class](#the-volume-class) for more construction detail.

### Usage

Values can be read and set via their keys as described in the base [`Volume` class](#the-volume-class), but `Grid` also provides `get()` and `set()` helper functions:


```python
from nvalues import Grid

grid = Grid[str, int, bool]()
grid.set("A", 0, True)
print(grid.get("A", 0))
# True
```

## The `Cube` class

The `Cube` class is a wrapper around the [`Volume` class](#the-volume-class) to simplify the creation of three-dimensional volumes.

### Construction

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

See the base [`Volume` class](#the-volume-class) for more construction detail.

### Usage

Values can be read and set via their keys as described in the base [`Volume` class](/volume), but `Cube` also provides `get()` and `set()` helper functions:


```python
from nvalues import Cube

cube = Cube[str, int, float, bool]()
cube.set("A", 0, 1.2, True)
print(cube.get("A", 0, 1.2))
# True
```

## The `Tesseract` class

The `Tesseract` class is a wrapper around the [`Volume` class](#the-volume-class) to simplify the creation of four-dimensional volumes.

### Construction

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

See the base [`Volume` class](#the-volume-class) for more construction detail.

### Usage

Values can be read and set via their keys as described in the base [`Volume` class](#the-volume-class), but `Tesseract` also provides `get()` and `set()` helper functions:

```python
from nvalues import Tesseract

tesseract = Tesseract[str, str, int, float, bool]()
tesseract.set("A", "B", 0, 1.2, True)
print(tesseract.get("A", "B", 0, 1.2))
# True
```

## The `Penteract` class

The `Penteract` class is a wrapper around the [`Volume` class](#the-volume-class) to simplify the creation of five-dimensional volumes.

### Construction

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

See the base [`Volume` class](#the-volume-class) for more construction detail.

### Usage

Values can be read and set via their keys as described in the base [`Volume` class](#the-volume-class), but `Penteract` also provides `get()` and `set()` helper functions:

```python
from nvalues import Penteract

penteract = Penteract[int, str, str, int, float, bool]()
penteract.set(3, "A", "B", 0, 1.2, True)
print(penteract.get(3, "A", "B", 0, 1.2))
# True
```

## Support

Please raise bugs, feature requests and ask questions at [cariad/nvalues/issues](https://github.com/cariad/nvalues/issues).

## The Project

**NValues** is &copy; 2022 Cariad Eccleston and released under the [MIT License](https://github.com/cariad/nvalues/blob/main/LICENSE) at [cariad/nvalues](https://github.com/cariad/nvalues).

## The Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance backend and infrastructure engineer in the United Kingdom. You can find me at [cariad.earth](https://cariad.earth), [github/cariad](https://github.com/cariad), [linkedin/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
