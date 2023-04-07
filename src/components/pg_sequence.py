from components.pg_renderable import PG_Renderable
from typing import Self

class PG_Sequence(PG_Renderable):

    def __init__(self: Self, *components: object) -> None:
        self.components = components

    def __str__(self: Self) -> str:
        return ' '.join(f'{c}' for c in self.components)
