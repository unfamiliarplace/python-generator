from typing import Self
from components.pg_mixin_renderable import PG_Mixin_Renderable

class PG_Mixin_Generatable():

    def generate(self: Self) -> str|int|float|bool|PG_Mixin_Renderable:
        return None
