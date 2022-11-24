from pytest import fixture

from .types import CubeType, GridType, LineType, PenteractType, TesseractType


@fixture
def cube() -> CubeType:
    t = CubeType("default")
    t.set(0, 0, 0, "foo")
    return t


@fixture
def grid() -> GridType:
    t = GridType("default")
    t.set(0, 0, "foo")
    return t


@fixture
def line() -> LineType:
    t = LineType("default")
    t.set(0, "foo")
    return t


@fixture
def penteract() -> PenteractType:
    t = PenteractType("default")
    t.set(0, 0, 0, 0, 0, "foo")
    return t


@fixture
def tesseract() -> TesseractType:
    t = TesseractType("default")
    t.set(0, 0, 0, 0, "foo")
    return t
