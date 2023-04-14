from typing import Self

class Mixin_Renderable():

    def __str__(self: Self) -> str:
        return ''

    def render(self: Self) -> str:
        """Alias of str."""
        return str(self)
        