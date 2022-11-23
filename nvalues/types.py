from typing import Any, TypeVar

# TODO: Use TypeVarTuple when mypy supports it.
# KeysT = TypeVarTuple("KeysT")
KeysT = TypeVar("KeysT", bound=tuple[Any, ...])
ValueT = TypeVar("ValueT")

XKeyT = TypeVar("XKeyT")
