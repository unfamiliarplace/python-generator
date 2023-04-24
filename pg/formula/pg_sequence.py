from typing import Self
import pg

class Sequence(pg.Mixin_Renderable):

    def __init__(self: Self, *components: object) -> None:
        self.components = components

    def __str__(self: Self) -> str:
        return ' '.join(f'{c}' for c in self.components)
