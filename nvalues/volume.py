from typing import Any, Dict, Generic, cast

from nvalues.exceptions import NKeyError, NoDefaultValue
from nvalues.types import KeysT, ValueT


class Volume(Generic[KeysT, ValueT]):
    """
    An n-dimensional volume of values.
    """

    class NullDefaultValue:
        """
        An unset default value. This is distinct from `None` which is a
        legitimate default value.
        """

    def __init__(
        self,
        default_value: ValueT | NullDefaultValue = NullDefaultValue(),
    ) -> None:
        self._default = default_value
        self._values: Dict[Any, Any] = {}

    def __getitem__(self, keys: KeysT) -> ValueT:
        context = self._values
        key_index = 0

        try:
            for index, key in enumerate(keys):
                key_index = index
                context = context[key]
        except KeyError:
            try:
                return self.default
            except NoDefaultValue as no_default_value:
                raise NKeyError(keys, key_index) from no_default_value

        return cast(ValueT, context)

    def __setitem__(self, keys: KeysT, value: ValueT) -> None:
        context = self._values
        index = 0

        while index < len(keys) - 1:
            key = keys[index]
            if key not in context:
                context[key] = {}
            context = context[key]
            index += 1

        context[keys[-1]] = value

    @property
    def default(self) -> ValueT:
        if isinstance(self._default, Volume.NullDefaultValue):
            raise NoDefaultValue()
        return self._default

    @default.setter
    def default(self, value: ValueT) -> None:
        self._default = value
