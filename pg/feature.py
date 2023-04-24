
class Feature():

    def __init__(self, name: str) -> None:
        self._name = name
        self._value = False
        self._disabled = False

    def value(self, value: bool=None) -> bool:
        if value is not None:
            self._value = value
        return self._value
    
    def disable(self, disable: bool) -> None:
        self._disabled = disable
    
    def is_disabled(self) -> bool:
        return self._disabled
