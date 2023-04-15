from typing import Self


class Mixin_Renderable_Operation(Mixin_Renderable):

    def __str__(self: Self) -> str:
        return f'({super().__str__()})'

    def render(self: Self) -> str:
        """Alias of str."""
        return str(self)
        