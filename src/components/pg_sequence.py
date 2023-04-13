from typing import Self
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Sequence(PG_Mixin_Renderable):

    def __init__(self: Self, *components: object) -> None:
        self.components = components

    def __str__(self: Self) -> str:
        return ' '.join(f'{c}' for c in self.components)
