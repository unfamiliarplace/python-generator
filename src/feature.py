from typing import Self

class Feature():
    _name: str
    _value: bool
    _disabled: bool

    def __init__(self: Self, name: str) -> None:
        self._name = name
        self._value = False
        self._disabled = False

    def value(self: Self, value: bool=None) -> bool:
        if value is not None:
            self._value = value
        return self._value
    
    def disable(self: Self, disable: bool) -> None:
        self._disabled = disable
    
    def is_disabled(self: Self) -> bool:
        return self._disabled
