from .types import TesseractType


def test_delete(tesseract: TesseractType) -> None:
    tesseract.delete(0, 0, 0, 0)
    assert tesseract.get(0, 0, 0, 0) == "default"


def test_get(tesseract: TesseractType) -> None:
    assert tesseract.get(0, 0, 0, 0) == "foo"
