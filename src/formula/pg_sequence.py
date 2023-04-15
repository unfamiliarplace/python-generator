from typing import Self

from mixins.pg_mixin_renderable import Mixin_Renderable


class Sequence(Mixin_Renderable):

    def __init__(self: Self, *components: object) -> None:
        self.components = components

    def __str__(self: Self) -> str:
        return ' '.join(f'{c}' for c in self.components)
