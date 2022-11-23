# NValues introduction

**NValues** is a Python package for working with _n_-dimensional volumes of data.

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

See the [`Volume` class](/volume) for more detail, or if you don't need more than five dimensions then see the [`Line`](/line), [`Grid`](/grid), [`Cube`](/cube), [`Tesseract`](/tesseract) or [`Penteract`](/penteract) wrapper classes for an easier life.

## Installation

**NValues** requires Python 3.9 or later and can be installed via [PyPI](https://pypi.org/project/nvalues/):

```console
pip install nvalues
```

## Support

Please raise bugs, feature requests and ask questions at [cariad/nvalues/issues](https://github.com/cariad/nvalues/issues).

## The Project

**NValues** is &copy; 2022 Cariad Eccleston and released under the [MIT License](https://github.com/cariad/nvalues/blob/main/LICENSE) at [cariad/nvalues](https://github.com/cariad/nvalues).

## The Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance backend and infrastructure engineer in the United Kingdom. You can find me at [cariad.earth](https://cariad.earth), [github/cariad](https://github.com/cariad), [linkedin/cariad](https://linkedin.com/in/cariad) and on Mastodon at [@cariad@tech.lgbt](https://tech.lgbt/@cariad).
